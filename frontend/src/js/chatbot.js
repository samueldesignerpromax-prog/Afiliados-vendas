let isChatbotOpen = false;

function openChatbot() {
    document.getElementById('chatbot-modal').style.display = 'block';
    isChatbotOpen = true;
}

function closeChatbot() {
    document.getElementById('chatbot-modal').style.display = 'none';
    isChatbotOpen = false;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

async function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Adicionar mensagem do usuário
    addMessage(message, 'user');
    input.value = '';
    
    // Mostrar indicador de digitação
    showTypingIndicator();
    
    try {
        const response = await API.enviarMensagemChatbot(message);
        hideTypingIndicator();
        addMessage(response.resposta, 'bot');
    } catch (error) {
        hideTypingIndicator();
        addMessage('Desculpe, tive um problema. Tente novamente.', 'bot');
    }
}

function addMessage(text, sender) {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.textContent = text;
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function showTypingIndicator() {
    const messagesContainer = document.getElementById('chat-messages');
    const indicator = document.createElement('div');
    indicator.className = 'message bot typing-indicator';
    indicator.id = 'typing-indicator';
    indicator.innerHTML = '<span>.</span><span>.</span><span>.</span>';
    messagesContainer.appendChild(indicator);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function hideTypingIndicator() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.remove();
    }
}
