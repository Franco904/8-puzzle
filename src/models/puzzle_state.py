import random


class PuzzleState(list):
    def __init__(self, pieces):
        super().__init__(int(piece) for piece in pieces)
        self.__must_exclude = False

    @property
    def must_exclude(self):
        return self.__must_exclude

    @must_exclude.setter
    def must_exclude(self, must_exclude):
        self.__must_exclude = must_exclude

    """
        Vizinhos:
        # 0: 1 e 3 (Vertice)
        # 1: 0, 2 e 4 (Aresta)
        # 2: 1 e 5 (Vertice)
        # 3: 0, 4 e 6 (Aresta)
        # 4: 1, 3, 5 e 7 (Centro)
        # 5: 2, 4 e 8 (Aresta)
        # 6: 3 e 7 (Vertice)
        # 7: 4, 6 e 8 (Aresta)
        # 8: 5 e 7 (Vertice)
    """
    def children(self):
        nine_index = self.index(9)

        neighbors = []
        if nine_index == 0:
            neighbors = [1, 3]
        elif nine_index == 1:
            neighbors = [0, 2, 4]
        elif nine_index == 2:
            neighbors = [1, 5]
        elif nine_index == 3:
            neighbors = [0, 4, 6]
        elif nine_index == 4:
            neighbors = [1, 3, 5, 7]
        elif nine_index == 5:
            neighbors = [2, 4, 8]
        elif nine_index == 6:
            neighbors = [3, 7]
        elif nine_index == 7:
            neighbors = [4, 6, 8]
        elif nine_index == 8:
            neighbors = [5, 7]

        # neighbors = [nine_index - 3, nine_index - 1, nine_index + 1, nine_index + 3]
        #
        # pieces_to_exclude = []
        # if nine_index == 2:
        #     pieces_to_exclude.extend([neighbors[0], neighbors[2]])
        # elif nine_index == 6:
        #     pieces_to_exclude.extend([neighbors[1], neighbors[3]])
        # else:
        #     for piece in neighbors:
        #         if piece < 0 or piece > 8:
        #             pieces_to_exclude.append(piece)
        #
        # neighbors = [n for n in neighbors if n not in pieces_to_exclude]
        # print(neighbors)

        children_states = []
        for n in neighbors:
            state = self.copy()

            item = state[n]
            state[nine_index] = item
            state[n] = 9

            children_states.append(state)

        return children_states

    def print_formatted(self):
        print(f'[{self[0]}] [{self[1]}] [{self[2]}]')
        print(f'[{self[3]}] [{self[4]}] [{self[5]}]')
        print(f'[{self[6]}] [{self[7]}] [{self[8]}]')

    @staticmethod
    def random():
        pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(pieces)

        return PuzzleState(pieces)

    @staticmethod
    def empty():
        return PuzzleState([])
