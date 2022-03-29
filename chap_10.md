# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

## Chapter10 ファイルと例外

### ファイルを読み込む

#### ファイル全体を読み込む

- pi_digits.txt
- file_reader.py

#### 1行づつ読み込む

- pi_digits.txt
- file_reader2.py

#### ファイルの行からリストを作成する

- pi_digits.txt
- file_reader3.py

#### ファイルの内容を操作する

- Pythonはテキストファイルを読み込む際、ファイル内のすべてのテキストを文字列型として解釈する。
- 読み込んだ数字を数値として扱いたい場合は、
  - `int()`関数を使って整数に変換する
  - `float()`関数を使って浮動小数点に変換する
- pi_digits.txt
- pi_string.py

#### 100万桁の巨大なファイル

- pi_million_digits.txt
- pi_string2.py

#### πの中に誕生日が含まれているか

- pi_million_digits.txt
- pi_string3.py

---

### ファイルに書き込む

#### 空のファイルを書き込む

- write_message.py
  - programing.txt
- `open(<filename>, 'r')`
  - read
- `open(<filename>, 'w')`
  - write
  - 書き込み先が存在しない場合、ファイルを自動的に作成する
  - 同名のファイルがある場合、既存のファイル内容を消去する
- `open(<filename>, 'a')`
- `open(<filename>, 'r+')`
  - append

- Pythonがテキストファイルに書き出せるのは、文字列のみ。
- 数値データをテキストファイルに保存するには、事前に`str()`関数を使ってデータを文字列型に変換する必要がある。

#### 複数行を書き込む


