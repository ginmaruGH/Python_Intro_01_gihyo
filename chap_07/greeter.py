# Chapter.07 ユーザー入力とwhileループ
# ## わかりやすい入力プロンプトを書く
print("\n## わかりやすい入力プロンプトを書く\n")

name = input("名前を入力してください。 >> ")
print(f"こんにちは、{name}!")

# ### 2行以上の入力プロンプト
print("\n### 2行以上の入力プロンプト\n")
prompt = "あなたが誰か教えてくれたら、あなた向けのあいさつをします。"
prompt += "\nあなたの名前は？ >> "
name = input(prompt)
print(f"\nこんにちは、{name}!")
