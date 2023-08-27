import time
from src.models.puzzle_state import PuzzleState


goal_state = PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9])


class Puzzle:
    """
        Creates a new 8 puzzle game.

        Here we are storing all the pieces in a simple list object to handle the state when
        a move is performed.

        Piece number 9 represents the empty piece.
    """

    def __init__(self):
        # self.__open_states = PuzzleState.random()

        initialState = PuzzleState([1, 2, 3, 4, 5, 6, 7, 9, 8])

        '''
            #todo transformar list de states em classe própria StatesSet
                - herda de lista, mas implementa função própria de set (garantir exclusividade dos elementos)
                - caso um elemento seja repetido, deverá implementar a lógica de substituição pelo custo
        '''  
        self.__open_states = [initialState]
        self.__visited_states = []
        self.__visits_counter = 0

        


    """
        Set up puzzle game.
    """

    def start_search(self):
        self.__print_start()
        self.__search()


    def __search(self):

        while(len(self.__open_states) != 0):
            
            current_state = self.__open_states[0]
            self.__open_states.remove(current_state)
            '''
            print("state")
            current_state.print_formatted()
            time.sleep(2)
            '''
            
            self.__increment_counter()

            if(current_state == goal_state):
                return self.__end_search(True, current_state)
            else:
                next_states = current_state.generateNextStates()

                for new_state in next_states:

                    if(new_state not in self.__open_states and new_state not in self.__visited_states):
                        self.__open_states.append(new_state) #todo alterar para considerar o peso na ordenação da inclusão
                    #todo
                    #else:
                    #   lógica para remoção do maior e manutenção do menor

            self.__visited_states.append(current_state)
            #todo sort open list

    def __end_search(self, hasFound: bool, finalState):
        if hasFound:
            print(f'Estado final:')
            finalState.print_formatted()
            print('')

            print(f'Contagem de movimentos: {finalState.acc_cost}')
            print(f'nodos visitados: {self.__visits_counter}')
        else:
            print('O estado final não foi encontrado!')

    def __print_start(self):
        print(f'======== 8 PUZZLE ========\n')
        print(f'Estado inicial:')
        self.__open_states[0].print_formatted()
        print('')

    def __increment_counter(self):
        self.__visits_counter +=1
