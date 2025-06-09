document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("currScr").src = "{{ url_for('chats')}}";
});

function changeScr(scrId) {
    try {
        document.getElementById("currScr").src = `/${scrId}`;
} catch (error) {
        console.log("Error changing screen:", error);
}
}