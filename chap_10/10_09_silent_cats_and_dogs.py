# 10-09.静かなネコとイヌ

print("\n# 10-09.静かなネコとイヌ\n")

filenames = [
    'chap_10/cats.txt',
    'dogs.txt',
]

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print(f"\n読込中のファイル: {filename}")
        print(contents)

