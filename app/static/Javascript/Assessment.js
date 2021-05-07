let currentQuestionId = 1;
const questionBlocks = document.getElementsByClassName('question');
const originalQuestion = document.getElementById(`question-${currentQuestionId}`);
originalQuestion.classList.remove('question-hidden');


function nextQuestion() {
    const currentQuestion = document.getElementById(`question-${currentQuestionId}`);
    currentQuestionId++;
    //If no next question do something
    const nextQuestion = document.getElementById(`question-${currentQuestionId}`);

    currentQuestion.classList.add('question-hidden');
    nextQuestion.classList.remove('question-hidden');



    

}