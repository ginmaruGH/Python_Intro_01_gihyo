# Chap.06 Dictionary
print("\nシンプルな辞書\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

# 新しいキーと値のペアを追加する
print("\n新しいキーと値のペアを追加する")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 空の辞書から開始する
print("\n空の辞書から開始する")
alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 辞書の値を変更する
print("\n辞書の値を変更する")
alien_0 = {'color': 'green'}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

# 辞書の使い方
print("\n# 辞書の使い方\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"最初のX座標: {alien_0['x_position']}")

# エイリアンは右に移動します。
# 現在のスピードによってエイリアンの移動距離を決定する
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 素早いエイリアン
    x_increment = 3

# 新しい位置は元の位置に移動距離を加算する
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"新しいX座標: {alien_0['x_position']}")


# キーと値のペアを削除する
print("\n# キーと値のペアを削除する\n")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
