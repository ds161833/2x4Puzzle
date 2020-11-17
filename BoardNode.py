from queue import PriorityQueue
import numpy as np

regular_move_cost = 1
wrapping_move_cost = 2
diagonal_move_cost = 3


def add_list_to_pq(q, q2, edge_cost):
    for item in q2:
        q.put((edge_cost, item))


class BoardNode:
    __children = None
    __board_height = None
    __board_width = None

    def __init__(self, board):
        self.board = board
        self.__board_height = len(board)
        self.__board_width = len(board[0])

    def get_possible_children(self):

        children = PriorityQueue()

        add_list_to_pq(children, self.__get_regular_move_states(), regular_move_cost)

        if self.__is_corner_zero():
            add_list_to_pq(children, self.__get_wrappint_move_states(), wrapping_move_cost)
            add_list_to_pq(children, self.__get_diagonal_move_states(), diagonal_move_cost)
        return children

    def __is_corner_zero(self):
        return self.board[0][0] == 0 or self.board[0][3] == 0 or \
               self.board[1][0] == 0 or self.board[1][3] == 0

    def get_regular_move_states(self):

        go_up = (-1, 0)
        go_down = (1, 0)
        go_right = (0, 1)
        go_left = (0, -1)

        directions = [go_up, go_down, go_right, go_left]
        allow_wrapping = False

        return self.__generate_children_from_directions(directions, allow_wrapping)

    def __get_wrapping_move_states(self):
        generated_children = []

        return generated_children

    def __get_diagonal_move_states(self):
        generated_children = []

        return generated_children

    # directions - list of tuples for directions
    def __generate_children_from_directions(self, directions, allow_wrapping):
        generated_children = []

        for direction in directions:
            child = self.__generate_state_if_zero_moves_into_new_direction(direction, allow_wrapping)
            if child is not None:
                generated_children.append(child)

        return generated_children

    def __generate_state_if_zero_moves_into_new_direction(self, move_direction, allow_wrapping):
        current_zero_coordinates = self.__get_zero_coordinates()
        new_zero_coordinates = self.__get_destination_coordinates(current_zero_coordinates, move_direction)
        # now that we have destination coordinates after applying move_direction (1, 0)
        # we need to check if we the move was legal if wrapping was not allowed
        # e.g. for regular moves we cannot jump from index 4 to index 0 if board_width is 4,
        # so we have to abandon this move
        if (new_zero_coordinates[0] >= self.__board_height or new_zero_coordinates[0] < 0 or
                new_zero_coordinates[1] >= self.__board_width or new_zero_coordinates[1] < 0)\
                and not allow_wrapping:
            return None
        else:
            # if wrapping was allowed AND has occurred the '%' division will take care of wrapping:
            # e.g. if board width is 7 and new row coordinate (new_zero_coordinates[1]) is out
            # of boundaries e.g. is now 7, 7 mod 7 = 0
            # -1 mod 7 equals 6
            # 4 mod 7 equals 4 (so for regular moves mod division has no effect)
            new_zero_coordinates = (new_zero_coordinates[0] % self.__board_height, new_zero_coordinates[1] % self.__board_width)
            return self.__get_new_board_from_swapping_elements(current_zero_coordinates, new_zero_coordinates)

    # swap_direction is a tuple of direction coordinated e.g. (1, 0) means go up, (-1, 0) means go down,
    # (1,1) means go up and right, (-1, -1) means go down and left
    @staticmethod
    def __get_destination_coordinates(zero_coordinates, direction):
        # if zero_coordinates was (1, 2), after adding direction (1, 0) new_zero_coordinates mean (2, 2)
        # which is an illegal regular move, or a legal wrapping move for boards with more than 2 rows
        new_zero_coordinates = (zero_coordinates[0] + direction[0], zero_coordinates[1] + direction[1])
        return new_zero_coordinates

    # returns location of a 0 element on the current board
    # for:
    # 6 1 2 3
    # 4 5 0 7
    # returns (1, 2) <- coordinates
    def __get_zero_coordinates(self):
        (i, j) = np.where(self.board == 0)
        return i[0], j[0]

    # generates a new board from current one and swaps 'a' and 'b'
    def __get_new_board_from_swapping_elements(self, a_tuple, b_tuple):
        a = self.board[a_tuple[0]][a_tuple[1]]
        b = self.board[b_tuple[0]][b_tuple[1]]

        new_board = BoardNode(self.board.copy())

        new_board.board[a_tuple[0]][a_tuple[1]] = b
        new_board.board[b_tuple[0]][b_tuple[1]] = a
        return new_board
