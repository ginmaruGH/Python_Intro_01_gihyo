# sort()
# 順番を元には戻せない
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted()
cars = ["bmw", "audi", "toyota", "subaru"]
print("\n元のリスト")
print(cars)

print("\nソートされたリスト")
print(sorted(cars))

print("\n元のリストを再表示")
print(cars)

# リストを逆順で出力する
# reverse()
print("\nリストを逆順で出力する")
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)
print("\n")

# リストの長さを調べる
# len()
print("\nリストの長さを調べる")
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))
