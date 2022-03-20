# Chapter.07 ユーザー入力とwhileループ
# ## リストから特定の値をすべて削除する
print("\n## リストから特定の値をすべて削除する\n")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
