import requests
import json

# API呼び出しを作成して、そのレスポンスを格納する
# url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
url = 'https://hacker-news.firebaseio.com/v0/item/31062465.json'
# url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

# データの構造を調べる
response_dict = r.json()
# readable_file = 'jissen/project_02/chap_06/readable_hn_data.json'
readable_file = 'jissen/project_02/chap_06/readable_hn_data_31062465.json'
# readable_file = 'jissen/project_02/chap_06/hn_topstories.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
