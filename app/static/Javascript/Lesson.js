const progressBarFull = document.querySelector('#progressBarFull');
const progressBar = document.querySelector('#progressBar');
const video = document.querySelector('#video');
const videoCaption = document.querySelector('.video-info');
const first = document.querySelector('.first');
const second = document.querySelector('.second');
const third = document.querySelector('.third');
const quizId = document.getElementsByClassName('quiz')[0].id.split('-')[1];
const summary = document.querySelector('.summary');
const MAX_PAGES = 5
var page = 0;
var nextClickCount = 0;

function progress() {

    page++;
    nextClickCount++;
    progressBarFull.style.width = `${(page / MAX_PAGES) * 100}%`;

    video.remove();
    videoCaption.remove();

    summary.style.display = "block";

    if (nextClickCount > 1) {
        if (window.confirm("Pressing next will take you to the quiz, are you ready?")) {
            document.location.href = `/assessment/${quizId}`;
        }
        else {
            nextClickCount = 1;
            page = 1;
        }
    }

}

