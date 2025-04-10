
document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chatForm');
    const messageInput = document.getElementById('messageInput');
    const messageArea = document.getElementById('messageArea');

    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const userMessage = messageInput.value.trim();
        if (userMessage) {
            appendMessage(userMessage, 'user');
            messageInput.value = '';

            
            fetch(chatForm.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new URLSearchParams({
                    'user_input': userMessage
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.response) {
                    appendMessage(data.response, 'bot');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    function appendMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        messageElement.textContent = message;
        messageArea.appendChild(messageElement);
        messageArea.scrollTop = messageArea.scrollHeight;
    }
});
