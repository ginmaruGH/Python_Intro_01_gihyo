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

# Project02 データの可視化

## Chap.04 データを生成する

### Matplotlibをインストールする

```bash
python3 -m pip install --user matplotlib
```

```bash
Collecting matplotlib
  Downloading matplotlib-3.5.1-cp39-cp39-macosx_10_9_x86_64.whl (7.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 10.6 MB/s eta 0:00:00
Collecting cycler>=0.10
  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.32.0-py3-none-any.whl (900 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 900.8/900.8 KB 8.1 MB/s eta 0:00:00
Collecting pyparsing>=2.2.1
  Downloading pyparsing-3.0.8-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.5/98.5 KB 3.0 MB/s eta 0:00:00
Collecting numpy>=1.17
  Downloading numpy-1.22.3-cp39-cp39-macosx_10_14_x86_64.whl (17.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.6/17.6 MB 10.5 MB/s eta 0:00:00
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.4.2-cp39-cp39-macosx_10_9_x86_64.whl (65 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.3/65.3 KB 2.3 MB/s eta 0:00:00
Collecting pillow>=6.2.0
  Downloading Pillow-9.1.0-cp39-cp39-macosx_10_9_x86_64.whl (3.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 10.1 MB/s eta 0:00:00
Collecting python-dateutil>=2.7
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 KB 5.6 MB/s eta 0:00:00
Collecting packaging>=20.0
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.8/40.8 KB 1.2 MB/s eta 0:00:00
Collecting six>=1.5
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, pillow, numpy, kiwisolver, fonttools, cycler, python-dateutil, packaging, matplotlib
  WARNING: The scripts f2py, f2py3 and f2py3.9 are installed in '/Users/takeru/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts fonttools, pyftmerge, pyftsubset and ttx are installed in '/Users/takeru/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed cycler-0.11.0 fonttools-4.32.0 kiwisolver-1.4.2 matplotlib-3.5.1 numpy-1.22.3 packaging-21.3 pillow-9.1.0 pyparsing-3.0.8 python-dateutil-2.8.2 six-1.16.0
```

[Matplotlib sample gallery](https://matplotlib.org/stable/gallery/index.html)

### 簡単な折れ線グラフを描画する

- ラベルと線の太さを変更する
- グラフを修正する
- 組み込みのスタイルを使用する

```bash
python3
>>> import matplotlib.pyplot as plt
>>> plt.style.available
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
>>> exit()
```

- scatter()で複数の点にスタイルを指定して描画する
- scatter()で連続した点を描画する
- データを自動的に計算する
- 色をカスタマイズする
- カラーマップを使用する
  - [matplotlib](https://matplotlib.org/)
  - [Colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html?highlight=colormap%20reference)
- グラフを自動的に保存する

### ランダムウォーク

- `RandomWalk()`クラスを作成する
- 方向を選択する
- ランダムウォークを描画する
- 複数のランダムウォークを生成する
  - 点に色を付ける
  - 開始点と終了点を描画する
  - 軸を取り除く描画する点を追加する
  - 画面を塗りつぶすためのサイズを変更する
- ランダムウォークにスタイルを設定する

### Plotlyでサイコロを転がす

- Plotlyをインストールする

```bash
python3 -m pip install --user plotly
```

```bash
Collecting plotly
  Downloading plotly-5.7.0-py2.py3-none-any.whl (28.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 28.8/28.8 MB 5.5 MB/s eta 0:00:00
Collecting tenacity>=6.2.0
  Downloading tenacity-8.0.1-py3-none-any.whl (24 kB)
Requirement already satisfied: six in /Users/takeru/Library/Python/3.9/lib/python/site-packages (from plotly) (1.16.0)
Installing collected packages: tenacity, plotly
Successfully installed plotly-5.7.0 tenacity-8.0.1
```

[Plotly](https://plot.ly/python/)

- Dieクラスを作成する
- サイコロを転がす
- 結果を分析する
- ヒストグラムを作成する
- 2個のサイコロを転がす
- 異なるサイズのサイコロを転がす

### まとめ

- データセットを生成し、そのデータを可視化する方法
- Matplotlibを使用して簡単なグラフを作成する方法と、散布図を使用してランダムウォークを調査する方法
- Plotlyを使用してヒストグラムを作成する方法と、異なるサイズのサイコロを転がした結果をヒストグラムで調べる方法

---

&nbsp;

## Chap.05 データをダウンロードする

### CSVファイル形式

[NOAA](https://ncdc.noaa.gov/cdo-web/)

- CSVファイルのヘッダーを解析する
  - csv.reader()
  - next()関数
- ヘッダーとその位置を出力する
  - enumerate()関数
    - リストをループするときに各要素のインデックスと値を返す
- データを抽出して読み込む
- 気温のグラフにデータを描画する
- datetimeモジュール
- 日付を描画する
- 長い時間の範囲を描画する
- 2番めのデータを描画する
- グラフ内の領域に陰影を付ける
- エラーをチェックする
- データをダウンロードする

### 地球全体のデータセットを地図に描画する（JSON形式）

- 地震データをダウンロードする
  - [United States Geological Survey](https://earthquake.usgs.gov/earthquakes/feed/)
- JSONデータを調査する
  - （経度・緯度）>（x, y）
- すべての地震データのリストを作成する
- マグニチュードを取り出す
- 位置データを取り出す
- 世界地図を構築する
- チャートデータを指定する別の方法
- マーカーの大きさをカスタマイズする
- マーカーの色をカスタマイズする
- ほかのカラースケール
- ホバーテキストを追加する

### まとめ

---

&nbsp;

## Chap.06 APIを取り扱う

### Web APIを使う

- GitとGitHub
  - [GitHub](https://github.com/)
- API呼び出しを使ってデータをリクエストする
  - <https://api.github.com/search/repositories?q=language:python&sort=stars>
- Requestsをインストールする

```bash
python3 -m pip install --user requests
```

```bash
Collecting requests
  Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.1/63.1 KB 1.7 MB/s eta 0:00:00
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.2/149.2 KB 3.9 MB/s eta 0:00:00
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.0/139.0 KB 3.8 MB/s eta 0:00:00
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 2.1 MB/s eta 0:00:00
Installing collected packages: certifi, urllib3, idna, charset-normalizer, requests
  WARNING: The script normalizer is installed in '/Users/takeru/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.12 idna-3.3 requests-2.27.1 urllib3-1.26.9
```

- APIのレスポンスを処理する

```bash
ステータスコード: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
```

- レスポンスの辞書を処理する
- 上位のリポジトリを要約する
- API利用頻度の制限を監視する
  - <https://api.github.com/rate_limit>

```text
{
  "resources":{
    "core":{
      "limit":60,
      "remaining":60,
      "reset":1650224475,
      "used":0,
      "resource":"core"
    },
    "graphql":{
      "limit":0,
      "remaining":0,
      "reset":1650224475,
      "used":0,
      "resource":"graphql"
    },
    "integration_manifest":{
      "limit":5000,
      "remaining":5000,
      "reset":1650224475,
      "used":0,
      "resource":"integration_manifest"
    },
    "search":{
      "limit":10,
      "remaining":10,
      "reset":1650220935,
      "used":0,
      "resource":"search"
    }
  },
  "rate":{
    "limit":60,
    "remaining":60,
    "reset":1650224475,
    "used":0,
    "resource":"core"
  }
}
```

### Plotlyを使ってリポジトリを可視化する

- Plotlyのグラフを改良する
- カスタマイズしたツールチップを追加する
- グラフにクリック可能なリンクを追加する
- PlotlyおｙびGitHub APIについてさらに詳しく
  - [Plotly User Guide in Python](https://plot.ly/python/user-guide/)
  - [Python Figure Reference](https://plot.ly/python/reference/)
  - [GitHub Docs](https://docs.github.com/ja)
  - [GitHub REST API](https://docs.github.com/ja/rest)
  - [GitHub GraphQL API](https://docs.github.com/ja/graphql)

### Hacker News API

### まとめ

---

&nbsp;
