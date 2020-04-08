#resource used: https://docs.python.org/3/library/socketserver.html#socketserver-tcpserver-example

import socketserver
import json
import os

class handler(socketserver.BaseRequestHandler):
    #global path
    getPath = "test"
    postPath = "test"
    def handle(self):
        string = " "
        rec_data = self.request.recv(1024).strip()
        print(rec_data)
        if b"GET" in rec_data:
            string = rec_data.decode("utf-8")
            word = string.split(' ')
        f = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\index.html"
        f1 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\index.html"
        f2 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\styles.css"
        f3 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\counter.js"
        p = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\Profess-pic.jpg"
        ajax = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\ajax.js"
        mess_data = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\data.txt"
        html = open(f, 'r')
        html2 = open(f, 'r')
        css = open(f2, 'r')
        js = open(f3, 'r')
        pic = open(p, 'rb')
        aj = open(ajax, 'r')
        data = open(mess_data, 'r')
        if "GET" in string:
            oreo, getPath = parseGetRequest(string)
            if getPath == "/" and oreo == 0:
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/html\n")
                self.request.sendall(b"Set-Cookie: sessionID=2342\n")
                self.request.sendall(b"\r\n")
                for content in html.readlines():
                    self.request.sendall(str.encode(""+content+""))
                    content = html.read(1024)
                html.close()
            elif getPath == "/" and oreo == 1:
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/html\n")
                self.request.sendall(b"Set-Cookie: sessionID=2342\n")
                self.request.sendall(b"\r\n")
                for content2 in html2.readlines():
                    self.request.sendall(str.encode(""+content2+""))
                    content2 = html2.read(1024)
                html2.close()    
            elif getPath == "/styles.css":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/css\n")
                self.request.sendall(b"\r\n")
                for style in css.readlines():
                    self.request.sendall(str.encode(""+style+""))
                    style = css.read(1024)
                css.close()
            elif getPath == "/Profess-pic.jpg":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: image/jpeg\n")
                self.request.sendall(b"\r\n")
                for pc in pic.readlines():
                    self.request.sendall(pc)
                    pc = pic.read(1024)
                pic.close()
            elif getPath == "/counter.js":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/javascript\n")
                self.request.sendall(b"\r\n")
                for j in js.readlines():
                    self.request.sendall(str.encode(""+j+""))
                    j = js.read(1024)
                js.close()
            elif getPath == "/ajax.js":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/javascript\n")
                self.request.sendall(b"\r\n")
                for a in aj.readlines():
                    self.request.sendall(str.encode(""+a+""))
                    a = aj.read(1024)
                aj.close()
            elif getPath == "/?q=jama+jama":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/plain\n")
                self.request.sendall(b"Content-Length: 43 \n\n Hello Jama, I'm responding to your query.\n\n")
                self.request.sendall(b"\r\n")
            elif getPath == "/json":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/plain\n")
                self.request.sendall(b"\r\n")
                for d in data.readlines():
                    self.request.sendall(str.encode(""+d+""))
                    d = data.read(1024)
                data.close()                
            else: 
                self.request.sendall(b"HTTP/1.1 404 Not Found\n")
        elif b"POST" in rec_data:
            postPath = parsePostRequest(rec_data.decode("ISO-8859-1"))
            foundMessage = False
            if postPath == "/form-path":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/html\n")
                self.request.sendall(b"Set-Cookie: sessionID=2342\n")
                self.request.sendall(b"\r\n")
                for content2 in html2.readlines():
                    self.request.sendall(str.encode(""+content2+""))
                    content2 = html2.read(1024)
                html2.close()
            elif postPath == "/send-message":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"\r\n")                
def parseGetRequest(req):
    requestType = " "
    oreo = " "
    getPath = " "
    found = False
    oreo = 0
    temp = req
    print("#########################START_______GET_________START###########################\n")
    print(temp)
    print("#########################END_______GET_________END###########################\n\n")
    word = req.split('\n')
    for w in word:
        w = req.split(' ')
        if "Content-Disposition" in w:
                sdv = 434
        for w2 in w:
            if "/" in w2 and found == False:
                getPath = w2
                #print(w)
                found = True
            if "Cookie" in w2:
                oreo = 1
            if "json" in w2:
                sdv = 434
        return oreo, getPath

def parsePostRequest(req):
    filepath = os.path.join("C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw5\\", "data.txt")
    data = open(filepath, 'a')
    global requestType
    global oreo 
    global postPath
    found = False 
    foundBound = False
    foundMessage = False
    oreo = 0
    temp = req
    print("#########################START_______POST_________START###########################\n")
    print(temp)
    print("#########################END_______POST_________END###########################")
    word = req.split('\n')
    for w in word:
        w = req.split(' ')
        for w2 in w:
            if "/" in w2 and not("HTTP" in w2) and found == False:
                postPath = w2
                found = True
                print(w2)
            if "visitor=Jay&comment=C" in w2:
                myInput = w2.partition("sessionID=2342\r\n\r\n")[2]
                start = myInput.find("visitor=") + len("visitor=")
                end = myInput.find("&")
                final = myInput[start:end]
                myInput2 = myInput.split("comment=")
                final2 = myInput2[1]
                f = open("writeSubmission.txt", "a")
                f.write(final + " " + final2)
                #print(myInput)
                f.close()
            if "WebKitFormBoundary" in w2 and foundBound == False:
                foundBound = True
                bound = w2
                start = bound.find("WebKitFormBoundary") + len("WebKitFormBoundary")
                end = bound.find("\r")
                boundary = bound[start:end]
                boundary = "------WebKitFormBoundary" + boundary + "--"
            if "/send-message-form" in w2:
                sdv = 434
    if not foundMessage and postPath == "/send-message":
        for ww in word:
            message = word[16]
            data.write(message + "\n")
            foundMessage = True
            break
        return postPath

if __name__ == "__main__":
    with socketserver.TCPServer(("localhost", 8000), handler) as server:
        server.serve_forever()