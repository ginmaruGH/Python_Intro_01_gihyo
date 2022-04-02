## Chapter10 ファイルと例外
### ファイルを読み込む
#### 1行づつ読み込む

print("\n1行づつ読み込む\n")

# filename = 'pi_digits.txt'
filename = 'chap_10/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# 余分な空行を取り除く
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
