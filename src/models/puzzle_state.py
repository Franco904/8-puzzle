import random
import time
import math


EMPTY = 9
BOARD_SIZE = 9
ROW_SIZE = 3

COORDS = {}
for i in range(9):
    COORDS[i] = (i%ROW_SIZE, i//ROW_SIZE)

class PuzzleState():
    def __init__(self, pieces, cost=0, previous_state=None):
        
        self.__state = pieces
        self.__previous_state = previous_state
        self.__acc_cost = cost
        self.__heuristic = 0

    
    def __eq__(self, other):
        # Verifica se dois estados são iguais com base em suas configurações de peças.
        return self.__state == other.state

    def __lt__(self, other):
        # Define a ordem de prioridade para a fila de prioridade usada em algoritmos de busca.
        # É baseado na soma do custo acumulado e da heurística do estado.
        return self.__acc_cost + self.__heuristic < other.acc_cost + other.heuristic

    @staticmethod
    def random():
        pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(pieces)

        return PuzzleState(pieces)

    @staticmethod
    def empty():
        return PuzzleState([])

    @property
    def state(self):
        return self.__state

    @property
    def acc_cost(self):
        return self.__acc_cost

    @property
    def heuristic(self):
        return self.__heuristic

    @property
    def previous_state(self):
        return self.__previous_state
    
    def generateNextStates(self):
        # Gera e retorna uma lista de estados possíveis resultantes de movimentos válidos do estado atual.

        empty_index = self.__state.index(EMPTY)
        next_states = []

        movements = [{"index": empty_index-3, "direction": False},
                     {"index": empty_index+3, "direction": False},
                     {"index": empty_index-1, "direction": True},
                     {"index": empty_index+1, "direction": True},
                     ]

        for movement in movements:
            try:
                next_states.append(self.__move_piece(
                    empty_index, movement["index"], movement["direction"]))
            except IndexError:
                pass

        return next_states

    def __switch_elements(self, empty_index, new_index):
        # Troca a posição do elemento vazio e de outro elemento.
        new_state = self.state[:]

        temp = new_state[new_index]
        new_state[new_index] = EMPTY
        new_state[empty_index] = temp

        return new_state

    def __move_piece(self, empty_index, new_index, horizontal_move=False):
        # Move uma peça para a posição vazia e gera um novo estado.
        if (new_index < 0 or new_index > BOARD_SIZE):
            raise IndexError("Invalid Movement")

        if (horizontal_move is True and (new_index // ROW_SIZE != empty_index // ROW_SIZE)):
            raise IndexError("Invalid Movement")

        new_state = self.__switch_elements(empty_index, new_index)
        new_cost = self.__acc_cost+1

        return PuzzleState(new_state, new_cost, self)

    
    def calculateBasicHeuristic(self):
        '''
            O state objetivo é [1,2,3,4,5,6,7,8,9]. Como listas iniciam indexação em 0, tem-se que um elemento estará em sua posição desejada se seu valor - seu index for igual a 1
        
            Calcula-se a heurística básica contando quantos elementos estão fora de posição.

            #!heurística ficará superestimada, considerando o custo unitário dos movimentos? Verificar e, se necessário, alterar para uma escala mais adequada (talvez dividir por 10?)
        '''
        heuristic = 0

        for i, piece_value in enumerate(self.__state):
            if (piece_value - i) != 1:
                heuristic += 1
        
        self.__heuristic = heuristic


    def calculateAdvancedHeuristic(self):
        
        '''
            Utiliza a mesma lógica da heurística anterior para identificar o estado desejado.

            A heurística é calculada como a soma das distâncias atuais (em linha reta) de cada peça para a sua posição correta.
        
            #!Heurística superestimada? Verificar e, se necessário, buscar forma de colocar em escala adequada
        '''

        heuristic = 0
        for i, piece_value in enumerate(self.__state):
            
            current_coord = COORDS[i]
            desired_coord = COORDS[piece_value-1]

            distance = math.sqrt((current_coord[0]-desired_coord[0])^2 - (current_coord[1] - desired_coord[1])^2)
            heuristic += distance

        self.__heuristic = heuristic



    def print_formatted(self):

        state = self.__state

        print(f'[{state[0]}] [{state[1]}] [{state[2]}]')
        print(f'[{state[3]}] [{state[4]}] [{state[5]}]')
        print(f'[{state[6]}] [{state[7]}] [{state[8]}]')

    def display_path(self):
        # Exibe o caminho do estado inicial até o estado atual.
        path = [self]
        previous = self.__previous_state

        while(previous is not None):
            path.append(previous)
            previous = previous.previous_state
        
        path.reverse()
        for i, state in enumerate(path):
            print(f'Step {i+1}:')
            state.print_formatted()
            print("")