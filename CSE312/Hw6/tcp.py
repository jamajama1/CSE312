#resource used: https://docs.python.org/3/library/socketserver.html#socketserver-tcpserver-example

import socketserver
import json
import os
import hashlib
import codecs
import base64

class handler(socketserver.BaseRequestHandler):
    #global path
    getPath = "test"
    postPath = "test"
    def handle(self):
        done = False
        string = " "
        rec_data = self.request.recv(1024).strip()
        print(rec_data)
        if b"GET" in rec_data:
            string = rec_data.decode("utf-8")
            word = string.split(' ')
        f = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw6\\index.html"
        ajax = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw6\\ajax.js"
        mess_data = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw6\\data.txt"
        html = open(f, 'r')
        aj = open(ajax, 'r')
        data = open(mess_data, 'r')
        if "GET" in string:
            myHash, getPath = parseGetRequest(string)
            print(getPath)
            if getPath == "/":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/html\n")
                self.request.sendall(b"Set-Cookie: sessionID=2342\n")
                self.request.sendall(b"\r\n")
                for content in html.readlines():
                    self.request.sendall(str.encode(""+content+""))
                    content = html.read(1024)
                html.close()
            elif getPath == "/ajax.js":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/javascript\n")
                self.request.sendall(b"\r\n")
                for a in aj.readlines():
                    self.request.sendall(str.encode(""+a+""))
                    a = aj.read(1024)
                aj.close()
            elif getPath == "/json":
                self.request.sendall(b"HTTP/1.1 200 OK\n")
                self.request.sendall(b"Content-Type: text/plain\n")
                self.request.sendall(b"\r\n")
                for d in data.readlines():
                    self.request.sendall(str.encode(""+d+""))
                    d = data.read(1024)
                data.close()
            elif getPath == "/socket":
                GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
                #GUID = "3BD9BF5F-2360-4BE4-AF56-FB0FCB72D460"
                myHash = str(myHash)
                myHash = myHash + GUID
                h = hashlib.sha1()
                h.update(myHash.encode('utf-8'))
                myHash = h.digest()
                myHash = base64.b64encode(myHash)
                print(myHash)
                self.request.sendall(b"HTTP/1.1 101 Switching Protocols\r\n")
                self.request.sendall(b"Connection: Upgrade\r\n")
                self.request.sendall(b"Upgrade: websocket\r\n")
                self.request.sendall(b"Sec-WebSocket-Accept: ")
                self.request.sendall(myHash)
                self.request.sendall(b"\r\n\r\n")
                while not done:
                    rec_data = self.request.recv(1000000)
                    done = parseBytes(rec_data)
            else: 
                self.request.sendall(b"HTTP/1.1 404 Not Found\n")
            
        elif b"POST" in rec_data:
            postPath = parsePostRequest(rec_data.decode("ISO-8859-1"))
             
def parseGetRequest(req):
    count = 0
    myHash = " "
    requestType = " "
    getPath = " "
    found = False
    temp = req
    print("#########################START_______GET_________START###########################\n")
    print(temp)
    print("#########################END_______GET_________END###########################\n\n")
    word = req.split('\r\n')
    for w in word:
        count+=1
        w = req.split(' ')
        if "/socket" in w:
            findHash = w[27]
            fhash = findHash.split('\r\n')
            myHash = fhash[0]
            getPath = "/socket"
            found = True
        for w2 in w:
            if "/" in w2 and found == False:
                getPath = w2
                #print(w)
                found = True
    return myHash, getPath
        
def parsePostRequest(req):
    temp = req
    print("#########################START_______POST_________START###########################\n")
    print(temp)
    print("#########################END_______POST_________END###########################")
   
def parseBytes(data):
    bites = data
    print(type(bites))
    print(bites)
    frame = []
    for b in bites:
        frame.append(b)
    i = 0
    for f in frame:
        if i == 0:
            opcode = f & 15 
            print(opcode)
        elif i == 1: 
            load = f & 127
            print(load)
            if load == 126:
                load = frame[2]
                key =[]
                key.append(frame[2])
                key.append(frame[3])
                key.append(frame[4])
                key.append(frame[5])
                count = 0
                pl = []
                for i in range(6, load):
                    pl.append(frame[i] ^ key[count % 4])
                    count+=1
                    print(chr(pl[i-6]))
            elif load == 127:
                load = frame[2]
                key =[]
                key.append(frame[2])
                key.append(frame[3])
                key.append(frame[4])
                key.append(frame[5])
                count = 0
                pl = []
                for i in range(11, load):
                    pl.append(frame[i] ^ key[count % 4])
                    count+=1
                    print(chr(pl[i-6]))
            else:
                pload = [] 
                unlock = []
                pl = []
                key =[]
                key.append(frame[2])
                key.append(frame[3])
                key.append(frame[4])
                key.append(frame[5])
                count = 0
                for i in range(6, load + 5):
                    pl.append(frame[i] ^ key[count % 4])
                    count+=1
                    print(chr(pl[i-6]))
                print(pl)
        i+=1
    if opcode == 8:    
        return True
    else:
        return False

if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("localhost", 8003), handler) as server:
        server.serve_forever()