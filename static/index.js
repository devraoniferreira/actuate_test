let shortText = document.getElementById("shortmsg");
let shortInput = document.getElementById("shortinput");
let longText = document.getElementById("longmsg");
let longInput = document.getElementById("longinput");
let clickCountText = document.getElementById("clickcountmsg");

window.short = function() {
	const url = shortInput.value;
	fetch("http://localhost:8000/short", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({url: url})
	}).then((response) => {
		response.json().then((data) => {
			shortText.innerHTML = data.short_url;
		})
	})
};

window.long = function() {
	const short_url = longInput.value;
	fetch("http://localhost:8000/long", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({short_url: short_url})
	}).then((response) => {
		response.json().then((data) => {
			longText.innerHTML = data.url;
		})
	})
};

