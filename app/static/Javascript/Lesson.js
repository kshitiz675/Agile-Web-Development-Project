const progressBarFull = document.querySelector('#progressBarFull');
const progressBar = document.querySelector('#progressBar');
const video = document.querySelector('#video');
const videoCaption = document.querySelector('.video-info');
const first = document.querySelector('.first');
const second = document.querySelector('.second');
const third = document.querySelector('.third');
const MAX_PAGES = 5
var page = 0;
var nextClickCount = 0;

function progress() {
    page++;
    nextClickCount++;
    progressBarFull.style.width = `${(page / MAX_PAGES) * 100}%`;

    video.remove();
    videoCaption.remove();

    if (nextClickCount === 1) {
        var heading = document.createElement("h2");
        var sub = document.createElement("p");
        var text = document.createTextNode("Blockchain");
        var subtext = document.createTextNode("The blockchain stores information across a network of computers which is decentralized. Information is stored in the form of “blocks” which are unique and cannot be altered due to undergoing cryptography. These blocks can be used for recording the transactions made by cryptocurrencies such as Bitcoin.")

        heading.appendChild(text);
        first.appendChild(heading);
        sub.appendChild(subtext);
        first.appendChild(sub);

        var heading2 = document.createElement("h2");
        var sub2 = document.createElement("p");
        var text2 = document.createTextNode("Decentralisation");
        var subtext2 = document.createTextNode("There is no middleman to transactions and operation on the blockchain since the blockchain is a peer-to-peer network of computers that validate each other’s transactions. These validations are done by people known as miners. This is what makes the blockchain decentralized as every block can be accessed from any computer across the network reflecting changes on the go. ");

        heading2.appendChild(text2);
        second.appendChild(heading2);
        sub2.appendChild(subtext2);
        second.appendChild(sub2);
    }

    if (nextClickCount > 1) {
        if (window.confirm("Pressing next will take you to the quiz, are you ready?")) {
            document.location.href = "/assessment/1";
        }
        else {
            nextClickCount = 1;
            page = 1;
        }
    }

}

