document.getElementById("tweet-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const tweet = document.getElementById("tweet-input").value.trim();

    if (!tweet) {
        alert("Please enter a tweet");
        return;
    }

    const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tweet: tweet })
    });

    const result = await response.json();

    localStorage.setItem("sentimentResult", JSON.stringify(result));
    window.location.href = "/sentiment";
});
