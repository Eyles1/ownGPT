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
    botMessageElement.appendChild(span);
    chatMessages.appendChild(botMessageElement);
  }
  
  function getBotResponse(userMessage) {
    // Bot Communication
    var botResponses = ["Hallo!", "Wie kann ich dir helfen?", "Das ist interessant!"];
    var randomIndex = Math.floor(Math.random() * botResponses.length);
    var botResponse = botResponses[randomIndex];
    
    displayBotMessage(botResponse);
  }
  