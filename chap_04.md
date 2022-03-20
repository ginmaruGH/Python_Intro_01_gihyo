# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Original GitHub](https://ehmatthes.github.io/pcc_2e/)

<https://github.com/ehmatthes/pcc_2e/>

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)
[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

## Chapter04 リストを操作する

- スライス（slice）
  - リスト内の特定の要素のグループに対して処理を行う
  - `list_name[0:3]`
  - `list_name[<インデックス番号以上>:<インデックス番号未満>]`
- タプル（tuple）
  - 変更できない値をイミュータブル（immutable）をいい、イミュータブルなリストをタプルと呼ぶ
  - 再代入はできない（再定義可能）
  - プログラム全体で変更すべきでないデータの集まりを保存する
  - `dimensions = (200, 50)`
  - `my_t = (3,)`
- PEP（Python Enhancement Proposal）
  - PEP8
    - コードは80文字未満
    - コメントは72文字以内
    - <https://legacy.python.org/dev/peps/pep-0008/>
    - <https://pep8-ja.readthedocs.io/ja/latest/>
