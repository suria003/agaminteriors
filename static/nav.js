var navbar = document.getElementById("navbar");

var sticky = navbar.offsetTop;

function handleScroll() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}

window.addEventListener("scroll", handleScroll);
