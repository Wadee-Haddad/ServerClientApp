import socket
import os

os.system("color 2")

print("""
      

   _____ _ _            _      _____ _             _           _ 
  / ____| (_)          | |    / ____| |           | |         | |
 | |    | |_  ___ _ __ | |_  | (___ | |_ __ _ _ __| |_ ___  __| |
 | |    | | |/ _ \ '_ \| __|  \___ \| __/ _` | '__| __/ _ \/ _` |
 | |____| | |  __/ | | | |_   ____) | || (_| | |  | ||  __/ (_| |
  \_____|_|_|\___|_| |_|\__| |_____/ \__\__,_|_|   \__\___|\__,_|
                                                                 


""")

def client_program():
    host = socket.gethostname()
    port = 9999

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Connected to the server.")

    greeting = client_socket.recv(1024).decode()
    print(greeting)

    name = input("Enter your name: ")
    client_socket.send(name.encode())

    age_question = client_socket.recv(1024).decode()
    print(age_question)

    age = input("Enter your age: ")
    client_socket.send(age.encode())

    print("Type 'exit' to quit.")

    while True:
        expression = input("Enter expression (5 + 8 , etc): ")

        if expression.lower().strip() == 'exit':
            client_socket.send(expression.encode())
            break

        client_socket.send(expression.encode())
        data = client_socket.recv(1024).decode()

        print('Server result: ' + data)

    client_socket.close()

if __name__ == '__main__':
    client_program()
