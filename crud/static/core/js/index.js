document.addEventListener("DOMContentLoaded", function (event) {
	const toggle = document.getElementById("header-toggle"),
		nav = document.getElementById("nav-bar"),
		bodypd = document.getElementById("body-pd"),
		headerpd = document.getElementById("header");

	if (toggle && nav && bodypd && headerpd) {
		toggle.addEventListener("click", () => {
			nav.classList.toggle("nshow"); // show navbar
			nav.classList.toggle("show"); // show navbar
			toggle.classList.toggle("bx-x"); // change icon
			bodypd.classList.toggle("body-pd"); // add padding to body
			headerpd.classList.toggle("body-pd"); // add padding to header
		});
	}

	/* Active link*/
	const linkColor = document.querySelectorAll(".nav_link");

	function colorLink() {
		if (linkColor) {
			linkColor.forEach((l) => l.classList.remove("active"));
			this.classList.add("active");
		}
	}
	linkColor.forEach((l) => l.addEventListener("click", colorLink));

});
