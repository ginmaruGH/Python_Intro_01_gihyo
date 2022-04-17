import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# データの構造を調査する
filename = 'jissen/project_02/chap_05/data2/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

# タイトルとfeatures情報を取得
title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

# マグニチュード、位置データをを取り出す
# 経度（longitude）、経度（latitude）
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# 地震の地図
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'マグニチュード'},
    },
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(
    fig,
    filename='jissen/project_02/chap_05/lti_5_7_global_earthquakes.html'
)
