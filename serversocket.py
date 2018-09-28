import socket

class HTTPserver(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.server_socket.bind(("",8888))
        self.server_socket.listen(128)

    def handler_client(self):
        client_socket, client_addr = self.server_socket.accept()
        self.response_server(client_socket)

    def response_server(self, client_socket):
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"
        response_body = "haha"
        response_data = response_headers + response_body
        client_socket.send(response_data.encode())
        client_socket.close()
def main():
    server = HTTPserver()
    server.handler_client()
    


if __name__ == '__main__':
    main()






