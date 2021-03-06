import Client as Client
class User:
    received_public_key = None

    def __init__(self, modulo, primitive_root_modulo, private_key):
        def is_prime(n):
            for i in range(2, n // 2):
                if n % i == 0:
                    return False
            return True

        if is_prime(modulo):
            self.modulo = modulo
        else:
            raise Exception('The modulo must be a prime number')
        self.primitive_root_modulo = primitive_root_modulo
        self.private_key = private_key

    def send_public_key(self, object):
        secret = self.primitive_root_modulo**self.private_key % self.modulo
        HOST = '127.0.0.2'  # The server's hostname or IP address
        PORT = 65432        # The port used by the server
        Client.Send(HOST,PORT,secret)

    def get_shared_secret_key(self):
        HOST = '127.0.0.2'  # The server's hostname or IP address
        PORT = 65432        # The port used by the server
        self.received_public_key=Client.Receive(HOST,PORT)
        if self.received_public_key is None:
            print('I didn\' received the shared public key.')
            return None
        else:
            return self.received_public_key ** self.private_key % self.modulo

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

Alice = User(23, 5, 4)
Bob = User(23, 5, 3)
Client.Host(HOST,PORT)
Alice.send_public_key(Bob)
Bob.send_public_key(Alice)
print('Alice')
print('Received:', Alice.received_public_key)
print('Secret key:', Alice.get_shared_secret_key())
print('===================')
print('Bob')
print('Received:', Bob.received_public_key)
print('Secret key:', Bob.get_shared_secret_key())
