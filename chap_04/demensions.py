# タプルを定義する
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# タプルのすべての値でループする
print("\nタプルのすべての値でループする\n")

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# タプルの再定義
print("\nタプルの再定義\n")

print("元のサイズ")
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print("変更したサイズ")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
