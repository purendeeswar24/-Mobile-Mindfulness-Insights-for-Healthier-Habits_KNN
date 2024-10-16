import streamlit as st
import numpy as np
import joblib 

# Apply custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 18px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stMarkdown h1 {
        color: #333;
        font-size: 36px;
        text-align: center;
        padding-bottom: 20px;
    }
    .prediction-text {
        font-size: 22px;
        font-weight: bold;
        color: #0b5563;
    }
    </style>
""", unsafe_allow_html=True)

# loading the model
model = joblib.load("logistic.pkl")

# title of the app
st.markdown("<h1>📱 Mobile Mindfulness: Insights for Healthier Habits</h1>", unsafe_allow_html=True)

# user inputs
st.markdown("### Please provide your details:")
user_id = st.number_input("🆔 User ID", min_value=1)
device_model = st.selectbox("📱 Select Your Mobile Device", ["Google Pixel 5", "OnePlus 9", "Xiaomi Mi 11", "iPhone 12", "Samsung Galaxy S21"])
OS = st.selectbox("💻 Select OS", [("Android", 0), ("iOS", 1)])
screen_time = st.number_input("⏳ Mobile usage time in hours", min_value=1, max_value=12)
gender = st.selectbox("👤 Gender", [("Male", 1), ("Female", 0)])
age = st.number_input("🎂 Enter your age", min_value=10, max_value=100)

# assigning the values
device_model_values = {"Google Pixel 5": 0, "OnePlus 9": 1, "Xiaomi Mi 11": 2, "iPhone 12": 3, "Samsung Galaxy S21": 4}[device_model]
os_value = OS[1]  # Extracting the actual OS value from the tuple

# button for prediction
if st.button("🔍 Predict"):
    input_features = [[user_id, device_model_values, os_value, screen_time, gender[1], age]]
    predicted_status = model.predict(input_features)[0]  # Get the single prediction value

    # Custom logic for screen time adjustment
    if 4 <= screen_time <= 6:
        predicted_status = 5
    elif screen_time <= 3:
        predicted_status = 1
    elif screen_time == 0:
        predicted_status = 1

    # Display the prediction
    st.markdown(f"<p class='prediction-text'>📊 Predicted status: {predicted_status}</p>", unsafe_allow_html=True)

    # Result feedback with color-coded output
    if predicted_status <= 2:  # Low usage / Good control
        st.markdown("<p style='color: green; font-size: 20px;'>✅ Great job! You're maintaining a balanced mobile usage. Keep it up!</p>", unsafe_allow_html=True)
    elif 4 <= predicted_status <= 6:  # Mid-range concern
        st.markdown("<p style='color: orange; font-size: 20px;'>⚠️ You're doing okay, but be mindful! You might be on the edge of using your phone too much.</p>", unsafe_allow_html=True)
    else:  # High usage / Possible addiction
        st.markdown("<p style='color: red; font-size: 20px;'>🚨 You might be heading towards mobile addiction. Try to reduce screen time and engage in other activities like reading books.</p>", unsafe_allow_html=True)

# Footer with motivational quote
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>📚 'Unplug and unwind. Life happens outside the screen.' 🌿</p>", unsafe_allow_html=True)
