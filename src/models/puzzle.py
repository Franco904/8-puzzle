from src.models.puzzle_state import PuzzleState

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Puzzle:
    """
        Creates a new 8 puzzle game.

        Here we are storing all the pieces in a simple list object to handle the state when
        a move is performed.

        Piece number 9 represents the empty piece.
    """
    def __init__(self):
        # self.__open_states = PuzzleState.random()

        self.__open_states = [PuzzleState([1, 2, 3, 4, 5, 6, 7, 9, 8])]
        self.__visited_states = []

        self.__current_state = PuzzleState.empty()

        self.__count_movements = 0

        print(f'======== 8 PUZZLE ========\n')
        print(f'Estado inicial:')
        self.__open_states[0].print_formatted()
        print('')

    """
        Set up puzzle game.
    """
    def start_puzzle(self):
        self.__move()

    """
        Perform puzzle movement following the breadth first search algorithm.
    """
    def __move(self):
        self.__current_state = self.__open_states[0]

        self.__open_states.remove(self.__open_states[0])
        self.__visited_states.append(self.__current_state)

        # Goal found
        if self.__current_state == goal_state:
            self.__end_puzzle(hasFound=True)
            return

        # Loop check
        children = [PuzzleState(c) for c in self.__current_state.children()]
        for c in children:
            if c in self.__open_states or c in self.__visited_states:
                c.must_exclude = True

        children = [c for c in children if not c.must_exclude]

        # Queue in open states
        self.__open_states.extend(children)

        if len(self.__open_states) > 0:
            self.__count_movements += 1

            # Recursion
            self.__move()
        else:
            self.__end_puzzle(hasFound=False)

    """
        Ends the game.
    """
    def __end_puzzle(self, hasFound: bool):
        if hasFound:
            print(f'Estado final:')
            self.__current_state.print_formatted()
            print('')

            print(f'Contagem de movimentos: {self.__count_movements}')
        else:
            print('O estado final não foi encontrado!')

