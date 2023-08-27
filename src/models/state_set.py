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

        if (new_state not in self.__open_states and new_state not in self.__visited_states):
            self.__open_states.append(new_state)
        elif (new_state in self.__open_states):
            self.__pick__cheapest_state(new_state, self.__open_states)
        else:
            self.__pick__cheapest_state(new_state, self.__visited_states)

        self.__open_states.sort()

    def __pick__cheapest_state(self, new_state, state_list):
        # Método interno usado para escolher o estado mais barato entre o novo estado e um estado já presente na lista.
        # Remove o estado existente se o novo tiver um custo menor, e adiciona o novo estado à lista.

        repeated_state_index = state_list.index(new_state)

        if (new_state < state_list[repeated_state_index]):
            state_list.pop(repeated_state_index)
            self.__open_states.append(new_state)

    def add_visited_state(self, visited_state):
        # Adiciona um estado à lista de estados visitados.
        self.__visited_states.append(visited_state)

    def get_next_state(self):
        # Retorna o primeiro estado da lista de estados abertos e o remove da lista.
        return self.__open_states.pop(0)

    def print_next_state(self):
        self.__open_states[0].print_formatted()
