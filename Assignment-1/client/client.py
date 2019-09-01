import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 7877)

def main():
    running = True
    while running:
        command = input('What command would you like to perform?\n > ')
        if command.lower() == 'connect':
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            account_number = input('Write your account number:\n > ')

            sock.sendall(str.encode(account_number))

            connectRunning = True
            while connectRunning:
                action = input('What do you want to do? Type \'help\' for help!\n')
                if action.lower() == 'help':
                    print('Help text!')            
                    print('> create_account - to get command help')            
                    print('> check_balance - to get command help')
                    print('> withdraw <amount> - to get command help')
                    print('> deposit <amount> - to get command help')
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
                    print('recieved {!r}'.format(data))
                    pass
            sock.close()
        elif command.lower() == 'settings':
            server_address[0] = input('Input server ip!\n > ')
            server_address[1] = int(input('Input server port!\n > '))
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