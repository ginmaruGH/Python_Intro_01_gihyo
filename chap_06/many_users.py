# 辞書の値に辞書を入れる
print("\n# 辞書の値に辞書を入れる\n")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maric',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nユーザー名: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\t氏名: {full_name.title()}")
    print(f"\t場所: {location.title()}")
