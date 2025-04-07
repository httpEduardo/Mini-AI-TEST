from chatbot.bot import get_response

print("Chatbot iniciado! (Digite 'sair' para encerrar)")
while True:
    msg = input("Você: ")
    if msg.lower() == 'sair':
        break
    resp = get_response(msg)
    print("Bot:", resp)
