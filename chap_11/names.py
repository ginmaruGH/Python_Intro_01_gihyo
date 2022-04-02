## Chapter11 コードをテストする
### 関数をテストする
####

print("\n### 関数をテストする\n")

from name_function import get_formatted_name

print("'q'を入力すると終了します。")
while True:
    first = input("\n名を入力してください。")
    if first == 'q':
        break
    last = input("\n姓を入力してください。")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tフォーマットされた名前は: {formatted_name}.")
