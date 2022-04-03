# 7-4.ピザのトッピング
print("\n# 7-4.ピザのトッピング\n")

prompt = "\n何をピザのトッピングにしますか？"
prompt += "\n終わったら、'終了'を入力してください。>>"

while True:
    topping = input(prompt)
    if topping != '終了':
        print(f" あなたのピザに{topping}をトッピングします。")
    else:
        break
