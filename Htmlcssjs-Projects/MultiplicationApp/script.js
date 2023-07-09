const questionElement = document.getElementById("question");

const num1 = Math.random()*20;
const num2 = Math.random()*10;

function updateQuestion(){
    questionElement.innerHTML = `What is ${num1.toFixed(0)} multiply by ${num2.toFixed(0)}?`;
}
updateQuestion();


const scoreElement = documet.getElementById("score");

const inputElement = document.getElementById("input");

if (inputElement.innerText == "5"){
    scoreElement.innerHTML = `Score = ${5}`;
}
else{
    scoreElement.innerHTML = "";
    scoreElement.innerHTML = `Score = -1`;
}