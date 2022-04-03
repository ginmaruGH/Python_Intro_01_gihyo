# スライス
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)
for number in odd_numbers:
    print(number)

print("\nリストの最初の3つの要素")
print(odd_numbers[:3])
for numbers in odd_numbers[:3]:
    print(numbers)

print("\nリストの中央の3つの要素")
print(odd_numbers[3:6])
for numbers in odd_numbers[3:6]:
    print(numbers)

print("\nリストの最後の3つの要素")
print(odd_numbers[-3:])
for numbers in odd_numbers[-3:]:
    print(numbers)
