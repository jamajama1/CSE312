#resource used: https://docs.python.org/3/library/socketserver.html#socketserver-tcpserver-example

import socketserver

class handler(socketserver.BaseRequestHandler):
    def handle(self):
        rec_data = self.request.recv(1024).strip()
        string = rec_data.decode("utf-8")
        word = string.split(' ')
        print(type(word))
        for w in word:
            if w == "GET":
                continue
            if w == "/hello":
                self.request.sendall(b"HTTP/1.1 200 OK\n Content-type: plain/text\n Content-Length: 13 \n\n Hello, World!\n\n")
                break
            elif w == "/redirect":
                self.request.sendall(b"HTTP/1.1 301 Moved Permanently\nLocation: /hello")
                break
            else: 
                self.request.sendall(b"HTTP/1.1 404 Not Found\n")
                break


if __name__ == "__main__":
    with socketserver.TCPServer(("localhost", 8000), handler) as server:
        server.serve_forever()