# 10-04.ゲストブック
# 10_04_guest_book.txtを出力

print("\n10-04.ゲストブック\n")

filename = 'chap_10/10_04_guest_book.txt'

print("終了するには、'終了' と入力してください。")
while True:
    name = input("\nお名前は？ >> ")
    if name == '終了':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"こんにちは、{name}さん。あなたはゲストブックに追加されました。")
