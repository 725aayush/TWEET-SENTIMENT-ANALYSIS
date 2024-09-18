document.addEventListener('DOMContentLoaded', function() {
    // Assuming these values are dynamically set by some logic or fetched from an API
    const positiveValue = 70; // Example value
    const neutralValue = 20;  // Example value
    const negativeValue = 10; // Example value

    document.getElementById('positive-value').textContent = `${positiveValue}%`;
    document.getElementById('neutral-value').textContent = `${neutralValue}%`;
    document.getElementById('negative-value').textContent = `${negativeValue}%`;
});
