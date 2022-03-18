# Chapter.07 ユーザー入力とwhileループ
# ## breakを使用してループを終了する
print("\n## breakを使用してループを終了する\n")

prompt = "\n行ったことのある街を教えて下さい。>> "
prompt += "\n（終わったら '終了' と入力してください。）"

while True:
    city = input(prompt)

    if city == '終了':
        break
    else:
        print(f"{city.title()}に行くのって最高です！")
