# 8-05.都市
print("\n# 8-05.都市\n")

def describe_city(city, country='Japan'):
    """都市について説明する"""
    msg = f"{city}は、{country}にあります。"
    print(msg)

describe_city('Kyoto')
describe_city('レイキャビック', 'アイスランド')
describe_city('Sapporo')
