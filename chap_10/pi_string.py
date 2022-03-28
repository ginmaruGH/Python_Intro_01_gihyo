## Chapter10 ファイルと例外
### ファイルを読み込む
#### ファイルの内容を操作する

print("\nファイルの内容を操作する\n")

filename = '/Users/takeru/Library/CloudStorage/OneDrive-個人用/Learn/Python/Python_Intro_01_gihyo/chap_10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
