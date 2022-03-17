# 似たようなオブジェクトを格納した辞書
print("\n# 似たようなオブジェクトを格納した辞書\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarahの好きなプログラミング言語は{language}です。")

# for文 items()
print("\n# for文 items()")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}の好きなプログラミング言語は、{language.title()}です。")

# すべてのキーをループする keys()
print("\n# すべてのキーをループする keys()")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# keys()は省略できる
print("\n# keys()は省略できる")
for name in favorite_languages:
    print(name.title())

# 任意のキーからの抽出
print("\n# 任意のキーからの抽出")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}、あなたの好きなプログラミング言語は、{language}ですね。")

# 任意のキーの有無を確認する
print("\n# 任意のキーの有無を確認する")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin、投票してください。")

# 辞書のキーを特定の順番でループする
print("\n# 辞書のキーを特定の順番でループする")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}、投票ありがとう。")

# 辞書のすべての値をループする values()
print("\n# 辞書のすべての値をループする values()")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("以下の言語が投票されました。")
for language in favorite_languages.values():
    print(language.title())

# 重複しない抽出 集合（set()）
print("\n# 重複しない抽出（set()）")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("以下の言語が投票されました。")
for language in set(favorite_languages.values()):
    print(language.title())


# 辞書の値にリストを入れる
print("\n辞書の値にリストを入れる")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarh': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}の好きな言語は、{languages[0]}ですね。")
    else:
        print(f"\n{name.title()}の好きな言語")
        for language in languages:
            print(f"\t{language.title()}")
