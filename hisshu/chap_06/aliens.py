# 入れ子
print("\n入れ子\n")

# ## 複数の辞書によるリスト
print("\n## 複数の辞書によるリスト\n")

# エイリアン艦隊の作成1
print("\nエイリアン艦隊の作成1")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

for alien in aliens:
    print(alien)

# エイリアン艦隊の作成2
print("\nエイリアン艦隊の作成2")
aliens = []
# 30匹のエイリアンを生成する
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 最初の5匹のエイリアンの情報を出力する
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"全エイリアンの数: {len(aliens)}")

# エイリアン艦隊の作成3
print("\nエイリアン艦隊の作成3")
aliens = []
# 30匹のエイリアンを生成する
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 最初の3匹の緑色エイリアンを黄色に変更する
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 最初の5匹のエイリアンの情報を出力する
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"全エイリアンの数: {len(aliens)}")
