document.addEventListener('DOMContentLoaded', function() {

    const startButton = document.querySelector('.play_button');
    const aboutButton = document.querySelector('.about_button');

    startButton.addEventListener('click', () => {
        window.location.href = '../Bots/bots.html';
    });

    aboutButton.addEventListener('click', () => {
        window.location.href = '../About/about.html';
    });
});