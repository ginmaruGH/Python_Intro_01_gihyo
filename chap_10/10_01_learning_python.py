# 10-01.Pythonを学ぶ
# learning_python.txtを読み込む

print("\n10-01.Pythonを学ぶ\n")

filename = '/Users/takeru/Library/CloudStorage/OneDrive-個人用/Learn/Python/Python_Intro_01_gihyo/chap_10/learning_python.txt'

print("--- ファイル全体を読み込む: ")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- ファイルの各行をループ: ")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- 各行をリストに格納する: ")
with open(filename) as f:
    lines = f.readlines()

print(f"\n{lines}\n")
for line in lines:
    print(line.rstrip())
