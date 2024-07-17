document.getElementById('image-input').addEventListener('change', function() {
    if (this.files.length > 0) {
        document.getElementById('message-input').disabled = true;
        previewImage(this.files[0]);
    } else {
        document.getElementById('message-input').disabled = false;
        document.getElementById('image-preview').innerHTML = ''; 
    }
});

document.getElementById('message-input').addEventListener('input', function() {
    if (this.value.length > 0) {
        document.getElementById('image-input').disabled = true;
        document.getElementById('image-preview').innerHTML = '';
    } else {
        document.getElementById('image-input').disabled = false;
    }
});

function previewImage(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        const imagePreview = document.getElementById('image-preview');
        imagePreview.innerHTML = ''; 
        const img = document.createElement('img');
        img.src = e.target.result;
        img.style.maxWidth = '100px'; 
        img.style.borderRadius = '4px';
        imagePreview.appendChild(img);
    };
    reader.readAsDataURL(file);
}

async function sendMessage(event) {
    event.preventDefault();

    const form = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const imageInput = document.getElementById('image-input');
    const sendButton = document.getElementById('send-button');
    const spinner = document.getElementById('spinner');

    const message = messageInput.value;
    const image = imageInput.files[0];

    const conversation = document.getElementById('conversation');
    const userMessage = document.createElement('p');
    userMessage.className = 'message user-message';
    
    if (image) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100%';
            img.style.borderRadius = '4px';
            userMessage.appendChild(img);
        };
        reader.readAsDataURL(image);
    } else {
        userMessage.textContent = message;
    }

    conversation.appendChild(userMessage);

    const botMessageContainer = document.createElement('p');
    botMessageContainer.className = 'message bot-message';
    const botMessage = document.createElement('span');
   

