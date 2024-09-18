document.getElementById('tweet-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const tweet = document.getElementById('tweet-input').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tweet: tweet })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <div class="sentiment-category">
                <h2>😊 Positive</h2>
                <p id="positive-value">${data.positive}%</p>
            </div>
            <div class="sentiment-category">
                <h2>😐 Neutral</h2>
                <p id="neutral-value">${data.neutral}%</p>
            </div>
            <div class="sentiment-category">
                <h2>😢 Negative</h2>
                <p id="negative-value">${data.negative}%</p>
            </div>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
