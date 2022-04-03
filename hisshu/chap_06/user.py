# 辞書をループする
print("\n# 辞書をループする\n")

# すべてのキーと値のペアをループする
print("\n# すべてのキーと値のペアをループする\n")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'efermi',
}

# forループ items()
print("\n# forループ items()")
for key, value in user_0.items():
    print(f"Key:   {key}")
    print(f"Value: {value}")
