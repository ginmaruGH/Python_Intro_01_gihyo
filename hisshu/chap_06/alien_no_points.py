# get()を使用して値にアクセスする
print("\n# get()を使用して値にアクセスする\n")

alien_0 ={'color': 'green', 'speed': 'slow'}
# alien_0['points']    # KeyError
point_value = alien_0.get('points', '点数は設定されていません。')
print(point_value)
