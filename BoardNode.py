from queue import PriorityQueue
import numpy as np

regular_move_cost = 1
wrapping_move_cost = 2
diagonal_move_cost = 3


def __add_list_to_pq(q, q2, edge_cost):
    for item in q2:
        q.put((edge_cost, item))


class BoardNode:
    __children = None

    def __init__(self, board):
        self.board = board

    def get_possible_children(self):

        children = PriorityQueue()

        BoardNode.__add_list_to_pq(children, self.__get_regular_move_states(), regular_move_cost)

        if self.__is_corner_zero():
            BoardNode.__add_list_to_pq(children, self.__get_wrappint_move_states(), wrapping_move_cost)
            BoardNode.__add_list_to_pq(children, self.__get_diagonal_move_states(), diagonal_move_cost)
        return children

    def __is_corner_zero(self):
        return self.board[0][0] == 0 or self.board[0][3] == 0 or \
               self.board[1][0] == 0 or self.board[1][3] == 0

    def __get_regular_move_states(self):
        nodes = []

        zero_location = self.__get_zero_location()
        if ()
            nodes

        return

    def __get_wrapping_move_states(self):
        return

    def __get_diagonal_move_states(self):
        return

    def swap_elements(self, a_tuple, b_tuple):
        a = self.board[a_tuple[0]][a_tuple[1]]
        b = self.board[b_tuple[0]][b_tuple[1]]

        self.board[a_tuple[0]][a_tuple[1]] = b
        self.board[b_tuple[0]][b_tuple[1]] = a

    # returns (0, 2) if 0 is at 1st row, 3 column
    def __get_zero_location(self):
        (i, j) = np.where(self.board == 0)
        return i[0], j[0]

ffffffff
