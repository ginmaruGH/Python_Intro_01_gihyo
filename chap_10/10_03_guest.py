# 10-03.ゲスト
# 10_03_guest.txtを出力

print("\n# 10-03.ゲスト\n")

filename = 'chap_10/10_03_guest.txt'

name = input("お名前は？ >> ")

with open(filename, 'w') as f:
    f.write(name)
