const progressBarFull = document.querySelector('#progressBarFull');
const progressBar = document.querySelector('#progressBar');
const video = document.querySelector('#video');
const videoCaption = document.querySelector('.video-info')
const MAX_PAGES = 5
var page = 0; 
var nextClickCount = 0;


function progress() {
    page++;
    nextClickCount++;
    progressBarFull.style.width = `${(page / MAX_PAGES) * 100}%`;

    video.remove();
    videoCaption.remove();

    

}