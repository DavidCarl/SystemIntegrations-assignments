import SOAPpy


def hello():
    return "Hello World"
    
server = SOAPpy.SOAPServer(("localhost", 8888))
server.registerFunction(hello)
server.serve_forever()