import bisect

class StateSet():
    def __init__(self, initial_state):
        # Cria duas listas: uma para estados abertos e outra para estados visitados.
        self.__open_states = [initial_state]
        self.__visited_states = []

    def open_size(self):
        # Retorna o número de estados na lista de estados abertos.
        return len(self.__open_states)

    def add_open_state(self, new_state):
        # Adiciona um novo estado à lista de estados abertos, garantindo exclusividade dos membros e utilização do elemento de menor custo
        open_index = bisect.bisect_left(self.__open_states, new_state)
        visited_index = bisect.bisect_left(self.__visited_states, new_state)

      
        open_repeated = self.__check_repetition(new_state, open_index, self.__open_states)
        visited_repeated = self.__check_repetition(new_state, visited_index, self.__visited_states)
        
        if(not open_repeated and not visited_repeated):
            self.__open_states.insert(open_index, new_state)
        elif(open_repeated and new_state < self.__open_states[open_index]):
            self.__open_states[open_index] = new_state
        elif(visited_repeated and new_state < self.__visited_states[visited_index]):
            self.__visited_states.pop(visited_index)
            self.__open_states.insert(open_index, new_state)
        
   
    def __check_repetition(self, state, index, state_list):
        return index < len(state_list) and state == state_list[index]
       

    def add_visited_state(self, visited_state):
        # Adiciona um estado à lista de estados visitados.
        visited_index = bisect.bisect_left(self.__visited_states, visited_state)
        self.__visited_states.insert(visited_index, visited_state)

    def get_next_state(self):
        # Retorna o primeiro estado da lista de estados abertos e o remove da lista.
        return self.__open_states.pop(0)

    def print_next_state(self):
        self.__open_states[0].print_formatted()
