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
        
        open_index, visited_index = self.__get_insertion_indexes(new_state)
        open_repeated, visited_repeated = self.__check_repetition(new_state, open_index, visited_index)
        
        if(not open_repeated and not visited_repeated):
            return self.__open_states.insert(open_index, new_state)
        
        if(open_repeated and new_state < self.__open_states[open_index]):
            self.__open_states[open_index] = new_state
            return
        
        if(visited_repeated and new_state < self.__visited_states[visited_index]):
            self.__visited_states.pop(visited_index)
            return self.__open_states.insert(open_index, new_state)
        
   

    def __get_insertion_indexes(self, new_state):
        open_index = bisect.bisect_left(self.__open_states, new_state)
        visited_index = bisect.bisect_left(self.__visited_states, new_state)

        return (open_index, visited_index)


    def __check_repetition(self, state, open_index, visited_index):


        #? Extrair mais uma função para retirar repetição? Talvez deixar (evitar excesso de fragmentação do código)
        open_repeated = open_index < len(self.__open_states) and state == self.__open_states[open_index]
        visited_repeated = visited_index < len(self.__visited_states) and state == self.__visited_states[visited_index]
        
        return (open_repeated, visited_repeated)
       

    def add_visited_state(self, visited_state):
        # Adiciona um estado à lista de estados visitados.
        visited_index = bisect.bisect_left(self.__visited_states, visited_state)
        self.__visited_states.insert(visited_index, visited_state)

    def get_next_state(self):
        # Retorna o primeiro estado da lista de estados abertos e o remove da lista.
        return self.__open_states.pop(0)

    def print_next_state(self):
        self.__open_states[0].print_formatted()
