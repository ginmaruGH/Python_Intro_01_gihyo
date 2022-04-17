import requests

from plotly.graph_objs import Bar
from plotly import offline

# API呼び出しを作成して、そのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

# 結果を処理する
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可視化を実行する
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'GitHubで最も多くのスターがついているPythonプロジェクト',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'リポジトリ',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'スターの数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(
    fig,
    filename='jissen/project_02/chap_06/python_repos.html'
)
