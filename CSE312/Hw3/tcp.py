#resource used: https://docs.python.org/3/library/socketserver.html#socketserver-tcpserver-example

import socketserver

class handler(socketserver.BaseRequestHandler):
    requestType = "test"
    path = " test"
    

    def handle(self):
        rec_data = self.request.recv(1024).strip()
        string = rec_data.decode("utf-8")
        word = string.split(' ')
        oreo = parseRequest(string)
        f = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw3\\index.html"
        f1 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw3\\index2.html"
        f2 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw3\\styles.css"
        f3 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw3\\counter.js"
        p = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw3\\Profess-pic.jpg"
        html = open(f, 'r')
        html2 = open(f1, 'r')
        css = open(f2, 'r')
        js = open(f3, 'r')
        pic = open(p, 'rb')
        if requestType == "GET":
            test = 0
        if path == "/" and oreo == 0:
            self.request.sendall(b"HTTP/1.1 200 OK\n")
            self.request.sendall(b"Content-Type: text/html\n")
            self.request.sendall(b"Set-Cookie: sessionID=2342\n")
            self.request.sendall(b"\r\n")
            for content in html.readlines():
                self.request.sendall(str.encode(""+content+""))
                content = html.read(1024)
            html.close()
        elif path == "/" and oreo == 1:
            self.request.sendall(b"HTTP/1.1 200 OK\n")
            self.request.sendall(b"Content-Type: text/html\n")
            self.request.sendall(b"Set-Cookie: sessionID=2342\n")
            self.request.sendall(b"\r\n")
            for content2 in html2.readlines():
                self.request.sendall(str.encode(""+content2+""))
                content2 = html2.read(1024)
            html2.close()    
        elif path == "/styles.css":
            self.request.sendall(b"HTTP/1.1 200 OK\n")
            self.request.sendall(b"Content-Type: text/css\n")
            self.request.sendall(b"\r\n")
            for style in css.readlines():
                self.request.sendall(str.encode(""+style+""))
                content = css.read(1024)
            css.close()
        elif path == "/Profess-pic.jpg":
            self.request.sendall(b"HTTP/1.1 200 OK\n")
            self.request.sendall(b"Content-Type: image/jpeg\n")
            self.request.sendall(b"\r\n")
            for pc in pic.readlines():
                self.request.sendall(pc)
                pc = pic.read(1024)
            pic.close()
        elif path == "/counter.js":
            self.request.sendall(b"HTTP/1.1 200 OK\n")
            self.request.sendall(b"Content-Type: text/javascript\n")
            self.request.sendall(b"\r\n")
            for j in js.readlines():
                self.request.sendall(str.encode(""+j+""))
                content = js.read(1024)
            js.close()
        elif path == "/?q=jama+jama":
            self.request.sendall(b"HTTP/1.1 200 OK\n")
            self.request.sendall(b"Content-Type: text/plain\n")
            self.request.sendall(b"Content-Length: 43 \n\n Hello Jama, I'm responding to your query.\n\n")
            self.request.sendall(b"\r\n")
        else: 
            self.request.sendall(b"HTTP/1.1 404 Not Found\n")
    
def parseRequest(req):
    global requestType
    global oreo 
    global path 
    oreo = 0
    temp = req
    print(temp)
    word = req.split('\n')
    for w in word:
        if "GET" in w:
            requestType = w.split(' ')[0]
            path = w.split(' ')[1]
        if "POST" in w:
            requestType = "POST"
        if "/" in w:
            #path = w
            print(w)
        if "Cookie" in w:
            oreo = 1
    return oreo

def getFunc(path):
    return

if __name__ == "__main__":
    with socketserver.TCPServer(("localhost", 8000), handler) as server:
        server.serve_forever()