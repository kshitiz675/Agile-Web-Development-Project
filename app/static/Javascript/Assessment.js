
const questionBlocks = document.getElementsByClassName('question');
const initialQuestionId = getInitialQuestionId(questionBlocks[0].id);
const lastQuestionId = initialQuestionId + questionBlocks.length -1;
let currentQuestionId = getInitialQuestionId(questionBlocks[0].id);
let resultsObj = loadResultsObj(questionBlocks);
const originalQuestion = document.getElementById(`question-${currentQuestionId}`);
originalQuestion.classList.remove('question-hidden');


function loadResultsObj(questionBlocks) {
    let obj = new Object();
    for(let item of questionBlocks) {
        let questionId = parseInt(item.id.split('-')[1]);
        obj[questionId] = new Array();
        obj[questionId][0] = null;
        obj[questionId][1] = null;
    }
    return obj;
}

function selectAnswer(event) {

    //Get answer and store in results obj
    const target = event.target;
    answerId = parseInt(target.id.split('-')[1]);
    resultsObj[currentQuestionId][0] = answerId;
    resultsObj[currentQuestionId][1] = target.textContent;

    nextQuestion();
}

function nextQuestion() {

    if(currentQuestionId > lastQuestionId) return;
    const currentQuestion = document.getElementById(`question-${currentQuestionId}`);
    if(currentQuestionId == lastQuestionId) {
        currentQuestion.classList.add('question-hidden');
        quizOver = document.getElementById('quiz-over').classList.remove('question-hidden');
        document.getElementById('submit-button').classList.remove('question-hidden');
        currentQuestionId++;

        //Display answers
        const answers = document.getElementById('quiz-answer-summary');
        for(let answerIndex in resultsObj) {

            let answer = resultsObj[answerIndex];
            const answerText = answer[1];
            let childNode = document.createTextNode(answerText);
            answers.appendChild(childNode);
        }

        return;
    }
    
    //Extract value of current question
    const nextQuestion = document.getElementById(`question-${currentQuestionId + 1}`);

    currentQuestionId++;
    
    currentQuestion.classList.add('question-hidden');
    nextQuestion.classList.remove('question-hidden');

}

function previousQuestion() {

    //Clear answer summary
    
    //TO DO Grey out back button
    if(initialQuestionId == currentQuestionId) return;
    if(currentQuestionId > lastQuestionId) {
        document.getElementById('quiz-answer-summary').innerHTML=" ";
        currentQuestionId--;
        const currentQuestion = document.getElementById(`question-${currentQuestionId}`);
        currentQuestion.classList.remove('question-hidden');
        quizOver = document.getElementById('quiz-over').classList.add('question-hidden');
        document.getElementById('submit-button').classList.add('question-hidden');

        return;

    }

    const currentQuestion = document.getElementById(`question-${currentQuestionId}`);
    const prevQuestion = document.getElementById(`question-${currentQuestionId-1}`);
    currentQuestionId--;

    currentQuestion.classList.add('question-hidden');
    prevQuestion.classList.remove('question-hidden');


}
function submit() {
    //Send ajax request
}

function getInitialQuestionId(questionId) {
    return parseInt(questionId.split('-')[1]);

}