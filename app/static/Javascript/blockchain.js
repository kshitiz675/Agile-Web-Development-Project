const progressBarFull = document.querySelector('#progressBarFull');
const progressBar = document.querySelector('#progressBar');
const MAX_PAGES = 5
var page = 0;

function progress() {
    page++;
    // progressBarFull.style.width = `${(page/MAX_PAGES) * 100}%`;
    progressBar.style.display = none;
}