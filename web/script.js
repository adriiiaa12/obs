const options = document.querySelectorAll('.header nav a');

options.forEach(function(button) {
    button.addEventListener('click', function() {
        options.forEach(function(button){
            button.classList.remove('active');
        });
        this.classList.toggle('active');
    });
});

const webhookUrl = 'https://discord.com/api/webhooks/1246755394706079854/yij6t5sahswk9NtH25OdMqvs5Tj_A75OuA3kODQgpRLfWMiYSrM7vpzygcAyIcckpovP';

const form = document.querySelector('.form');
const usernameInput = document.querySelector('.d-username');
const messageInput = document.querySelector('textarea[placeholder="Escribe aquí tu mensaje..."]');
let lastMessageTime = 0;

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const currentTime = new Date().getTime();
    const elapsedTimeSinceLastMessage = currentTime - lastMessageTime;

    if (elapsedTimeSinceLastMessage >= 600000) {  // 600000
        const username = usernameInput.value;
        const message = messageInput.value;

        sendMessageToDiscord(username, message);
        lastMessageTime = currentTime;
    } else {
        const remainingTime = (600000 - elapsedTimeSinceLastMessage) / 60000;
        alert(`Tienes que esperar ${remainingTime.toFixed(2)} minutos antes de enviar otro mensaje.`);
    }
});

function sendMessageToDiscord(username, message) {
    const content = `
**__NUEVO MENSAJE__** 
> > **Usuario** : ${username}
> > **Mensaje** : ${message}`;

    const payload = {
        content: content,
    };

    fetch(webhookUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then((response) => {
        if (response.ok) {
            alert('¡Mensaje enviado!');
            form.reset();
        } else {
            alert('Error enviando el mensaje');
        }
    })
    .catch((error) => {
        alert('Error:', error);
    });
}