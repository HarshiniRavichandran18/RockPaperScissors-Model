from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import random
import cv2

app = Flask(__name__)

model = tf.keras.models.load_model("keras_model.h5", compile=False)

labels = ["Rock", "Paper", "Scissors"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))

    img = img.astype(np.float32)
    img = (img / 127.5) - 1     

    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)
    player = labels[np.argmax(pred)]

    computer = random.choice(labels)

    if player == computer:
        result = "Draw 🤝"
    elif (player=="Rock" and computer=="Scissors") or \
         (player=="Paper" and computer=="Rock") or \
         (player=="Scissors" and computer=="Paper"):
        result = "You Win 🎉"
    else:
        result = "Computer Wins"

    return jsonify({
        "player": player,
        "computer": computer,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
