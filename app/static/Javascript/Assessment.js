
const questionBlocks = document.getElementsByClassName('question');
let currentQuestionId = getInitialQuestionId(questionBlocks[0].id);

const originalQuestion = document.getElementById(`question-${currentQuestionId}`);
originalQuestion.classList.remove('question-hidden');


function nextQuestion() {

    //Extract value of current question
    const currentQuestion = document.getElementById(`question-${currentQuestionId}`);
    currentQuestionId++;
    //If no next question do something
    const nextQuestion = document.getElementById(`question-${currentQuestionId}`);

    currentQuestion.classList.add('question-hidden');
    nextQuestion.classList.remove('question-hidden');

}

function getInitialQuestionId(questionId) {
    return questionId.split('-')[1];

}