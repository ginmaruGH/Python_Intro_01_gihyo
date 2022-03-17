# 6.09 好きな場所
print("\n# 6.09 好きな場所\n")

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'takanory': ['barcelona', 'billund', 'taipei'],
    'zenich': ['san francisco', 'amsterdam', 'cambell river'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}が好きな場所は、以下です。")
    for place in places:
        print(f" - {place.title()}")
