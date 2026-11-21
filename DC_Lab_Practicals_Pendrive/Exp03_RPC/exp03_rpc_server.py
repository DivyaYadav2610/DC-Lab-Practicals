from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


with SimpleXMLRPCServer(("localhost", 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(add, "add")
    server.register_function(subtract, "subtract")
    server.register_function(multiply, "multiply")
    server.register_function(divide, "divide")
    print("Server is running on port 8000...")
    server.serve_forever()
