document.addEventListener('DOMContentLoaded', function() {
    const hiddenContent = document.querySelector('.hidden_stuff');

    // Define the functions used in HTML onclick
    window.showBotCount = function() {
        hiddenContent.classList.add('show');
    }

    window.hideBotCount = function() {
        hiddenContent.classList.remove('show');
        window.location.href = '../Game/game.html?bots=$0';
    }

    window.submitBot = function() {
        const numBots = document.getElementById('number-of-bots').value;
        window.location.href = `../Game/game.html?bots=${numBots}`;
    }
});