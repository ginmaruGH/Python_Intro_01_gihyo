# 6-06.Polling
print("\n投票\n")

# 投票する必要がある人のリスト
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

# 投票してくれた人の辞書
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for coder in coders:
    if coder in favorite_languages.keys():
        print(f"{coder.title()}、投票ありがとう。")
    else:
        print(f"{coder.title()}、好きなプログラミング言語はなんですか？")

