const data = JSON.parse(localStorage.getItem("sentimentResult"));

if (!data) {
    alert("No data found. Please analyze a tweet first.");
    window.location.href = "/";
} else {
    document.getElementById("positive-value").innerText = data.positive + "%";
    document.getElementById("neutral-value").innerText = data.neutral + "%";
    document.getElementById("negative-value").innerText = data.negative + "%";
}
