import socket
import sys
import random
import filemanager


config = filemanager.load_data("../config.json")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', int(config['server_port']))
print('starting server on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

def main():
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            connected = True
            customerNumber = connection.recv(16)
            custNumbStr = customerNumber.decode("utf-8")
            
            if custNumbStr == 'create_account':
                print('sending data back to the client')
                handle = generate_customer_id()
                connection.sendall(str.encode(str(handle)))
                connection.close()
            else:
                while connected:
                    customers = filemanager.load_data("customer.json")
                    data = connection.recv(32)
                    print(data[0:8])
                    print('received {!r}'.format(data))
                    if data == b'check balance':
                        balance = customers[custNumbStr]['balance']
                        currency = customers[custNumbStr]['currency']
                        print(balance)
                        connection.sendall(str.encode(balance + ' ' + currency))
                    elif data[0:8] == b'withdraw':
                        withdrawAmount = int(data[9:].decode("utf-8"))
                        balance = int(customers[custNumbStr]['balance'])
                        currency = customers[custNumbStr]['currency']
                        if withdrawAmount < balance:
                            res = balance - withdrawAmount
                            customers[custNumbStr]['balance'] = str(res)
                            filemanager.save_data("customer.json", customers)
                            response = 'Withdrew ' + str(withdrawAmount) + ' ' + currency + ' and you got ' + str(res) + ' ' + str(currency) + ' left!'
                            connection.sendall(str.encode(response))
                        else:
                            response = 'Sorry, there is not enough money on your account. You got ' + balance + ' ' + currency 
                            connection.sendall(str.encode(response))
                    elif data[0:7] == b'deposit':
                        depositAmount = int(data[8:].decode("utf-8"))
                        balance = customers[custNumbStr]['balance']
                        currency = customers[custNumbStr]['currency']
                        res = int(balance) + depositAmount
                        customers[custNumbStr]['balance'] = str(res)
                        filemanager.save_data("customer.json", customers)
                        response = 'Money depositet, new balance is ' + str(res) + ' ' + currency 
                        connection.sendall(str.encode(response))
                    elif data == b'disconnect':
                        connection.close()
                        connected = False
                    else:
                        print('Unrecognized Command')
                        connection.sendall(b'Unrecognized Command')
        finally:
            connection.close()

def generate_customer_id():
    customers = filemanager.load_data("customer.json")
    handle = random.randint(1000, 9999)
    customers[str(handle)] = {'balance': config['start_money'], 'currency': config['currency']}
    filemanager.save_data("customer.json", customers)
    return handle

if __name__ == '__main__':
    main()