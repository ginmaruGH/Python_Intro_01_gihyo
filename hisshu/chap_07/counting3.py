# Chapter.07 ユーザー入力とwhileループ
# ## 無限ループを回避する
print("\n## 無限ループを回避する\n")

x = 1
while x <= 5:
    print(x)
    x += 1

# 以下は、無限ループ
# 終了は、`Ctrl` + `c`
# x = 1
# while x <= 5:
#     print(x)
