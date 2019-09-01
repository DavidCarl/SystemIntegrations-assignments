import socket
import sys
import random
import filemanager


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 7877)
print('starting server on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

def main():
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            connected = True
            while connected:
                print('connection from', client_address)
                
                customers = filemanager.load_data()
                customerNumber = connection.recv(16)

                print(customerNumber)

                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data == b'create_account':
                    print('sending data back to the client')
                    handle = generate_customer_id()
                    connection.sendall(str.encode(str(handle)))
                elif data == b'check_balance':
                    balance = customers[customerNumber.decode("utf-8")]['balance']
                    currency = customers[customerNumber.decode("utf-8")]['currency']
                    print(balance)
                    connection.sendall(str.encode(balance + ' ' + currency))
                elif data == b'withdraw':
                    pass
                elif data == b'deposit':
                    pass
                elif data == b'disconnect':
                    connection.close()
                    connected = False
                else:
                    print('Unrecognized Command')
                    connection.sendall(b'Unrecognized Command')
                    break
        finally:
            pass

def generate_customer_id():
    customers = filemanager.load_data()
    print(customers)
    handle = random.randint(1000, 9999)
    customers[handle] = {'balance': '500', 'currency': 'USD'}
    filemanager.save_data(customers)
    return handle

if __name__ == '__main__':
    main()