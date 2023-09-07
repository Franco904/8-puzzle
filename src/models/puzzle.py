import time
from src.models.puzzle_state import PuzzleState
from src.models.state_set import StateSet
start_time = 0
end_time = 0
goal_state = PuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 9))

'''
#* Casos de teste
#* Difícil: [9,6,5,2,4,7,8,1,3] - 16
#* Difícil: [6,4,5, 2, 8, 9, 7, 3, 1] - 17
#* Médio: [2,3,9, 1, 5, 8, 7, 6, 4] - 10
#* Médio: [2, 6, 1, 9, 3, 5, 7, 4, 8] - 11
#* Fácil: [1, 2, 3, 7, 5, 6, 4, 8, 9] - 2

'''

class Puzzle:
    """
        Creates a new 8 puzzle game.

        Here we are storing all the pieces in a simple list object to handle the state when
        a move is performed.

        Piece number 9 represents the empty piece.
    """

    def __init__(self):
        # self.__open_states = PuzzleState.random()

        initial_state = PuzzleState((4,7,5,9,2,1,3,6,8))
        self.__state_set = StateSet(initial_state)
        self.__visits_counter = 0
        self.__found = False

        
    """
        Set up puzzle game.
    """

    def start_search(self):
        self.__print_start()
        self.__search()


    def __search(self):

        start_time = time.time()
        # Enquanto houver estado aberto
        while(self.__state_set.open_size() != 0):
            
            # Obtém o próximo estado
            current_state = self.__state_set.get_next_state()

            '''
            print("state")
            current_state.print_formatted()
            time.sleep(2)
            '''

            self.__increment_counter()
            # Verifica se o novo estado é o objetivo. Caso positivo, encerra a busca. Caso negativo, gera estados filhos.
            if(current_state == goal_state):
                self.__found = True
                break
            else:
                child_states = current_state.generate_child_states()

                for child_state in child_states:
                    self.__state_set.add_open_state(child_state)

            # Adiciona estado analisado à lista de visitados.        
            self.__state_set.add_visited_state(current_state)
        
        end_time = time.time()
        self.__end_search(current_state, end_time - start_time)

    def __end_search(self, final_state, total_time):
        
        print(f'Tempo de busca: {total_time} seconds')
        print(f'nodos visitados: {self.__visits_counter}')

        if self.__found:
            print(f'Estado final:')
            final_state.print_formatted()
            print('')    
            print(f'Contagem de movimentos: {final_state.acc_cost}')
            print('Caminho para o resultado: ')
            final_state.display_path()
        else:
            print('O estado final não foi encontrado!')

    def __print_start(self):
        print(f'======== 8 PUZZLE ========\n')
        print(f'Estado inicial:')
        print('')
        self.__state_set.print_next_state()
        print('')


    def __increment_counter(self):
        self.__visits_counter +=1
