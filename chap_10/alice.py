## Chapter10 ファイルと例外
### 例外
#### FileNotFoundErrorを例外処理する

print("\n#### FileNotFoundErrorを例外処理する\n")

filename = 'chap_10/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"ごめんなさい。{filename}は見当たりません。")
