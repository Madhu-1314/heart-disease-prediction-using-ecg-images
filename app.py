import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import hashlib
import json
import os

# Load the trained model
MODEL_PATH = "Densenet169_ECG_Model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class names 
class_names = ["AHB", "COVID-19", "HMI", "MI","Normal"]

# File to store user credentials
CREDENTIALS_FILE = "user_credentials.json"

# Load user credentials from a JSON file
def load_user_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            return json.load(f)
    return {}

# Save user credentials to a JSON file
def save_user_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(credentials, f)

# Initialize session state
if "USER_CREDENTIALS" not in st.session_state:
    st.session_state["USER_CREDENTIALS"] = load_user_credentials()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

dept_ids = [121, 122, 123, 124, 125, 126, 127, 128, 129, 130]  # Valid department IDs

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def login_page():
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login", key="login_button_form"):
        if username in st.session_state["USER_CREDENTIALS"] and \
           st.session_state["USER_CREDENTIALS"][username] == hash_password(password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

def register_page():
    st.subheader("Register")
    new_username = st.text_input("Choose a Username", key="reg_user")
    department = st.selectbox("Department", ["Cardiology", "Other"])
    dept_id = st.text_input("Enter your ID", key="reg_id")
    new_password = st.text_input("Choose a Password", type="password", key="reg_pass")

    if st.button("Register", key="register_button_form"):
        if new_username in st.session_state["USER_CREDENTIALS"]:
            st.error("Username already exists. Choose a different one.")
        elif department != "Cardiology":
            st.error("Sorry! You can't have access to this system.")
        elif not dept_id.isdigit() or int(dept_id) not in dept_ids:
            st.error("Invalid department ID. You can't have access to this system.")
        else:
            st.session_state["USER_CREDENTIALS"][new_username] = hash_password(new_password)
            save_user_credentials(st.session_state["USER_CREDENTIALS"])
            st.success("Registration successful! Please log in.")
            st.rerun()

def main_app():
    
    # Custom CSS for styling
    st.markdown("""
        <style>
            .main {background-color: #f4f4f4;}
            h1 {color: #007bff; text-align: center;}
            .stButton>button {background-color: crimson; color: white; font-size: 18px; padding: 10px;}
            .stImage {display: flex; justify-content: center;}
            .prediction {font-size: 24px; font-weight: bold; color: #28a745; text-align: center;}
        </style>
    """, unsafe_allow_html=True)
    
    st.write("Upload an ECG image to classify the heart condition.")
    
    uploaded_file = st.file_uploader("Choose an ECG Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image_display = Image.open(uploaded_file)
        st.image(image_display, caption="Uploaded ECG Image", use_column_width=True)

        img = image_display.resize((224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions)
        confidence = predictions[0][predicted_class] * 100

        # Display prediction result
        st.markdown(f"<p class='prediction'>Predicted Class: {class_names[predicted_class]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='prediction'>Confidence: {confidence:.2f}%</p>", unsafe_allow_html=True)


# Main layout
st.title("Welcome to ECG Disease Prediction System")

if not st.session_state["logged_in"]:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign In", key="signin_button_main"):
            st.session_state["show_login"] = True
            st.session_state["show_register"] = False
    with col2:
        if st.button("Register", key="register_button_main"):
            st.session_state["show_register"] = True
            st.session_state["show_login"] = False


    if st.session_state.get("show_login", False):
        login_page()
    elif st.session_state.get("show_register", False):
        register_page()
    
else:
    # Logout button
    if st.button("Logout", key="logout_button"):
        st.session_state["logged_in"] = False
        st.session_state["show_login"] = False
        st.session_state["show_register"] = False
        st.session_state["username"] = ""
        st.rerun()
    main_app()
