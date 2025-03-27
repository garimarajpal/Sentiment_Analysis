# Sentiment Analysis Web Application using Flask

This is a simple web application built with Flask and `TextBlob` for performing sentiment analysis on user input. The app analyzes text and returns whether the sentiment is positive, negative, or neutral, along with the polarity and subjectivity of the text.

## Features
- Input text and get sentiment analysis results.
- Displays sentiment as Positive, Negative, or Neutral.
- Shows polarity (range of -1 to 1) and subjectivity (range of 0 to 1).
- Styled user interface using custom CSS.

## Requirements
To run this app, you need Python 3.x and the following libraries:

- Flask
- TextBlob

You can install the required dependencies using pip:

```bash
pip install Flask textblob
```

## Setup and Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/sentiment-analysis-flask.git
cd sentiment-analysis-flask
```
## Install Dependencies

Make sure you have `pip` installed and then install the required dependencies:

```bash
pip install -r requirements.txt
```
Alternatively, you can install dependencies individually using:

```bash
pip install Flask textblob
```
## Run the Application

Once the dependencies are installed, run the Flask application:

```bash
python app.py
```
By default, the app will be available at `http://127.0.0.1:5000/`.

## How It Works

- The app displays a simple homepage (`index.html`) with a text input field, styled with the custom CSS from `static/style.css`.
- When the user submits the text, the `result` route handles the POST request and performs sentiment analysis using `TextBlob`.
- The app then displays the results on the `results.html` page, showing:
  - Sentiment (Positive, Negative, Neutral)
  - Polarity (ranges from -1 to 1)
  - Subjectivity (ranges from 0 to 1)

## Folder Structure

The project follows a simple structure:

```php
sentiment-analysis-flask/
│
├── app.py                # Main Flask app
├── static/
│   └── style.css         # Custom CSS file for styling the app
└── templates/
    ├── index.html        # Homepage template
    └── results.html      # Results page template
```

## Styling

The app uses a custom CSS file (`style.css`) located in the `static` folder to style the input form and result display. Feel free to modify `style.css` to customize the look and feel of the app.
