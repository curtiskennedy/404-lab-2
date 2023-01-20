import socket

BYTES_TO_READ = 4096

def get(host, port):

    request = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"
    # note, this is the http1.1 spec, it differentiates headers from the body by the double newline
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    s.send(request)

    s.shutdown(socket.SHUT_WR)

    result = s.recv(BYTES_TO_READ)
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close()

get("www.google.com", 80)
