## Chapter10 ファイルと例外
### ファイルを読み込む
#### πの中に誕生日が含まれているか

print("\nπの中に誕生日が含まれているか\n")

filename = 'chap_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

birthday = input("誕生日を、mmddyyフォーマットで入力してください。>> ")
if birthday in pi_string:
    print("円周率の最初の100万桁にあなたの誕生日が見つかりました！")
else:
    print("円周率の最初の100万桁にあなたの誕生日は見当たらないようです。")
