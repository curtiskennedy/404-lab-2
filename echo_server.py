import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1" # OR "localhost" OR "0.0.0.0" (all interfaces)
PORT = 8080


def handle_connection(conn, addr):
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data) # send vs sendall, send doesn't guarantee all data is sent, will return how much was sent
            # can compare with number of sent bytes
            # sendall will return if there is an error
    return

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # lab question

        s.listen()
        conn, addr = s.accept() #lab question
        handle_connection(conn, addr)
    return 

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)

        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

# start_server()
start_threaded_server()

# echo "foobar" | nc localhost 8080 -q 1
# q 1 means close connection after connection is done
# if it doesnt work, omit the flag
