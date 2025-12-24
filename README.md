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
This project uses the ASVspoof 2019 Logical Access (LA) dataset, a widely accepted benchmark for evaluating voice anti-spoofing and deepfake audio detection systems.
The dataset contains:
  Bonafide (genuine human speech)
  Spoofed speech generated using text-to-speech (TTS) and voice conversion (VC) techniques
Each audio sample is provided in .flac format along with protocol files that specify:
  Speaker identity
  Audio file ID
  Ground-truth label (bonafide or spoof)
The dataset is organized into predefined splits:

Training set – used for model learning
Development set – used for validation and performance evaluation
Evaluation set – reserved for benchmark testing

ASVspoof 2019 LA focuses on logical access attacks, where adversaries attempt to bypass voice authentication systems using synthetic or cloned audio, making it highly relevant for financial security and biometric authentication applications.

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
