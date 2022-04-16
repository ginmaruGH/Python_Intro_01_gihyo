from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 2つの6面サイコロを作成する
die_1 =Die()
die_2 =Die()

# サイコロを転がし、結果をリストに格納する
results = [die_1.roll() + die_2.roll() for roll_num in range(5_000)]
# for roll_num in range(50_000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# 結果を分析する
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)

# 結果を可視化する
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '結果', 'dtick': 1}
y_axis_config = {'title': '発生した回数'}
plot_title = '２つの6面サイコロを50,000回転がした結果'
my_layout = Layout(
    title=plot_title,
    xaxis=x_axis_config, yaxis=y_axis_config
)
offline.plot(
    {'data': data, 'layout': my_layout},
    filename='jissen/project_02/chap_04/lti_4_9_dice_comprehension.html'
)
