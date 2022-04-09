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

### プロジェクトをレビューする

- コードを調べ、新しい機能を実装する前にリファクタリングが必要かを判断する
- 画面の左上の角に適切な余白を付けて1匹のエイリアンを配置する
- 最初のエイリアンの余白を使用して、画面サイズから適切なエイリアンの数を決定する
  - 画面上部をエイリアンで埋めるループ処理を記述する
- エイリアンの艦隊が全滅するか、エイリアンが宇宙船に衝突するか、エイリアンが画面の一番下に到達するまで、艦隊を横と下に移動する。
  - 全艦隊が撃ち落とされた場合は、新しい艦隊を作成する
  - エイリアンが宇宙船に衝突するか、画面の一番下に到達した場合は、宇宙船を破壊して新しい艦隊を作成する
- プレイヤーが使用できる宇宙船の数を制限し、プレイヤーが割り当てられた宇宙船をすべて使い切ったら、ゲームを終了する

---

### 最初のエイリアンを生成する

#### Alienクラスを作成する

#### Alienのインスタンスを生成する

---

### エイリアンの艦隊を編成する

#### 1列に収まるエイリアンの数を決定する

#### 1列のエイリアンを作成する

- `available_space_x = settings.screen_width - ( 2 * alien_width)`
- `number_aliens_x = available_space_x // (2 * alien_width)`

#### _create_fleet()をリファクタリングする

#### 複数の列を追加する

- `available_space_y = settings.screen_height - (3 * alien_height) - ship_height`
- `number_rows = available_space_y // (2 * alien_height)`

---

### 艦隊を動かす

#### エイリアンを右に移動する

#### 艦隊の移動する方向の設定を追加する

#### エイリアンがどちらかの端に到達したかを確認する

#### 艦隊を下に移動して進行方向を変える

---

### エイリアンを撃つ

#### 弾が衝突したことを検出する

- `sprite.groupcollide()`メソッド

#### テスト用に大きな弾を作成する

#### 艦隊を再度出現させる

#### 弾のスピードを上げる

#### _update_bullets()をリファクタリングする

---

### ゲームを終了する

#### エイリアンと宇宙船の衝突を検出する

#### エイリアンと宇宙船の衝突に対応する

#### エイリアンが画面の一番下に到達する

#### ゲームオーバー！

#### ゲームの状態によって実行される箇所を明確にする

---

&nbsp;

## Chapter03 得点を表示する

---

&nbsp;
