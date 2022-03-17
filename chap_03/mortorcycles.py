motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")
print(motorcycles)

# 空のリストから要素を追加する
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print("空のリストから要素を追加する")
print(motorcycles)

# リストの中に要素を追加する
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# リストから要素を削除する
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# pop()メソッドを使用して要素を削除する
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# リスト中の任意の位置から要素を削除する
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"最初に手に入れたバイクは{first_owned.title()}です。")
print(motorcycles)

# 値を指定して、要素を1つ削除する
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# remove()メソッドを使用して削除した値を使用する
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}は、私には高すぎます。")
