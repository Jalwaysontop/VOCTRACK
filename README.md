Voctrack: Deepfake Audio Detection 🎤🚫
Voctrack is an intermediate-level machine learning system designed to identify and flag synthetically generated "Deepfake" audio. This project was originally conceived and developed during the AIAmplify Hackathon, a 24-hour challenge focused on engineering AI solutions for urgent real-world problems.

🌟 Overview
Voctrack leverages MFCC (Mel-frequency cepstral coefficients) feature extraction combined with a Support Vector Machine (SVM) classifier. By analyzing the unique spectral textures of human speech, the system can distinguish between genuine recordings and those generated via advanced text-to-speech (TTS) models.

🔬 Scientific Foundation
This implementation is inspired by the research paper:

A. Hamza et al., "Deepfake Audio Detection via MFCC Features Using Machine Learning," IEEE Access, 2022. Read the Paper

The project utilizes the Fake-or-Real dataset, a benchmark containing four specialized sub-datasets:

for-rece: Received audio.

for-2-sec: Short 2-second clips.

for-norm: Normalized audio samples.

for-original: Raw, original-length samples.

👥 Contributors
Original Developers: Noor Chauhan, Abhishek Khadgi, Omkar Sapkal, Himanshi Shinde, Furqan Ali.

🚀 Getting Started
Prerequisites
Python 3.8+

Virtual Environment (Recommended)

Installation
Clone the Repository:

Bash

git clone https://github.com/your-username/Voctrack.git
cd Voctrack
Setup Environment:

Bash

python -m venv venv
# Windows: venv\Scripts\activate | Linux/macOS: source venv/bin/activate
Install Dependencies:

Bash

pip install -r requirements.txt
🛠️ Usage Guide
1. Training the Model
To train your own SVM model using the local dataset:

Place genuine files in /real_audio and deepfakes in /deepfake_audio.

Run the training engine:

Bash

python main.py
The script will automatically extract MFCCs, scale features, and save the resulting .h5 model and scaler.

2. Analyzing Audio (CLI)
To check a specific file for deepfake markers:

Bash

python analyze_audio.py path/to/sample.wav
3. Launching the Web Interface
For an interactive experience, launch the Flask-based web application:

Bash

python app.py
📜 License & Contribution
This project is released under the MIT License. We welcome forks and pull requests! Please ensure any contributions include a clear description of the new feature or bug fix.

This beginners guide to the MIT license explains how to properly apply and maintain attribution when renaming or forking projects on GitHub.
