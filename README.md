# AI-Powered Sentiment Analysis Web Application

## Overview

This project is a fully functional web application that performs sentiment analysis on user-provided text. It leverages an embedded IBM Watson AI library for Natural Language Processing (NLP) to determine if the sentiment of the text is positive, negative, or neutral. The entire application is deployed as a web service using the Flask framework.


## Features

-   **Sentiment Analysis Engine**: Utilizes the Watson NLP library's BERT-based model to classify text as `SENT_POSITIVE`, `SENT_NEGATIVE`, or `SENT_NEUTRAL`.
-   **Web Interface**: A simple and clean front-end built with HTML and Bootstrap that allows users to input text and view the analysis result dynamically.
-   **Flask Backend**: A lightweight web server built with the Flask framework to handle GET requests from the user interface and serve the analysis results.
-   **Robust Error Handling**: Implements logic to gracefully handle invalid text inputs that result in a server-side error (HTTP 500), returning a user-friendly message.
-   **Unit Testing**: Includes a suite of unit tests using Python's `unittest` library to validate the sentiment analysis function's reliability for different inputs.
-   **Code Quality Assurance**: Static code analysis is performed with `pylint` to ensure the codebase adheres to PEP8 coding standards, achieving a 10/10 rating.
-   **Python Packaging**: The core sentiment analysis logic is structured as an importable Python package, making it modular and easy to use.

## Technologies Used

-   **Backend**: Python, Flask
-   **AI/ML**: IBM Watson NLP Library (BERT-based Sentiment Model)
-   **Frontend**: HTML, JavaScript, Bootstrap
-   **Testing**: Unittest
-   **Libraries**: Requests

## Setup and Usage

Follow these instructions to get a local copy up and running.

### Prerequisites

Ensure you have Python 3.11 or later installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/BonyKoshy/sentiment-analysis-project.git](https://github.com/BonyKoshy/sentiment-analysis-project.git)
    cd sentiment-analysis-project
    ```

2.  **Install the required packages:**
    The project requires `requests`, `flask`, and `pylint`. You can install them using pip:
    ```sh
    pip install requests flask pylint
    ```

### Running the Application

1.  Execute the server script from the project's root directory:
    ```sh
    python server.py
    ```
   

2.  Open your web browser and navigate to the following address to use the application:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

### License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
