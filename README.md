# AI Stone • Paper • Scissors

AI Stone • Paper • Scissors is a Flask-based web application that uses a TensorFlow Keras model trained with Google Teachable Machine to recognize hand gestures in real time. The player shows a Rock, Paper, or Scissors gesture to the webcam and competes against the computer.

## Features

- Real-time Rock, Paper, and Scissors gesture recognition
- Live webcam integration
- AI model trained using Google Teachable Machine
- Random computer opponent
- Automatic winner detection
- Live score tracking
- Responsive and simple web interface

## Requirements

- Python 3.11
- Webcam-enabled device
- Modern web browser (Chrome or Edge recommended)

## Installation

Create a virtual environment:

```bash
py -3.11 -m venv venv
```

Activate it:

```bash
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Allow camera access when prompted.

## How to Play

1. Launch the application.
2. Allow webcam permission.
3. Show your hand gesture inside the camera frame.
4. Click **PLAY**.
5. The AI predicts your gesture.
6. The computer makes a random choice.
7. The winner and updated score appear instantly.

## Project Structure

```text
StonePaperScissors/
│
├── app.py
├── keras_model.h5
├── labels.txt
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Model Details

The gesture classifier was trained with **Google Teachable Machine** and exported as a **TensorFlow Keras (.h5)** model.

**Recognized Classes**

- Rock
- Paper
- Scissors

The application preprocesses webcam images by converting them to **224 × 224 RGB** format and normalizing pixel values before prediction.

## Troubleshooting

### Webcam is not opening

- Allow camera permission in your browser.
- Make sure no other application is using the webcam.
- Run the app through Flask (`127.0.0.1:5000`) instead of opening the HTML file directly.

### Incorrect gesture prediction

- Keep your full hand inside the camera frame.
- Use good lighting and avoid dark backgrounds.
- Hold the gesture steady for a moment before pressing **PLAY**.
- If needed, retrain the Teachable Machine model with more diverse images.

## Author

**Harshini K R**
