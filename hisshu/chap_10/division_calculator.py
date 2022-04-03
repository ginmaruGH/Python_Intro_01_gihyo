## Chapter10 ファイルと例外
### 例外
#### `ZeroDivisionError`を例外処理する

print("\n#### `ZeroDivisionError`を例外処理する\n")

try:
    print(5/0)
except ZeroDivisionError:
    print("ゼロで割ることはできません。")
