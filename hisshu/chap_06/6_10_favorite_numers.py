# 6.10 好きな数字
print("\n# 6.10 好きな数字\n")

favorite_numbers = {
    'tanjiro': [42, 17],
    'zenitsu': [42, 39, 56],
    'inosuke': [7, 12],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}の好きな数字は、以下です。")
    for number in numbers:
        print(f" {number}")
