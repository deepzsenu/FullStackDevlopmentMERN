const questionElement = document.getElementById("question");

const num1 = Math.random()*10;
const num2 = Math.random()*10;

function updateQuestion(){
    questionElement.innerHTML = `What is ${num1.toFixed(0)} multiply by ${num2.toFixed(0)}?`;
}
updateQuestion();


const scoreElement = documet.getElementById("score");

const inputElement = document.getElementById("input");

