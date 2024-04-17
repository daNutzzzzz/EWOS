function parseFile() {
    const fileInput = document.getElementById('fileInput');
    const outputDiv = document.getElementById('output');
    
    const file = fileInput.files[0];
    if (!file) {
        outputDiv.innerText = 'Please select a file.';
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/parse', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        outputDiv.innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        outputDiv.innerText = 'Error parsing file.';
        console.error('Error:', error);
    });
}
