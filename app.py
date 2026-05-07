import os
import numpy as np
from flask import Flask, render_template, request
import random
from io import BytesIO
import base64

app = Flask(__name__)

# Simple decision tree based on random features
def simple_decision_tree(features):
    """
    Simple decision tree for mock cancer detection prediction.
    Based on random features and threshold values.
    """
    threshold_1 = 0.5 # Random threshold for feature 1
    threshold_2 = 0.6  # Random threshold for feature 2

    # Decision tree logic (simplified)
    if features[0] > threshold_1 and features[1] > threshold_2:
        # Cancer Detected
        prediction = "Cancer Detected"
        confidence = random.uniform(50, 100)  # Confidence between 50 and 100 for Cancer
    else:
        # No Cancer Detected
        prediction = "No Cancer Detected"
        confidence = random.uniform(0, 50)  # Confidence between 0 and 50 for Non-Cancer

    return prediction, confidence

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    image_path = None

    if request.method == "POST":
        if "image" not in request.files:
            result = "No image uploaded"
        else:
            file = request.files["image"]

            if file.filename == "":
                result = "No image selected"
            else:
                try:
                    # Use random features (not processing the image here)
                    random_features = [random.random(), random.random()]  # Random features for testing

                    # Use the decision tree for prediction
                    result, confidence = simple_decision_tree(random_features)

                    # Predict based on confidence
                    if confidence > 50:
                        result = "Cancer Detected"
                    else:
                        result = "No Cancer Detected"

                    # Convert image to base64 for display without saving to static
                    buffered = BytesIO()
                    file.save(buffered)
                    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                    image_path = "data:image/jpeg;base64," + img_str

                except Exception as e:
                    result = f"Prediction error: {str(e)}"

    return render_template("index.html", result=result, confidence=confidence, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)