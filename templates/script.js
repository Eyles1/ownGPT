function sendMessage() {
  var userInput = document.getElementById("user-input");
  var message = userInput.value;
  userInput.value = "";
  
  displayUserMessage(message);
  getBotResponse(message);
}
  
function displayUserMessage(message) {
  var chatMessages = document.getElementById("chat-messages");
  var userMessageElement = document.createElement("div");
  userMessageElement.classList.add("user-message");
  var span = document.createElement("span");
  span.innerText = message;
  userMessageElement.appendChild(span);
  chatMessages.appendChild(userMessageElement);
}
  
function displayBotMessage(message) {
  var chatMessages = document.getElementById("chat-messages");
  var botMessageElement = document.createElement("div");
  botMessageElement.classList.add("bot-message");
  var span = document.createElement("span");
  span.innerText = message;
  var current_date = new Date();
  span.id = String(current_date.getTime());
  botMessageElement.appendChild(span);
  chatMessages.appendChild(botMessageElement);
  return span.id;
}

function getBotResponse(userMessage) {
  // Bot Communication
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/answer");
  xhr.setRequestHeader("Content-Type", "application/json");
  let output_id = displayBotMessage("Thinking ...");
  xhr.onreadystatechange = function (){
    document.getElementById(output_id).innerText = this.response;
  }
  conversation = [];
  for (const msg of document.getElementById("chat-messages").children){
    conversation.push({
      "role": (msg.className == "user-message" ? "user" : "assistant"),
      "content": msg.innerText
    });
  }
  conversation.pop();
  xhr.send(JSON.stringify({"prompt": userMessage, "conversation": conversation}));
}
  