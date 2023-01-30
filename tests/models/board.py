from random import randrange
from models.house import Houses


class Board:
    def __init__(self):
        self.board = []
        self.houses = Houses()

    def get_board(self):
        return self.board

    def generate_positive_board(self):
        self.board = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
                      [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    def generate_negative_board(self):
        self.board = [[], []]
        if len(self.board) != 6:
            return self.generate_positive_board()

    def create_board_with_different_number_of_houses(self):
        number_of_houses = 10
        self.board = [[1, 2, 3, 4, 5, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

        self.houses.set_number_of_houses(number_of_houses)
        return number_of_houses

    def create_custom_board(self, board):
        self.board = board

    def use_crystal(self,coordinates=None):
        if coordinates:
            return True
        return False

    def merge_houses(self, houses, expected_result):
        if houses:
            self.board = expected_result
            return None, True
        return expected_result, False
