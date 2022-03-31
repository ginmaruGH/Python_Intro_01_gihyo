## Chapter10 ファイルと例外
### 例外
#### クラッシュ回避のために例外を使用する

print("\n#### クラッシュ回避のために例外を使用する\n")

print("数字を2つ教えてください。割り算をします。")
print("終了するには、'q' を入力してください。")

while True:
    first_number = input("\n1番目の数字 >> ")
    if first_number == 'q':
        break
    second_number = input("2番めの数字 >> ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

