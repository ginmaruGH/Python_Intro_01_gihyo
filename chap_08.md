# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

## Chapter08 関数

### 関数を定義する

- greeter.py

#### 関数に情報を渡す

- ドックストリング（docstring）
  - 関数の動作に関する説明を記述する
  - `"""docstring"""`

- greeter2.py

#### 実引数と仮引数

- 仮引数（parameter）
  - 関数が作業を実行するために必要な情報
  - `def greet_user(<parameter>)`
- 実引数（argument）
  - 関数呼び出し元から関数に渡される情報のこと
  - `greet_user(<argument>)`

---

### 実引数を渡す

#### 位置引数

- 位置引数
  - 関数呼び出し時に指定された実引数の順番を、関数定義時の仮引数の順番に対応付けること
- pets.py

#### キーワード引数

- キーワード引数
  - 名前と値のペアを関数に渡す
  - 実引数で名前と値を直接関連付けて指定する
  - 関数呼び出し時に実引数の順番を気にする必要がなくなる
- pets2.py

#### デフォルト値

- デフォルト値
  - 関数を定義する際、各仮引数にデフォルト値を定義できる
  - デフォルト値を持たいない仮引数の後ろに記述する
- pets3.py

#### 関数を同じように呼び出す

- pets4.py

#### 実引数のエラーを回避する

---

### 戻り値

- 戻り値（返り値）
  - 関数が返す値

#### 単純な値を返す

- formatted_name.py

#### オプション引数を作成する

- formatted_name2.py

#### 辞書を返す

- person.py

#### whileループで関数を使用する


