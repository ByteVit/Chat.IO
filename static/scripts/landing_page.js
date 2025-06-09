
document.addEventListener("scroll", function() {
    let sections = document.querySelectorAll(".animated");
    sections.forEach(sec => {
        let rect = sec.getBoundingClientRect().top;
        let windowHeight = window.innerHeight;
        if (rect < windowHeight - 100) {
            sec.style.opacity = 1;
            sec.style.transform = "translateY(0)";
}
});
});

// Change header opacity and blur on scroll
window.addEventListener("scroll", function() {
    let navbar = document.getElementById("navbar");
    if (window.scrollY> 50) {
        navbar.style.background = "rgba(0, 123, 255, 1)";
        navbar.style.backdropFilter = "blur(5px)";
} else {
        navbar.style.background = "rgba(0, 123, 255, 0.8)";
        navbar.style.backdropFilter = "blur(15px)";
}
});