# 7-5.映画のチケット
print("\n# 7-5.映画のチケット\n")

prompt = "\n何歳ですか？"
prompt += "\n終わったら、'終了'と入力してください。>> "

while True:
    age = input(prompt)
    if age == '終了':
        break

    age = int(age)
    if age < 3:
        print(" チケット料金は無料です。")
    elif age < 13:
        print(" チケット料金は1,000円です。")
    else:
        print(" チケット料金は1,500円です。")


