# 10-05.プログラミングの投票
# 10_05_programming_poll.txtを出力

print("\n# 10-05.プログラミングの投票\n")

filename = 'chap_10/10_05_programming_poll.txt'

responses = []
while True:
    response = input("\nプログラミンが好きな理由は何ですか？ >> ")
    responses.append(response)

    continue_poll = input("誰かほかに回答する人はいますか？（y/n）>> ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
