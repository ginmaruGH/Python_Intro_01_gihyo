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

- greeter3.py

---

### リストを受け渡す

- greet_users.py

#### 関数の中でリストを変更する

- printing_models.py

#### 関数によるリストの変更を防ぐ

- 関数にリストのコピーを渡す
  - `function_name(list_name[:])`

---

### 任意の数の引数を渡す

- `def make_pizza(*toppings):`
  - 仮引数`*toppings`は、受け取った値を`toppings`というタプルにまとめて格納する
- pizza.py
- pizza2.py

#### 位置引数と可変長引数を同時に使う

- 任意の数の実引数を受け取る仮引数（可変長引数）は、関数定義の最後に書く
- 可変長引数をまとめるための一般的な仮引数名として、`*args`が使われる
- pizza3.py

#### 可変長キーワード引数を使用する

- 可変長キーワード引数をまとめるための一般的な仮引数名として、`**kwargs`がよく使われる
- user_profile.py

---

### 関数をモジュールに格納する

#### モジュール全体をインポートする

- pizza4.py
- making_pizzas.py
- `import <module_name>`
  - `<module_name>.<function_name>()`

#### 特定の関数をインポートする

- `from <module_name> import <function_name>`
  - `<function_name>()`
- `from <module_name> import <function_0>, <function_1>, <function_2>`
  - `<function_0>()`
  - `<function_1>()`
  - `<function_2>()`

#### asを使用して関数に別名を付ける（asキーワード）

- `from <module_name> import <function_name> as fn`
  - `fn()`

#### asを使用してモジュールに別名を付ける

- `import <module_name> as mn`
  - `mn.<function_name>()`

#### モジュールの全関数をインポートする

- `from <module_name> import *`
  - `<function_name>()`

- Pythonは、同じ名前の関数や変数を見つけた場合、すべての関数を別々にインポートせずに上書きする
- 必要な関数だけインポートするか、モジュール全体をインポートしてドット（`.`）を使って関数を呼び出すのが最良の方法

---

### 関数のスタイル

- 関数にはわかりやすい名前を付ける
- 名前にはアルファベットの小文字とアンダースコア（`_`）だけを使う
- モジュール名も同じ
- すべての関数には、その関数が何を実行するかを完結に説明するコメントを書く
  - docstring形式で書く
  - 関数名、必要な引数、戻り値の種類
- 仮引数にデフォルト値を指定する場合、等号（`=`）の左右にスペースを入れない
  - `def <function_name>(parameter_0, parameter_1='default_value')`
    - `<function_name>(value_0, parameter_1='value_1')`
- プログラムやモジュールに2つ以上の関数がある場合は、関数の間に2行の空行を入れる
- すべてのimport文はファイルの先頭に記述する
