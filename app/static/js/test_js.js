let items = document.querySelectorAll(".item"),
	viewer = document.querySelector(".viewer img");
document.querySelector(".viewer .close").onclick = () => {
	document.querySelector("body").classList.toggle("overlayed");
};
items.forEach((item) => {
	item.onclick = () => {
		let content = item.querySelector(".img img");
		viewer.setAttribute("src", content.getAttribute("src"));
		document.querySelector(".viewer .alt").innerHTML = item.querySelector(
			".title"
		).innerHTML;
		document.querySelector("body").classList.toggle("overlayed");
	};
});

["load", "scroll"].forEach((eventName) => {
	window.addEventListener(eventName, (event) => {
		document.querySelectorAll(".fluid-container").forEach((item) => {
			if (isScrolledIntoView(item)) {
				item.classList.add("inScreen");
			} else {
				item.classList.remove("inScreen");
			}
		});
	});
});
function isScrolledIntoView(el) {
	let rect = el.getBoundingClientRect();
	let elemTop = rect.top;
	let elemBottom = rect.bottom;
	let isVisible = elemTop >= -300 && elemBottom <= screen.height + 300;
	return isVisible;
}