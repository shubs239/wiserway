// Smooth scrolling on page anchors
$(document).ready(function () {
  $("a").on("click", function (event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;

      $("html, body").animate(
        {
          scrollTop: $(hash).offset().top,
        },
        800,
        function () {
          window.location.hash = hash;
        }
      );
    }
  });
});
document.getElementById("summarize-btn").addEventListener("click", function () {
  // Get the input text
  const inputText = document.getElementById("text-input").value;

  // Display the input text in the output container
  document.getElementById("output-text").textContent = inputText;
});
document.getElementById("summarize-btn").addEventListener("click", function () {
  // Get the input text
  const inputText = document.getElementById("text-output").value;

  // Display the input text in the output container
  document.getElementById("output-text").textContent = inputText;
});
var screenSize = "";

function checkScreenSize() {
  if (window.innerWidth < 576) {
    screenSize = "Mobile";
  } else if (window.innerWidth >= 576 && window.innerWidth < 992) {
    screenSize = "Tablet";
  } else {
    screenSize = "Desktop";
  }
  console.log("Screen size:", screenSize);
}

// Call checkScreenSize on page load
checkScreenSize();

// Call checkScreenSize every time the screen size changes
window.addEventListener("resize", checkScreenSize);
function updateClass() {
  const div = document.getElementById("nav");
  if (screenSize === "mobile") {
    div.className = "navbar-mobile";
  } else {
    div.className = "navbar";
  }
}
