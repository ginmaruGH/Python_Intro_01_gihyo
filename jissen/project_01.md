Python Crash Course - Second Part -

最短距離でゼロからしっかり学ぶPython入門「実践編」

ゲーム開発・データ可視化・Web開発

---

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

# Project 1 エイリアン侵略ゲーム

## Chapter01 弾を発射する宇宙船

### プロジェクトの計画を立てる

- エイリアン侵略ゲームでプレイヤーは画面の下部中央に表示される宇宙船を操縦する
- プレイヤーは、[←][→]キーで宇宙船を左右に動かし、[Space]キーで弾を発射する
- ゲーム開始時にエイリアンの艦隊が空を埋め、画面を横断しながら下降してくる
- プレイヤーは、エイリアンを撃って破壊する
- プレイヤーがすべてのエイリアンを撃ち落とした場合、新しい艦隊が現れて直前の艦隊よりも素早く移動する
- エイリアンがプレイヤーの宇宙船に衝突するか画面の一番下に到達すると、プライヤーは宇宙船を1機失う
- プレイヤーが宇宙船を3機失うとゲームは終了する

### Pygameをインストールする

```bash
python3 -m pip install --user pygame

Collecting pygame
  Downloading pygame-2.1.2-cp39-cp39-macosx_10_9_x86_64.whl (8.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 10.5 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.1.2
```

### ゲームのプロジェクトを開始する

- alien_invasion.py

#### 背景色を設定する

#### Settingsクラスを作成する

- settings.py

---

### 宇宙船の画像を追加する

- [Pixabay](https://pixabay.com/)

#### Shipクラスを作成する

- ship.py

#### 宇宙船を描画する

- alien_invasion.py

---

### リファクタリング：_check_events()と_update_screen()メソッド

- ヘルパーメソッド
  - クラスの内部で動作するもの
  - インスタンス経由で呼び出すことは意図していない
  - 名前の先頭にアンダースコア（`_`）を付ける
    - `_helper_method()`

#### _check_events()メソッド

- alien_invasion.py

#### _update_screen()メソッド

- alien_invasion.py

---

### 宇宙船を操縦する

#### キー入力に反応する

- alien-invasion.py

#### 連続した移動に対応する

- ship.py
- alien-invasion.py

#### 左右に移動する

#### 宇宙船のスピードを調整する

#### 宇宙船の移動範囲を制限する

#### _check_events()をリファクタリングする

#### Qを押したら終了する

#### ゲームをフルスクリーンモードで実行する

---

### 振り返り

#### alien_invasion.py

#### settings.py

#### ship.py

---

### 弾を発射する

#### 弾の設定を追加する

#### Bulletクラスを作成する

#### 複数の弾をグループに格納する

#### 弾を発射する

#### 古い弾を削除する

#### 玉の数を制限する

#### _update_bullets()メソッドを作成する

---

### まとめ

- ゲームを作成する計画を立て方
- Pygameでゲームを作成するときの基本的な構造
- 背景色の設定方法
- ゲームで使用する各種の設定値を別のクラスに格納し、より簡単に設定値を調整する方法
- 画像を画面に描画する方法
  - プレイヤーの操作によってゲーム中の要素を動かすこと
- 画面の上に向かう弾など複数の要素を生成して動かすこと
  - 不要になったオブジェクトと削除する方法
- 開発を進行しやすくするために、定期的にプロジェクトのコードをリファクタリングすること

---

&nbsp;

## Chapter02 エイリアン！

---

&nbsp;

## Chapter03 得点を表示する

---

&nbsp;
