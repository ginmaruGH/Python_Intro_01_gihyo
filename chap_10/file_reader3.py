## Chapter10 ファイルと例外
### ファイルを読み込む
#### ファイルの行からリストを作成する

print("\nファイルの行からリストを作成する\n")

# filename = 'pi_digits.txt'
filename = 'chap_10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())

