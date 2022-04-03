# リストの一部を使用する
print("\nリストをスライスする\n")

players = ["charles", "martina", "michael", "florence", "eli"]
print("players")
print(players)
print("players[0:3]")
print(players[0:3])

print("players[1:4]")
print(players[1:4])

print("players[:4]")
print(players[:4])

print("players[2:]")
print(players[2:])

print("players[-3:]")
print(players[-3:])

# スライスによるループ
print("\nスライスによるループ\n")

players = ["charles", "martina", "michael", "florence", "eli"]
print(players)
print("チームの最初3人の選手です。")
for player in players[:3]:
    print(player.title())

