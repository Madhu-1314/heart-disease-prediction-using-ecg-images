# 🫀 Heart Disease Prediction using ECG Images

This is a Streamlit web application that uses a pre-trained **DenseNet169** deep learning model to predict heart conditions from uploaded ECG images. It features secure user authentication for cardiology department users only.

---

## 🔍 Features

- 🔐 **Login and Registration** for doctors (Cardiology dept. only)
- 🖼 **Upload ECG image** and view predictions
- 📊 Model: DenseNet169 trained on ECG image dataset
- 🧠 Prediction confidence score shown
- 💾 Secure password hashing and user credential storage

---

## 📁 Project Structure
heart-disease-prediction-ecg/ │ ├── app.py # Main Streamlit app ├── Densenet169_ECG_Model.h5 # Trained model (stored via Google Drive) ├── user_credentials.json # Stores registered users ├── requirements.txt # Python dependencies └── README.md # Project documentation
