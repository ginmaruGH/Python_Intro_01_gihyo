"""
作者によるこの解答例についての注記
訳注 : はじめに python_repos.py の作者による注記をご覧ください。
ここでは、ステータスコード200のレスポンスが取得できることをテストします。
また、各リポジトリの辞書に存在するはずのいくつかのキーが
最初のリポジトリの辞書に含まれることをテストします。
( https://ehmatthes.github.io/pcc_2e/solutions/chapter_17/#17-3-testing-python_repospy
に記載の文章を翻訳して掲載しました)
訳注 : 実際は python_repos_visual.py が対象のようです。
"""

import unittest

import lti_6_3_python_repos as pr

class PythonReposTestCase(unittest.TestCase):
    """lti_6_3_python_repos.pyに対するテスト"""

    def setUp(self):
        """すべての関数を呼び出し、別々に要素をテストする。"""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = pr.get_project_data(self.repo_dicts)

    def test_get_response(self):
        """正しいレスポンスが取得できていることをテスト"""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """想定通りのデータが取得できていることをテスト"""
        # 30レポジトリ分の辞書が取得される
        self.assertEqual(len(self.repo_dicts), 30)

        # リポジトリには必要なキーが存在する
        required_keys = [
            'name', 'owner', 'stargazers_count', 'html_url'
        ]
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()
