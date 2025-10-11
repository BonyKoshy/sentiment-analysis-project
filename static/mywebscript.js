function runSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const resultDisplay = document.getElementById("result-display");
    const loadingSpinner = document.getElementById("loading-spinner");

    // Check if input is empty
    if (!textToAnalyze.trim()) {
        resultDisplay.innerHTML = "Please enter some text to analyze.";
        resultDisplay.className = "result-error";
        resultDisplay.style.display = "block";
        return;
    }

    // Show spinner and hide previous results
    loadingSpinner.style.display = "block";
    resultDisplay.style.display = "none";

    // Use modern Fetch API to make the request
    fetch(`sentimentAnalyzer?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            // Hide spinner
            loadingSpinner.style.display = "none";

            // Display the result
            resultDisplay.innerHTML = data;
            resultDisplay.style.display = "block";
            
            // Apply style based on sentiment
            const lowerCaseData = data.toLowerCase();
            if (lowerCaseData.includes("positive")) {
                resultDisplay.className = "result-positive";
            } else if (lowerCaseData.includes("negative")) {
                resultDisplay.className = "result-negative";
            } else if (lowerCaseData.includes("neutral")) {
                resultDisplay.className = "result-neutral";
            } else {
                resultDisplay.className = "result-error";
            }
        })
        .catch(error => {
            // Hide spinner and show error message
            loadingSpinner.style.display = "none";
            resultDisplay.innerHTML = "An error occurred while analyzing the text. Please try again.";
            resultDisplay.className = "result-error";
            resultDisplay.style.display = "block";
            console.error('Error:', error);
        });
}