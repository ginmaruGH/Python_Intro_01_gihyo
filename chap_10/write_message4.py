## Chapter10 ファイルと例外
### ファイルに書き込む
#### ファイルに追記する

print("\n#### ファイルに追記する\n")

filename = 'chap_10/programming4.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
