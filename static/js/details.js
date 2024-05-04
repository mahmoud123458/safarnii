let numAdult = document.getElementById("displayAdult");
let numChild = document.getElementById("displayChild");
let totalP = document.querySelector(".totalPrice");

let valAdult = 1;
function increaseAdult() {
    if (valAdult < 10) {
        valAdult++;
        numAdult.innerHTML = valAdult;
        updateTotalPrice();
    }
}
function decreaseAdult() {
    if (valAdult > 1) {
        valAdult--;
        numAdult.innerHTML = valAdult;
        updateTotalPrice();
    }
}

let valChild = 0;
function increaseChild() {
    if (valChild < 10) {
        valChild++;
        numChild.innerHTML = valChild;
        updateTotalPrice();
    }
}
function decreaseChild() {
    if (valChild > 0) {
        valChild--;
        numChild.innerHTML = valChild;
        updateTotalPrice();
    }
}

function updateTotalPrice() {
    let totalPrice = (valAdult * thePrice) + (valChild * (thePrice / 2)); // Calculate total price
    totalP.innerHTML = `${totalPrice} EG`;
}

// Functions to switch between booking and enquiry forms
function bookFun() {
    document.querySelector("#formEnquiry").classList.remove("show");
    document.querySelector("#formBook").classList.add("show");
    document.querySelector("#bookForm").classList.add("active");
    document.querySelector("#enquiryForm").classList.remove("active");
}

function enquiryFun() {
    document.querySelector("#formBook").classList.remove("show");
    document.querySelector("#formEnquiry").classList.add("show");
    document.querySelector("#bookForm").classList.remove("active");
    document.querySelector("#enquiryForm").classList.add("active");
}

updateTotalPrice(); // Initialize total price
