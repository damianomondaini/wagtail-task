function openNav() {
    document.querySelector(".main-header").classList.add("main-header__animation"), document.getElementById("overlay").style.height = "100%", document.querySelector(".main-header").style.height = "100vh"
}

function closeNav() {
    document.querySelector(".main-header").classList.remove("main-header__animation"), document.getElementById("overlay").style.height = "0", document.querySelector(".main-header").style.height = "80px"
}
null != document.querySelector(".landing__title") && window.fitText(document.querySelectorAll(".landing__title"), .55);
var container, members = document.querySelectorAll(".member-container");

function pop(e) {
    "member-container" === e.path[1].className ? container = e.path[1] : "member-container" === e.path[0].className && (container = e.path[0]), container.style.backgroundColor = "#EF476F", container.firstElementChild.style.display = "block", container.lastElementChild.style.filter = "brightness(50%)"
}

function unpop(e) {
    container.style.backgroundColor = "transparent", container.firstElementChild.style.display = "none", container.lastElementChild.style.filter = "brightness(100%)"
}
for (var i = 0; i < members.length; i++) members[i].addEventListener("mouseleave", unpop), members[i].addEventListener("mouseover", pop);