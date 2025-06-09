function showPswd() {
    let passwordField = document.getElementById("password");
    let toggleBtn = document.getElementById("toggle-btn");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleBtn.innerHTML = "Hide Password";
} else {
        passwordField.type = "password";
        toggleBtn.innerHTML = "Show Password";
}
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("password").type = "password";
});