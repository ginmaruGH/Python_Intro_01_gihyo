# 11-03.従業員

class Employee():
    """従業員を表すクラス"""

    def __init__(self, f_name, l_name, salary):
        """従業員を初期化する"""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=500000):
        """従業員の給与を増やす"""
        self.salary += amount
