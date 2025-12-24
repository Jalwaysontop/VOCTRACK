from flask import Flask, render_template, request
import os
import joblib
import numpy as np
import librosa
from pathlib import Path
from werkzeug.utils import secure_filename

# --------------------
# Flask setup
# --------------------
app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "svm_model.pkl"
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {"wav", "flac", "mp3"}

# --------------------
# Load trained model
# --------------------
svm_pipeline = joblib.load(MODEL_PATH)

# --------------------
# Utility functions
# --------------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_mfcc(audio_path, sr=16000, n_mfcc=13):
    try:
        audio, sr = librosa.load(audio_path, sr=sr)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
        return np.concatenate([mfcc.mean(axis=1), mfcc.std(axis=1)])
    except Exception as e:
        print("MFCC error:", e)
        return None


def predict_audio(audio_path):
    feat = extract_mfcc(audio_path)
    if feat is None:
        return "Error processing audio", 0.0

    feat = feat.reshape(1, -1)

    probs = svm_pipeline.predict_proba(feat)[0]
    pred_class = np.argmax(probs)

    if pred_class == 1:
        label = "Bonafide (Real Voice)"
        confidence = probs[1] * 100
    else:
        label = "Spoof (Deepfake)"
        confidence = probs[0] * 100

    return label, round(confidence, 2)



# --------------------
# Routes
# --------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None

    if request.method == "POST":
        if "audio" not in request.files:
            result = "No file uploaded"
            return render_template("index.html", result=result)

        file = request.files["audio"]

        if file.filename == "":
            result = "No file selected"
            return render_template("index.html", result=result)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = UPLOAD_DIR / filename
            file.save(file_path)

            result, confidence = predict_audio(file_path)

        else:
            result = "Unsupported file format"

    return render_template(
        "index.html",
        result=result,
        confidence=confidence
    )


# --------------------
# Run app
# --------------------
if __name__ == "__main__":
    app.run(debug=True)
