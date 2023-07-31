
const num1 = Math.ceil(Math.random()*10);
const num2 = Math.ceil(Math.random()*10);

const questionElement = document.getElementById("question");
questionElement.innerHTML = `What is ${num1} multiply by ${num2}?`;

const correctAns= num1*num2;

let score = JSON.parse(localStorage.getItem('score'));

if(!score){
    score = 0;
}

const inputElement = document.getElementById("input");
// Add event listener to the form and get the data from the form
const formElement = document.getElementById("form");

formElement.addEventListener("submit", () => {
    const userAnswer = +inputElement.value;
    if (userAnswer == correctAns) {
        score++;
        console.log(score);
        updateLocalStorage();
    }
    else{
        score--;
        console.log(score);
        updateLocalStorage();
    }
})

// saving  score to local storage.
function updateLocalStorage(){
    localStorage.setItem("score", JSON.stringify(score));
}

const scoreElement = document.getElementById("score");

scoreElement.innerHTML = `Score = ${score}`;
