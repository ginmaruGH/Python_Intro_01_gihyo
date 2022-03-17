print("\n平方数のリストを作る\n")

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 数値のリストによる簡単な統計
print("\n数値のリストによる簡単な統計")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,0]
print(digits)
print(f"min: {min(digits)}")
print(f"max: {max(digits)}")
print(f"sum: {sum(digits)}")

# リスト内包表記
print("\nリスト内包表記\n")

print("squares = [value**2 for value in range(1, 11)]")
squares = [value**2 for value in range(1, 11)]
print(squares)
