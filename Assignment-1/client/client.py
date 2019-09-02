import socket
import sys
import filemanager


config = filemanager.load_data("../config.json")

def main():
    running = True
    while running:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (config['server_ip'], int(config['server_port']))
        command = input('What command would you like to perform?\n > ')
        if command.lower() == 'connect':
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            account_number = input('Write your account number:\n > ')

            sock.sendall(str.encode(account_number))

            connectRunning = True
            while connectRunning:
                action = input('What do you want to do? Type \'help\' for help!\n > ')
                if action.lower() == 'help':
                    print('Help text!')
                    print('> help - Help text shown here')
                    print('> create account - create a new account')            
                    print('> check balance - to get a status on your balance')
                    print('> withdraw <amount> - to withdraw money from the account')
                    print('> deposit <amount> - to deposit money to the account')
                    print('> disconnect - to disconnect from the server')
                elif action.lower() == 'disconnect':
                    connectRunning = False
                    message = str.encode(action)
                    sock.sendall(message)
                    print('Disconnected!')
                else:
                    message = str.encode(action)
                    sock.sendall(message)
                    data = sock.recv(512)
                    print('<< Server response >> ' + data.decode('utf-8'))
                    pass
            sock.close()
        elif command.lower() == 'create account':
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            sock.sendall(b'create_account')
            data = sock.recv(16)
            print('Account created, account number {!r}'.format(data))
            sock.close()
        elif command.lower() == 'settings':
            print('Yet to be implemented!')
            pass
        elif command.lower() == 'help':
            print('Help text!')
            print('> connect - to get command help')            
            print('> help - to get command help')
            print('> exit - to exit the application')
        elif command.lower() == 'exit':
            print('Exiting application!')
            running = False
        else:
            print('Run the command \'help\' to recieve command help!')

if __name__ == '__main__':
    main()