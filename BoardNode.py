from queue import PriorityQueue

class BoardNode:
    __children = None

    def __init__(self, board):
        self.board = board

    def get_possible_children(self):
        # based on the position there are different children that can be generated
        self.__children = PriorityQueue()


    def __is_corner_zero(self):
        return self.board[0][0] == 0 or self.board[0][3] == 0 or \
               self.board[1][0] == 0 or self.board[1][3] == 0

    def __get_regular_move_states(self):
        return

    def __get_wrapping_move_states(self):
        return

    def __get_diagonal_move_states(self):
        return

