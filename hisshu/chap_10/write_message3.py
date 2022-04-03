## Chapter10 ファイルと例外
### ファイルに書き込む
#### 複数行を書き込む（改行あり）

print("\n#### 複数行を書き込む（改行あり）\n")

filename = 'chap_10/programming3.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
