# ビュッフェ

menu_items = (
    'ハンバーグステーキ', 'ポークリブ', 'ラムチョップ',
    'サーモングリル', 'ロブスター',)

print("以下のメニューから選択できます。")
for item in menu_items:
    print(f"- {item}")

# タプルの要素の一部変更でTypeErrorになる
# menu_items[-1] = "イカフライ"

# タプルの変更（再定義）
menu_items = (
    'ハンバーグステーキ', 'ポークリブ', 'ラムチョップ',
    '真鯛のグリル', 'イカフライ',)

print("\nメニューが変更になりました。")
print("以下のメニューから選択できます。")
for item in menu_items:
    print(f"- {item}")
