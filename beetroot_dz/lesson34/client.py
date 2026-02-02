import socket
import sys
import random
import time

from threading import Thread
from datetime import datetime
from colorama import init, Fore

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

client_color = random.choice(colors)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'Connecting to {SERVER_HOST}:{SERVER_PORT}...')
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f'Connected to {SERVER_HOST}:{SERVER_PORT}')

name = input('Enter unique name: ')

commands = """All available commands:
/list - Get all rooms
/create room_name password - Create a new room
/join room_name password - Join to existing room
/rename old_name new_name - Rename an existing room
/leave - Leave current room
/close - Close program
"""
print(commands)


def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(2048).decode('utf-8')
            print(message)
        except Exception as error:
            print(f'An error occurred: {error}')
            break


receiver = Thread(target=receive_message, args=(client_socket,), daemon=True)
receiver.start()

while True:
    message = input()
    command = message.split(' ')[0]
    if command in ['/list', '/create', '/join', '/rename', '/leave']:
        client_socket.send(message.encode('utf-8'))
    elif command == '/close':
        client_socket.close()
        print('Closing program...')
        time.sleep(3)
        sys.exit()
    else:
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formated_message = f'{command}[{data}] {name}: {message}{Fore.RESET}'
        client_socket.send(formated_message.encode('utf-8'))