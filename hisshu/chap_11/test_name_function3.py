## Chapter11 コードをテストする
### 関数をテストする
#### テストに成功する

import unittest
from name_function3 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """name_function.pyをテストする"""

    def test_first_last_name(self):
        """'Janis Joplin'のような名前で動作するか？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
