# 6-2.好きな数字
print("\n# 6-2.好きな数字\n")

favorite_numbers = {
    'tanjiro': 42,
    'zenitsu': 23,
    'inosuke': 7,
    'giyu': 1_000_000,
    'sumi': 0,
}
for favorite_number in favorite_numbers.items():
    print(f"{favorite_number[0]}: {favorite_number[1]}")
