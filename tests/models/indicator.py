class Indicator:
    def __init__(self):
        self.money = 0

    def increase(self, number):
        self.money = self.money + number

    def get_money(self):
        return self.money

    def set_house(self, n):
        return n

    def merged_houses(self, n, x):
        return n * x

    def combo_merged_houses(self, houses):
        previous = houses[0]
        sum_ = 0
        for i in range(1, len(houses)):
            count = houses[i].get('count')
            lvl = houses[i].get('lvl')
            sum_first = lvl * count
            sum_second = previous.get('count') * previous.get('lvl')
            res = sum_first + sum_second
            sum_ = sum_ + res
            previous = houses[i]
        return sum_ * 2


    def used_crystal(self, n):
        return n + 1

    def destroyed_house(self, n):
        return n * 20

