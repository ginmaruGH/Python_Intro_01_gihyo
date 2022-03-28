## Chapter10 ファイルと例外
### ファイルを読み込む
#### 100万桁の巨大なファイル

print("\n100万桁の巨大なファイル\n")

filename = '/Users/takeru/Library/CloudStorage/OneDrive-個人用/Learn/Python/Python_Intro_01_gihyo/chap_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
