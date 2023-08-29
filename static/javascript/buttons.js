var downloadButton = document.getElementById('downloadButton');
if (downloadButton) {
    downloadButton.addEventListener('click', function() {
        const confirmed = window.confirm('Are you sure you want to download a 100Mb file?');
        if (confirmed) {
            window.location.href = "/static/downloads/artillery_war_game.zip";
        }
    });
}

function carouselControl(prevButtonId, nextButtonId, carouselClass) {
    var currentSlide = 0;
    var slides = document.querySelectorAll('.' + carouselClass);

    // Check if prevButton exists before attaching event
    var prevButton = document.getElementById(prevButtonId);
    if (prevButton) {
        prevButton.addEventListener("click", function() {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
        });
    }

    // Check if nextButton exists before attaching event
    var nextButton = document.getElementById(nextButtonId);
    if (nextButton) {
        nextButton.addEventListener("click", function() {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        });
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Check if any slide of carousel1 exists
    if (document.querySelector('.carousel1')) {
        carouselControl("prevBtn", "nextBtn", "carousel1");
    }

    // Check if any slide of carousel2 exists
    if (document.querySelector('.carousel2')) {
        carouselControl("prevBtn2", "nextBtn2", "carousel2");
    }
});
