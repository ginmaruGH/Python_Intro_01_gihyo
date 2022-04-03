## Chapter10 ファイルと例外
### 例外
#### テキストを分析する

print("\n#### テキストを分析する\n")

filename = 'chap_10/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"ごめんなさい。{filename}は見当たりません。")
else:
    # ファイル内のだいたいの単語の数を数える
    words = contents.split()
    num_words = len(words)
    print(f"ファイル{filename} には、約{num_words}の単語が含まれます。")
