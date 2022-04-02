## Chapter10 ファイルと例外
### 例外
#### 複数のファイルを扱う

print("\n#### 複数のファイルを扱う\n")

def count_words(filename):
    """ファイルに含まれるだいたいの単語の数を数える。"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"ごめんなさい。{filename} は、見当たりません。")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"ファイル{filename} には、約{num_words}の単語が含まれます。")

filenames= [
    'chap_10/alice.txt',
    'chap_10/siddahrtha.txt',
    'chap_10/little_women.txt',
    'chap_10/moby_dick.txt',
]
for filename in filenames:
    count_words(filename)
