import requests
import json
import zeep


def main():
    running = True
    while running:
        command = input('What command would you like to perform?\n > ')
        if command.lower() == 'soap':
            soap_loop()
        elif command.lower() == 'api':
            api_loop()
        elif command.lower() == 'exit':
            running = False
        else:
            print('Wrong command')
            print('use \'soap\' for using the soap server')
            print('use \'api\' for using the api server')            
            print('use \'exit\' for closing the script')
    print('Bye!')

def api_loop():
    print('You will be asked for 2 numbers (float use .) and 1 operator')
    n1 = input('What should the first number be?\n > ')
    operator = input('What should the operator be? Valid operators are + - * /\n > ')
    n2 = input('What should the second number be?\n > ')
    post_api(float(n1), operator, float(n2))

def soap_loop():
    print('You will be asked for 2 numbers (float use .) and 1 operator')
    n1 = input('What should the first number be?\n > ')
    operator = input('What should the operator be? Valid operators are + - * /\n > ')
    n2 = input('What should the second number be?\n > ')
    soap(float(n1), operator, float(n2))

def post_api(n1, operator, n2):
    payload = {'key1': n1, 'operator': operator, 'key2': n2}
    res = requests.post('http://localhost:5000', data=json.dumps(payload)).content.decode('utf-8')
    print(res)

def soap(n1, operator, n2):
    wsdl = 'http://localhost:8080/service/calculator.wsdl'
    client = zeep.Client(wsdl)
    print(client.service.Calculator(n1, operator, n2))

if __name__ == "__main__":
    main()