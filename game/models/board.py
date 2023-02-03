from game.models.house import Houses


class Board:
    def __init__(self):
        self.board = []
        self.houses = Houses()

    def get_board(self):
        return self.board

    def merge_houses(self, houses, expected_result):
        if houses:
            self.board = expected_result
            return None, True
        return expected_result, False
