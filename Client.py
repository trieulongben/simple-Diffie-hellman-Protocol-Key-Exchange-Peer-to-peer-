import socket
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
def Host(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Start listening...')
        conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
def Connect(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'connected')
        data = s.recv(1024)
def Send(HOST,PORT,data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.sendall(data)
        check= s.recv(1024)
    print('Received', repr(data))
def Receive(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.recv(1024)
    return s.recv(1024)
