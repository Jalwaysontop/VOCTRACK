# 🎧 Voctrack – Deepfake Audio Detection System

Voctrack is a machine learning–based **voice anti-spoofing system** that detects **synthetic and deepfake audio** using classical signal processing and supervised learning techniques.  
The system is trained on the **ASVspoof 2019 Logical Access (LA)** dataset and deployed as a **Flask web application** for real-time inference.

---

## 🚀 Key Features

- 🎙️ Detects **deepfake / synthetic voices**
- 📊 Trained on **ASVspoof 2019 (LA)** benchmark dataset
- 🧠 Uses **MFCC features + SVM (RBF kernel)**
- 🌐 Flask-based web interface for audio upload
- 📈 Provides **prediction confidence**
- 🛡️ Designed for **financial & voice-authentication systems**

---

## 🧠 Technical Overview

### 🔹 Dataset
- **ASVspoof 2019 – Logical Access (LA)**
- Binary classification:
  - `Bonafide` → Real human voice
  - `Spoof` → AI-generated / cloned voice

### 🔹 Feature Engineering
- Audio resampled to **16 kHz**
- **MFCC (13 coefficients)**
- Mean + Standard Deviation
- Final feature vector: **26 dimensions**

### 🔹 Model
- **Support Vector Machine (SVM)**
- Kernel: `RBF`
- Feature scaling via `StandardScaler`
- Probabilistic output enabled

### 🔹 Performance
- ~**90–92% accuracy** on development set
- Robust against common logical-access spoofing attacks

---

## 📁 Project Structure

```text
VOCTRACK/
│
├── app.py                     # Flask application
├── requirements.txt
│
├── data/                       # ASVspoof 2019 dataset
│   ├── ASVspoof2019_LA_train/
│   ├── ASVspoof2019_LA_dev/
│   └── ASVspoof2019_LA_cm_protocols/
│
├── training/
│   └── model.ipynb             # Training notebook
│
├── models/
│   └── svm_model.pkl           # Trained model
│
├── templates/
│   └── index.html              # UI
│
├── static/
│   └── logo.png
│
└── uploads/                    # Uploaded audio files
