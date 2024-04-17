function fetchData() {
    fetch('/parse')
        .then(response => response.json())
        .then(data => {
            const outputDiv = document.getElementById('output');
            outputDiv.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Fetch data initially
fetchData();

// Fetch data every 5 seconds
setInterval(fetchData, 5000);
