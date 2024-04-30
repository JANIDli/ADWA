function smoothScroll(target) {
    const element = document.querySelector(target);
    window.scrollTo({
        top: element.offsetTop,
        behavior: 'smooth'
    });
}

// app.js

document.addEventListener('DOMContentLoaded', function () {
    changeBg(); 
});

function changeBg() {
    const images = [
        'url("1.jpg")',
        'url("2.jpg")',
        'url("3.jpg")'
    ];

    const home = document.getElementById('home');
    const bg = images[Math.floor(Math.random() * images.length)];
    home.style.backgroundImage = bg;
}
