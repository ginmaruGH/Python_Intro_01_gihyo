# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)


---

## Chapter06 辞書

- `keys()`は省略できる（オススメ）
  - `for name in favorite_languages.keys():`
  - `for name in favorite_languages:`
  - 上記2つは同じ結果になる
- 集合`set()`
  - 同じ要素を含んでいるリストを`set()`で囲むと、リスト内のいち一意の要素だけで、集合を作成する
    - `set(favorite_languages.values())`
  - 集合を直接作成する
    - `languages = {'python', 'ruby', 'python', 'c'}`
  - 集合は要素の順序を保持しない

