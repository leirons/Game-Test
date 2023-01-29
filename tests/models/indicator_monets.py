class Indicator:
    def __init__(self):
        self.money = 0

    def increase(self, number):
        self.money = self.money + number

    def get_money(self):
        return self.money
