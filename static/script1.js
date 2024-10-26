// script.js

function loadPage(page) {
    fetch(`/${page}`)  // Fetch the content from the server
    .then(response => response.text())  // Get the HTML content
    .then(html => {
        document.getElementById('dynamic-content').innerHTML = html;  // Replace the content in the div
    })
    .catch(error => console.error('Error loading page:', error));
}
function chhat()
{
    window.location.href = "chatbot.html"
}

function submitForm() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (email && password) {
        // Redirecting to the summary page after form submission (you can modify this as needed)
        window.location.href = "./Templates/summary.html";
    } else {
        alert("Please enter both email and password.");
    }
}