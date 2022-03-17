# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Original GitHub](https://ehmatthes.github.io/pcc_2e/)

<https://github.com/ehmatthes/pcc_2e/>

---

## Chapter02 変数とシンプルなデータ型

### 文字列

- `name.title()`
  - 先頭の文字を大文字にする
- `name.upper()`
  - すべての文字を大文字にする
- `name.lower()`
  - すべての文字を小文字にする

ユーザーから入力された情報を保存する前に、すべて小文字変換する場合がある。

- 空白文字の削除
  - `name.strip()`
  - `name.rstrip()`
  - `name.lstrip()`

ユーザーが入力した文字列をプログラムに保存する前処理としてよく使われる

---

### 数値

- 大きな数値を読みやすくできる
  - `50_000_000_000`
- 複数同時の代入
  - `x, y, z = 0, 0, 0`
- 定数
  - `MAX_CONNECTIONS = 5000`

```bash
# The Zen of Python
python3

>>>import this

# Beautiful is better than ugly.
# 汚いよりきれいなほうがいい

# Explicit is better than implicit.

# Simple is better than complex.
# 複雑より簡単な方がいい

# Complex is better than complicated.
# 込み入っているよりは複雑な方がいい

# Flat is better than nested.

# Sparse is better than dense.

# Readability counts.
# 読みやすいことに勝ちがある

# Special cases aren't special enough to break the rules.

# Although practicality beats purity.

# Errors should never pass silently.

# Unless explicitly silenced.

# In the face of ambiguity, refuse the temptation to guess.

# There should be one-- and preferably only one --obvious way to do it.
# たった一つの最良のやり方があるはずだ

# Although that way may not be obvious at first unless you're Dutch.

# Now is better than never.
# やらないより今やるほうがいい

# Although never is often better than *right* now.

# If the implementation is hard to explain, it's a bad idea.

# If the implementation is easy to explain, it may be a good idea.

# Namespaces are one honking great idea -- let's do more of those!


```

- [The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)
- [The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

&nbsp;

---

autopep8

```bash
/usr/local/bin/python3 -m pip install -U autopep8
```

```bash
# DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
# Collecting autopep8
#   Downloading autopep8-1.6.0-py2.py3-none-any.whl (45 kB)
#      |████████████████████████████████| 45 kB 4.3 MB/s
# Requirement already satisfied: toml in /Users/takeru/Library/Python/3.9/lib/python/site-packages (from autopep8) (0.10.2)
# Collecting pycodestyle>=2.8.0
#   Downloading pycodestyle-2.8.0-py2.py3-none-any.whl (42 kB)
#      |████████████████████████████████| 42 kB 3.0 MB/s
# Installing collected packages: pycodestyle, autopep8
#   DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
# DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
# Successfully installed autopep8-1.6.0 pycodestyle-2.8.0
# WARNING: You are using pip version 21.3.1; however, version 22.0.3 is available.
# You should consider upgrading via the '/usr/local/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip' command.
```

- 設定画面>>python.formatting.autopep8Path>>検索
  - Python > Formatting: Autopep8 Path項目 >> autopep8 に設定
- 設定画面>>python.formatting.provider>>検索
  - Python > Formatting: Provider項目 >> autopep8 を選択設定
- 設定画面>>python.formatting.autopep8Argsを検索>>
  - Python > Formatting: Autopep8 Args項目 >> 設定を追加
