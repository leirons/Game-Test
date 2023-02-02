class Pause:
    def __init__(self):
        self.active_pause = True
        self.elements = ["tooltip", "amount_of_money", "record_amount_of_money"]

    def continue_game(self):
        self.active_pause = True

    def stop_game(self):
        self.active_pause = False
