import socket, ssl

f = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw7\\index.html"
f2 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw7\\styles.css"
f3 = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw7\\counter.js"
p = "C:\\Users\Muwahid Billah\\Desktop\\Computer Science\\CSE312\\Hw7\\Profess-pic.jpg"
html = open(f, 'r')
css = open(f2, 'r')
js = open(f3, 'r')
pic = open(p, 'rb')

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
 
host = 'localhost'
port = 8001 
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="public_cert.pem", keyfile="private.key")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((host, port))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        
        # data = conn.recv(4096)
        # conn.sendall(b"HTTP/1.1 200 OK\r\n")
    while True:
        done = False
        string = " "
        rec_data = conn.recv(4096).strip()
        print(rec_data)
        if b"GET" in rec_data:
            string = rec_data.decode("utf-8")
            word = string.split(' ')
        if "GET" in string:
            myHash, getPath = parseGetRequest(string)
            print(getPath)
        if getPath == "/":
                conn.sendall(b"HTTP/1.1 200 OK\n")
                conn.sendall(b"Content-Type: text/html\n")
                conn.sendall(b"Set-Cookie: sessionID=2342\n")
                conn.sendall(b"\r\n")
                for content2 in html.readlines():
                    conn.sendall(str.encode(""+content2+""))
                    content2 = html.read(1024)
                html.close()    
        elif getPath == "/styles.css":
            conn.sendall(b"HTTP/1.1 200 OK\n")
            conn.sendall(b"Content-Type: text/css\n")
            conn.sendall(b"\r\n")
            for style in css.readlines():
                conn.sendall(str.encode(""+style+""))
                style = css.read(1024)
            css.close()
        elif getPath == "/Profess-pic.jpg":
            conn.sendall(b"HTTP/1.1 200 OK\n")
            conn.sendall(b"Content-Type: image/jpeg\n")
            conn.sendall(b"\r\n")
            for pc in pic.readlines():
                conn.sendall(pc)
                pc = pic.read(1024)
            pic.close()
        elif getPath == "/counter.js":
            conn.sendall(b"HTTP/1.1 200 OK\n")
            conn.sendall(b"Content-Type: text/javascript\n")
            conn.sendall(b"\r\n")
            for j in js.readlines():
                conn.sendall(str.encode(""+j+""))
                j = js.read(1024)
            js.close()
        # conn.sendall(b"Content-Type: text/plain\r\n")
        # conn.sendall(b"Content-Length: 5\r\n")
        # conn.sendall(b"\r\n")
        # conn.sendall(b'Hello')

