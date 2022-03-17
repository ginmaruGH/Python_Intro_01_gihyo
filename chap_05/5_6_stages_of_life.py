# # 5-6.ライフステージ
print("\n5-6.ライフステージ\n")

age = 75
print(f"age: {age}")

if age < 2:
    stage = '赤ちゃん'
elif 2 <= age and age < 4:
    stage = '幼児'
elif 4 <= age and age < 13:
    stage = '子供'
elif 13 <= age and age < 20:
    stage = 'ティーンエイジャー。'
elif 20 <= age and age < 65:
    stage = '大人'
else:
    stage = '高齢者'

print(f"あなたは、{stage}です。")
