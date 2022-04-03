# 11-03.従業員

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """employeeモジュールをテストする"""

    def setUp(self):
        """テスト用の従業員を作成する"""
        self.tanji = Employee('tanjiro', 'kamado', 7_000_000)

    def test_give_default_raise(self):
        """デフォルト金額での昇給が正しく動作することを確認する"""
        self.tanji.give_raise()
        self.assertEqual(self.tanji.salary, 7_500_000)

    def test_give_custom_raise(self):
        """指定した金額での昇給が正しく動作することを確認する"""
        self.tanji.give_raise(1_000_000)
        self.assertEqual(self.tanji.salary, 8_000_000)

 
if __name__ == '__main__':
    unittest.main()
