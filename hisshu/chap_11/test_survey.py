## コードをテストする
### クラスをテストする
#### AnonymousSurveyクラスをテストする

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """AnonymousSurveyクラスのテスト"""

    def test_store_single_response(self):
        """1件の回答が正しく保存されているかをテストする"""
        question = "最初に勉強した言語は何ですか？"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('英語')
        self.assertIn('英語', my_survey.responses)

    def test_store_three_responses(self):
        """3件の異なる回答が正しく保存されているかをテストする"""
        question = "最初に勉強した言語は何ですか？"
        my_survey = AnonymousSurvey(question)
        responses = ['英語', 'スペイン語', '中国語']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
