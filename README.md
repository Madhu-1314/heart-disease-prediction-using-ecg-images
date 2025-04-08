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

├── app.py                     # Main Streamlit app
├── Densenet169_ECG_Model.h5  # Trained model (loaded from Google Drive if too large)
├── user_credentials.json     # Stores registered doctor login info
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

🚀 How to Run Locally
1. Clone the Repository
git clone https://github.com/YourUsername/heart-disease-prediction-using-ecg-images.git
cd heart-disease-prediction-using-ecg-images

2. Set Up the Environment
pip install -r requirements.txt

3. Download the Model File
If the model .h5 file is not present, download it manually from:

🔗 Google Drive

And place it in the root directory as:
Densenet169_ECG_Model.h5

4. Run the Application
streamlit run app.py

