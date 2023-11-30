import socket
import os

os.system("color 4")

print("""

      

   _____                             _____ _             _           _ 
  / ____|                           / ____| |           | |         | |
 | (___   ___ _ ____   _____ _ __  | (___ | |_ __ _ _ __| |_ ___  __| |
  \___ \ / _ \ '__\ \ / / _ \ '__|  \___ \| __/ _` | '__| __/ _ \/ _` |
  ____) |  __/ |   \ V /  __/ |     ____) | || (_| | |  | ||  __/ (_| |
 |_____/ \___|_|    \_/ \___|_|    |_____/ \__\__,_|_|   \__\___|\__,_|
                                                                       
                                                                       

""")

def perform_operation(expression):
    try:
        operators = set('+-*/')
        for op in operators:
            if op in expression:
                num1, num2 = map(float, expression.split(op))
                if op == '+':
                    return str(num1 + num2)
                elif op == '-':
                    return str(num1 - num2)
                elif op == '*':
                    return str(num1 * num2)
                elif op == '/':
                    return str(num1 / num2)
        return "Invalid expression"
    except Exception as e:
        return "Error: " + str(e)

def server_program():
    host = socket.gethostname()
    port = 9999

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    conn.send("Hello! What is your name?".encode())
    client_name = conn.recv(1024).decode()
    print("Client's name: " + client_name)

    conn.send(f"Hello {client_name}! How old are you?".encode())
    client_age = conn.recv(1024).decode()
    print(f"{client_name}'s age: " + client_age)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"{client_name}: " + str(data))

        if data.lower().strip() == 'exit':
            break

        result = perform_operation(data)
        print('Sending result to ' + client_name + ": " + result)
        conn.send(result.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
