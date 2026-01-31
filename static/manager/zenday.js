const days = document.querySelectorAll(".zenday-day");
let index = [...days].findIndex(d => d.classList.contains("today"));

function scrollDay(step) {
    index = Math.max(0, Math.min(days.length - 1, index + step));
    days[index].scrollIntoView({ behavior: "smooth", block: "start" });
}

// Auto-focus TODAY
window.onload = () => {
    if (index >= 0) {
        days[index].scrollIntoView({ behavior: "smooth", block: "start" });
    }
};
