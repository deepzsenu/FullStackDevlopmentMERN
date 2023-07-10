const textAreaElement = document.getElementById("textarea");
const totalCounterElement = document.getElementById("total-counter");  
const remaingElement = document.getElementById("remaining-counter");

textAreaElement.addEventListener("keyup", () => {
    // console.log("This is a text area");
    updateCounter()
})

function updateCounter() {
    totalCounterElement.innerText = textAreaElement.value.length;
    const maxLength  = textAreaElement.getAttribute("maxLength");
    remaingElement.innerText = maxLength -textAreaElement.value.length;
}