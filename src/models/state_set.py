import bisect

class StateSet():
    def __init__(self, initial_state):
        # Cria duas listas: uma para estados abertos e outra para estados visitados.
         
        self.__open_states_list = [initial_state]
        self.__open_states_set = {initial_state.state}
        self.__visited_states = {}

    def open_size(self):
        # Retorna o número de estados na lista de estados abertos.
        return len(self.__open_states_list)

    #todo refactor
    def add_open_state(self, new_state):
        # Adiciona um novo estado à lista de estados abertos, garantindo exclusividade dos membros e utilização do elemento de menor custo
        

        # Verifica se o novo estado já foi incluído em alguma das listas
        open_repeated = new_state.state in self.__open_states_set
        visited_repeated = True and self.__visited_states.get(new_state.state, False)

        # Se o novo estado não está em nenhuma das listas, faz sua inclusão na lista de abertos
        if(not open_repeated and not visited_repeated):
            # Obtém índices para inserção do novo estado
            open_index = self.__get_insertion_index(new_state)
            self.__open_states_set.add(new_state.state)
            return self.__open_states_list.insert(open_index, new_state)
        
        # Se o novo estado já está na lista de abertos, mantém o estado com menor custo
        if(open_repeated):
            open_index = self.__open_states_list.index(new_state)

            if new_state < self.__open_states_list[open_index]:
                self.__open_states_list[open_index] = new_state
                return
        
        # Se o novo estado já está na lista de visitados, mas possui um custo menor, retira o antigo da lista de visitados e inclui o novo na lista de abertos
        if(visited_repeated):

            visited_state = self.__visited_states[new_state.state]

            if new_state < visited_state:
                
                open_index = self.__get_insertion_index(new_state)
                self.__visited_states.pop(new_state.state)
                self.__open_states_set.add(new_state.state)
                return self.__open_states_list.insert(open_index, new_state)
        

    def __get_insertion_index(self, new_state):
        # Obtém a posição de inserção do novo estado nas listas de estados abertos e visitados

        open_index = bisect.bisect_left(self.__open_states_list, new_state)
        
        return open_index


    def __check_repetition(self, state, open_index):
        # Verifica se o estado está repetido em alguma das listas
        
        
        #open_repeated = open_index < len(self.__open_states) and state == self.__open_states[open_index]
        #visited_repeated = True and self.__visited_states.get(state.state, False)
        
        #return (open_repeated, visited_repeated)
        pass
       

    def add_visited_state(self, visited_state):
        # Adiciona um estado à lista de estados visitados.

        #todo remove commented code
        #visited_index = bisect.bisect_left(self.__visited_states, visited_state)
        #self.__visited_states.insert(visited_index, visited_state)

        state = visited_state.state
        self.__visited_states[state] = visited_state

    def get_next_state(self):
        # Retorna o primeiro estado da lista de estados abertos e o remove da lista.

        next_state = self.__open_states_list.pop(0)


        
        self.__open_states_set.remove(next_state.state)
        return next_state

    def print_next_state(self):
        self.__open_states_list[0].print_formatted()
