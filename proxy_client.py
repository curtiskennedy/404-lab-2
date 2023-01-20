import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request)
        client_socket.shutdown(socket.SHUT_WR)
        print("Waiting for response!")

        chunk = client_socket.recv(BYTES_TO_READ)
        result = b'' + chunk
        while(len(chunk) > 0):
            chunk = client_socket.recv(BYTES_TO_READ)
            result += chunk

        return result

print(get("127.0.0.1", 8080))
