document.querySelectorAll(".event").forEach(ev => {
    ev.addEventListener("dragstart", e => {
        e.dataTransfer.setData("text", "event");
        ev.classList.add("dragging");
    });

    ev.addEventListener("dragend", () => {
        ev.classList.remove("dragging");
    });
});

document.querySelectorAll(".hour-row").forEach(row => {
    row.addEventListener("dragover", e => e.preventDefault());
    row.addEventListener("drop", e => {
        const dragging = document.querySelector(".dragging");
        if (dragging) row.appendChild(dragging);
    });
});

/* Keyboard scroll */
document.addEventListener("keydown", e => {
    if (e.key === "ArrowDown") window.scrollBy({top:200, behavior:"smooth"});
    if (e.key === "ArrowUp") window.scrollBy({top:-200, behavior:"smooth"});
});
