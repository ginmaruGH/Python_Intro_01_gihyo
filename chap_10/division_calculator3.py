## Chapter10 ファイルと例外
### 例外
#### elseブロック

print("\n#### elseブロック\n")

print("数字を2つ教えてください。割り算をします。")
print("終了するには、'q' を入力してください。")

while True:
    first_number = input("\n1番目の数字 >> ")
    if first_number == 'q':
        break
    second_number = input("2番めの数字 >> ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("ゼロで割ることはできません。")
    else:
        print(answer)

