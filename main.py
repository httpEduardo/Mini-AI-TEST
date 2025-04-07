from bot import get_response

print("Mini AI Channer Ativada. Diga algo:")
while True:
    msg = input("Você: ")
    if msg.lower() in ["sair", "exit", "quit"]:
        break
    print("IA:", get_response(msg))