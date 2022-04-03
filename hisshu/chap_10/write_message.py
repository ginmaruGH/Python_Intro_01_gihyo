## Chapter10 ファイルと例外
### ファイルに書き込む
#### 空のファイルを書き込む

print("\n#### 空のファイルを書き込む\n")

filename = 'chap_10/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
