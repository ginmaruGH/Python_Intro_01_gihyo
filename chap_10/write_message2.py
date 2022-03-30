## Chapter10 ファイルと例外
### ファイルに書き込む
#### 複数行を書き込む（改行なし）

print("\n#### 複数行を書き込む（改行なし）\n")

filename = 'chap_10/programming2.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
