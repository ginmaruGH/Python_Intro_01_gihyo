# 全体をループする処理
print("\nChap.4 全体をループする処理")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# forループの中でより多くの作業をする
print("\nforループの中でより多くの作業をする")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}は、素晴らしい手品をした。")
    print(f"私は、{magician.title()}の次の手品が待ちきれない。\n")

print("みなさんありがとう。素晴らしい手品ショーでした。")
