import socket
from threading import Thread

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

client_database = {}  # {connection: 'room_name', connection: 'default'}
rooms = {}  # {room_name: password}
admins = {}  # {room_name: connection}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen(5)

print(f'Server listening on {SERVER_HOST}:{SERVER_PORT}')


def listen_for_client(connection):
    while True:
        try:
            message = connection.recv(2048).decode('utf-8')
            if len(message.split()) == 3:
                command, room_name, parameter = tuple(message.split())
            else:
                command, room_name, parameter = message, client_database[connection], None
        except Exception as error:
            if '[WinError 10054]' in str(error):
                connection.close()
                del client_database[connection]
                print(f'Client {connection} disconnected')
                break
            else:
                print(f'Failed to receive message: {error}')
                continue
        match command:
            case '/list':
                connection.send(str(list(rooms.keys())).encode('utf-8'))
            case '/join':
                if room_name in rooms and parameter == rooms[room_name]:
                    client_database[connection] = room_name
                    connection.send(f'Reconnect to {room_name}'.encode('utf-8'))
                else:
                    connection.send('Wrong room name or password.'.encode('utf-8'))
            case '/create':
                if room_name not in rooms:
                    rooms[room_name] = parameter
                    admins[room_name] = connection
                    client_database[connection] = room_name
                    connection.send(f'Reconnect to {room_name}'.encode('utf-8'))
                else:
                    connection.send(f'Current room {room_name} already exists.'.encode('utf-8'))
            case '/rename':
                if admins.get(room_name) == connection:  # room_name - old name, parameter - new name
                    rooms[parameter] = rooms.pop(room_name)
                    admins[parameter] = admins.pop(room_name)
                    for client, room in client_database.items():
                        if room == room_name:
                            client_database[client] = parameter
                    connection.send(f'Room {room_name} renamed to {parameter}'.encode('utf-8'))
                else:
                    connection.send('You are not an admin of this room.'.encode('utf-8'))
            case '/leave':
                client_database[connection] = 'default'
                connection.send(f'Leave {room_name} room'.encode('utf-8'))
            case _:
                room_clients = dict(filter(lambda item: item[1] == room_name, client_database.items()))
                room_clients.pop(connection)
                for client in room_clients:
                    client.send(message.encode('utf-8'))


while True:
    connection, client_address = server.accept()
    print(f'Client {client_address} connected')

    client_database[connection] = 'default'
    client_thread = Thread(target=listen_for_client, args=(connection,), daemon=True)
    client_thread.start()