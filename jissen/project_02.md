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
- グラフを自動的に保存する

### ランダムウォーク

### Plotlyでサイコロを転がす

### まとめ

---

&nbsp;

## Chap.05 データをダウンロードする

---

&nbsp;

## Chap.06 APIを取り扱う

---

&nbsp;
