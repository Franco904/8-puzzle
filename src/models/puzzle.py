import time

from settings import SETTINGS
from src.models.puzzle_state import PuzzleState
from src.models.state_set import StateSet

start_time = 0
end_time = 0
goal_state = PuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 9))


class Puzzle:
    """
        Creates a new 8 puzzle game.

        Here we are storing all the pieces in a simple list object to handle the state when
        a move is performed.

        Piece number 9 represents the empty piece.
    """

    def __init__(self):
        
        initial_state = PuzzleState(SETTINGS["INITIAL_STATE"])
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
        while self.__state_set.open_size() != 0:
            
            # Obtém o próximo estado
            current_state = self.__state_set.get_next_state()

            '''
            print("state")
            current_state.print_formatted()
            time.sleep(2)
            '''

            self.__increment_counter()

            # Verifica se o novo estado é o objetivo. Caso positivo, encerra a busca. Caso negativo, gera estados
            # filhos.
            if current_state == goal_state:
                self.__found = True
                break
            else:
                child_states = current_state.generate_child_states()

                for child_state in child_states:

                    self.__apply_heuristic(child_state)
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

    def __apply_heuristic(self, child):

        '''
            Aplica heurística básica se HEURISTIC for definida como 1 nas configurações.
            Aplica a heurística avançada caso a configuração seja definida como 2.
            Não executada nada caso o valor da configuração seja diferente (modo sem heurística)
        '''

        heuristic = SETTINGS["HEURISTIC"]

        if heuristic == 1:
            child.calculate_basic_heuristic()
        
        if heuristic == 2:
            child.calculate_advanced_heuristic()

    def __print_start(self):
        print(f'======== 8 PUZZLE ========\n')
        print(f'Estado inicial:')
        print('')
        self.__state_set.print_next_state()
        print('')

    def __increment_counter(self):
        self.__visits_counter += 1
