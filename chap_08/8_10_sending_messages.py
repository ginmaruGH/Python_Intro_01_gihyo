# 8-10.メッセージを送信する
print("\n# 8-10.メッセージを送信する\n")

def show_messages(messages):
    """リストの中のメッセージを出力する"""
    print("全メッセージを表示します。")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """各メッセージを出力し、sent_messagesに移動する"""
    print("\n全メッセージを送信します。")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["おはようございます。", "こんにちは。", "こんばんは。"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\n最終的なリストの状態")
print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")
