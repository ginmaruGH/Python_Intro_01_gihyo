# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

## Chapter09 クラス

### クラスを作成して使用する

#### イヌのクラスを作成する

- dog.py
- クラス名の先頭は大文字
- `__init__`メソッド
  - `self`はメソッド定義に必須の引数

#### クラスからインスタンスを生成する

- 属性にアクセスする
  - `my_dog.name`
- メソッドを呼び出す
  - `my_dog.site()`

---

### クラスとインスタンスを操作する

#### 自動車のクラス

- car.py

#### 属性にデフォルト値を設定する

- car2.py

#### 属性の値を変更する

- インスタンスを通して、属性の値を直接変更する
  - car3.py
- メソッドを通して、値を変更する
  - car4.py
- メソッドを通して、値を増加させる
  - car5.py

---

### 継承

#### 子クラスの`__init__()`メソッド

- electric_car.py

#### 子クラスに属性とメソッドを定義する

- electric_car2.py

#### 親クラスのメソッドをオーバーライドする

#### 属性としてインスタンスを使用する

- electric_car3.py

#### 現実世界のモノをモデル化する

---

### クラスをインポートする

#### 1つのクラスをインポートする

- class_car.py
- my_car.py

#### モジュールに複数のクラスを格納する

- class_car2.py
- my_electric_car.py

#### モジュールから複数のクラスをインポートする

- class_car2.py
- my_cars.py
- `from <module_name> import <ClassName_1>, <ClassName_2>`

#### モジュール全体をインポートする

- class_car2.py
- my_cars2.py
- `import <module_name>`
  - `module_name.ClassName()`
- プログラム内で使用されるモジュールの場所が明確になる
- 名前が衝突する可能性を避けられる

#### モジュールからすべてのクラスをインポートする

- `from <module_name> import *`
- モジュールのどのクラスを使用しているか不明瞭になる
- インポートしたクラスと同じ名前をプログラム内で誤って使用してしまう可能性がある
- 非推奨

#### モジュールの中にモジュールをインポートする

- class_electric_car.py
- my_cars3.py

#### 別名を使用する

- `from electric_car import ElectricCar as EC`
  - `my_tesla = EC('tesla', 'roadster', 2019)`

---

### Python標準ライブラリ

```python
from random import randint

randint(1, 6)
# 3
```

```python
from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
# 'florence'
```

[python 3 Module of the Week](https://pymotw.com/3/)

---

### クラスのスタイル

- クラス名
  - キャメルケース（CamelCase）
- インスタンス名とモジュール名
  - 小文字で単語間をアンダースコア（`_`）でつなぐ
  - スネークケース（snake_case）
- クラス定義の直下にdocstringを書く
- クラスについての簡潔な説明をdocstringに書く
- クラスのdocstringも関数のdocstringも同じフォーマットで書く
- モジュールのdocstringには、モジュール内のクラスの使用方法などを記述する
- クラス内の各メソッドの間は空行を1行取る
- モジュール内の各クラスの間は空行を2行取る
- 標準ライブラリのモジュールと、自作のモジュールをインポートする場合、
  - 最初に標準ライブラリをインポートする
  - 空行を1行取り、自作のモジュールをインポートする
