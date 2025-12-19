# 🎤🚫 Voctrack — Deepfake Audio Detection System

**Voctrack** is an intermediate-level machine learning project focused on detecting synthetically generated **deepfake audio**. The system analyzes speech characteristics to differentiate between authentic human recordings and AI-generated voices.

This project was originally designed and implemented during the **AIAmplify Hackathon**, a 24-hour innovation challenge centered on building impactful AI solutions for real-world problems.

---

## 🌟 Project Overview

Voctrack combines **MFCC (Mel-Frequency Cepstral Coefficients)** feature extraction with a **Support Vector Machine (SVM)** classifier to identify subtle spectral differences in speech signals.

By learning the acoustic fingerprints of real versus synthesized speech, the system effectively flags audio generated using modern **Text-to-Speech (TTS)** and voice-cloning models.

---

## 🔬 Scientific Foundation

This implementation is inspired by the following research work:

> **A. Hamza et al.**, *“Deepfake Audio Detection via MFCC Features Using Machine Learning,”* IEEE Access, 2022.

The model is trained and evaluated using the **Fake-or-Real (FoR) dataset**, a widely used benchmark for deepfake audio research. The dataset consists of four curated subsets:

* **for-rece** — Received and processed audio
* **for-2-sec** — Short 2-second audio clips
* **for-norm** — Normalized audio samples
* **for-original** — Raw, original-length recordings

---

## 🚀 Getting Started

### Prerequisites

* Python **3.8 or higher**
* Virtual environment (recommended)

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Jalwaysontop/VOCTRACK.git
cd VOCTRACK
```

#### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage Guide

### 1️⃣ Training the Model

To train the SVM classifier using your own dataset:

* Place **real audio samples** inside `/real_audio`
* Place **deepfake audio samples** inside `/deepfake_audio`

Run the training pipeline:

```bash
python main.py
```

The script will:

* Extract MFCC features
* Normalize and scale the data
* Train the SVM classifier
* Save the trained model and scaler (`.h5` files)

---

### 2️⃣ Audio Analysis via CLI

To analyze a single audio file for deepfake characteristics:

```bash
python analyze_audio.py path/to/sample.wav
```

---

### 3️⃣ Web Interface

For an interactive experience, launch the Flask-based web application:

```bash
python app.py
```

This interface allows users to upload audio files and receive real-time predictions.

---

## 📜 License & Contributions

This project is released under the **MIT License**.

Contributions are welcome!
Feel free to fork the repository and submit pull requests. Please ensure that:

* Each PR includes a clear description of changes
* Proper attribution is maintained when renaming or extending the project

For guidance, refer to a beginner-friendly overview of the MIT License to understand attribution and redistribution requirements.
