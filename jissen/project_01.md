# Python Crash Course [Second Part]

最短距離でゼロからしっかり学ぶPython入門「実践編」

ゲーム開発・データ可視化・Web開発

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

## Project 1 エイリアン侵略ゲーム

### Chapter 01 弾を発射する宇宙船

- エイリアン侵略ゲームでプレイヤーは画面の下部中央に表示される宇宙船を操縦する
- プレイヤーは、[←][→]キーで宇宙船を左右に動かし、[Space]キーで弾を発射する
- ゲーム開始時にエイリアンの艦隊が空を埋め、画面を横断しながら下降してくる
- プレイヤーは、エイリアンを撃って破壊する
- プレイヤーがすべてのエイリアンを撃ち落とした場合、新しい艦隊が現れて直前の艦隊よりも素早く移動する
- エイリアンがプレイヤーの宇宙船に衝突するか画面の一番下に到達すると、プライヤーは宇宙船を1機失う
- プレイヤーが宇宙船を3機失うとゲームは終了する

#### Pygameをインストールする

```bash
python3 -m pip install --user pygame

Collecting pygame
  Downloading pygame-2.1.2-cp39-cp39-macosx_10_9_x86_64.whl (8.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 10.5 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.1.2
```

#### ゲームのプロジェクトを開始する

- alien_invasion.py

##### 背景色を設定する

##### Settingsクラスを作成する

- settings.py

---

#### 宇宙船の画像を追加する

- [Pixabay](https://pixabay.com/)

##### Shipクラスを作成する

- ship.py

##### 宇宙船を描画する

- alien_invasion.py

---

#### リファクタリング：_check_events()と_update_screen()メソッド

##### _check_events()メソッド

- alien_invasion.py

##### _update_screen()メソッド

- alien_invasion.py

---

&nbsp;

### Chapter 02 エイリアン！

---

&nbsp;

### Chapter 03 得点を表示する

---

&nbsp;
