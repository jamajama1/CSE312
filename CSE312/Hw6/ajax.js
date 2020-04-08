/* var js = [];
count = 0;
change = 0;
function sendMessage(){
    const box = document.getElementById("chatInput");
    const message = box.value;
    box.value = " ";
    const request = new XMLHttpRequest();
    request.onreadystatechange	=	function(){	
        if	(this.readyState	===	4	&&	this.status	===	200){	
                        console.log(this.responseText);		
        }	
    };	

    let chat = document.getElementById("messages");
    chat.innerHTML = message;
    request.open("POST", "send-message");
    //const messageObject = {"message": message};
    request.send(message);
    //message.focus();
}

function getData(){
    for (i = 0; i <js.length; i++){
        var addChat = document.createElement("P");             
        addChat.innerText = js[i];       
        document.body.appendChild(addChat);
    }
}

// function getJSON(){
//     const req = new XMLHttpRequest();
//     req.open("GET", "/aajson");
//     req.send();
//     change++;
//     console.log(req);
//     var mess =req.responseText;
//     var addChat = document.createElement("P"); 
//     addChat.innerText = mess;               
//     document.body.appendChild(addChat);
// }

function getMessages(){
    const request = new XMLHttpRequest();
    request.open("GET", "/json");
    request.send();	
    request.onreadystatechange	=	function(){	
        if	(this.readyState	===	4	&&	this.status	===	200){	
            renderMessage(request.responseText);
            console.log(request.responseText);
        }	
    };
}

function renderMessage(msg){
    let chat = document.getElementById("messages");
    chat.innerHTML = msg;
    //setInterval(getMessages(), 1000);
}

const socket = new WebSocket('ws://' + window.location.host + '/socket');


 */

let socket = new WebSocket('ws://' + window.location.host + '/socket');
socket.onmessage = renderMessages;
var username = "jama"
function sendMessage() {
    const box = document.getElementById("chatInput");
    const message = box.value;
 socket.send(JSON.stringify({'username': username, 'message': message}))
}
function renderMessages(message) {
 console.log(message.data);
}