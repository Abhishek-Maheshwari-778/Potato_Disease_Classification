import streamlit as st
import requests
from PIL import Image
import time
import os

# ========================================
# Backend FastAPI endpoint
# ========================================
API_BASE = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
API_URL = f"{API_BASE}/predict"
PING_URL = f"{API_BASE}/ping"

# ========================================
# Streamlit Page Setup
# ========================================
st.set_page_config(
    page_title="Potato Disease Classifier",
    layout="centered",
)

# ========================================
# Custom CSS Styling
# ========================================
st.markdown("""
    <style>
    .main {
        background: linear-gradient(120deg, #e3f2fd, #e8f5e9);
        font-family: 'Segoe UI', sans-serif;
        color: #1a237e;
    }
    .title {
        text-align: center;
        color: #2e7d32;
        font-size: 42px;
        font-weight: bold;
        margin-top: 10px;
    }
    .subtitle {
        text-align: center;
        color:white;
        font-size: 18px;
        margin-bottom: 25px;
    }
    .upload-box {
        background: #ffffff;
        border: 2px dashed #2e7d32;
        border-radius: 12px;
        text-align: center;
        padding: 25px;
        margin-top: 20px;
        transition: 0.3s;
    }
    .upload-box:hover {
        background: #f1f8e9;
    }
    .disease-section {
        background: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-top: 30px;
    }
    .prediction-card {
        background: linear-gradient(145deg, #f5fff7, #ffffff);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
    }
    .footer {
        text-align: center;
        color: white;
        margin-top: 40px;
        font-size: 14px;
    }
    table {
        margin-left: auto;
        margin-right: auto;
        border-collapse: collapse;
        font-size: 15px;
    }
    th, td {
        border: 1px solid #2e7d32;
        padding: 8px 15px;
        text-align: center;
        vertical-align: top;
    }
    th {
        background-color: #2e7d32;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ========================================
# Title 
# ========================================
st.markdown("<h1 class='title'>Potato Disease Classifier</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>This project focuses on detecting and classifying potato plant diseases using Convolutional Neural Networks (CNNs)</p>",
    unsafe_allow_html=True
)




# ========================================
# Backend Connection
# ========================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4 class='title'>Backend Connection</h4>", unsafe_allow_html=True)
def check_backend():
    try:
        res = requests.get(PING_URL, timeout=3)
        if res.status_code == 200:
            return True
    except:
        return False

backend_status = check_backend()
if backend_status:
    st.success("Backend Is Connected Successfully")
else:
    st.error("Backend Not Reachable. Please ensure FastAPI is running on port 8000.")

st.markdown("<hr>", unsafe_allow_html=True)


# ========================================
# Upload Image Section
# ========================================
st.markdown(
    "<p class='subtitle'>Upload a potato leaf image to identify if it's healthy or affected by Early Blight or Late Blight.</p>",
    unsafe_allow_html=True
)
st.markdown("Click to upload or drag and drop")
st.markdown("Supported formats: JPG, PNG, JPEG")
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
# ========================================
# Show Uploaded Image and Predict
# ========================================
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image Preview", use_container_width=True)

    if st.button("Analyze Leaf"):
        if backend_status:
            with st.spinner("Analyzing... Please wait..."):
                try:
                    files = {"file": uploaded_file.getvalue()}
                    response = requests.post(API_URL, files=files)

                    if response.status_code == 200:
                        result = response.json()
                        if "error" in result:
                            st.error(result["error"])
                        else:
                            st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
                            st.subheader("Prediction Result")
                            st.write(f"Disease Type: {result['class']}")
                            st.write(f"Confidence Level: {result['confidence']:.2f}%")

                            progress = st.progress(0)
                            for i in range(int(result['confidence'])):
                                time.sleep(0.01)
                                progress.progress(i + 1)

                            if "healthy" in result["class"].lower():
                                st.success("The leaf appears Healthy.")
                            elif "early" in result["class"].lower():
                                st.warning("Detected Early Blight.")
                            elif "late" in result["class"].lower():
                                st.error("Detected Late Blight.")
                            st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"Server Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Error connecting to API: {e}")
        else:
            st.warning("Cannot predict because backend is not connected.")


# ========================================
# About Potato Diseases Section
# ========================================
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## About Potato Diseases")

# Use local images in "images/" folder
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/healthy.JPG", caption="Healthy Leaf", use_container_width=True)
    st.write("Healthy: Vibrant green leaves without dark spots or lesions.")

with col2:
    st.image("images/early_blight.JPG", caption="Early Blight", use_container_width=True)
    st.write("Early Blight: Caused by Alternaria solani. Shows brown spots with concentric rings.")

with col3:
    st.image("images/late_blight.JPG", caption="Late Blight", use_container_width=True)
    st.write("Late Blight: Caused by Phytophthora infestans. Shows dark, water-soaked spots.")

# ========================================
# Credits & Footer (Centered Table)
# ========================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("## About Project")
st.markdown("""
<div class='footer'>
<table>
    <tr>
        <th>Developed By</th>
        <th>Team Members</th>
        <th>Mentor</th>
        <th>Built With</th>
    </tr>
    <tr>
        <td>Abhishek Maheshwari & Team</td>
        <td style="text-align: left;">
            1. Abhishek Maheshwari<br>
            2. Vaishnavi Gupta<br>
            3. Prateek Gupta<br>
            4. Samina Nooreen<br>
            5. Soni<br>
            6. Purti Singh<br>
            7. Anishka Bhatt<br>
            8. Hemendra Gangwar
        </td>
        <td>Vedant Sir</td>
        <td>FastAPI + Streamlit</td>
    </tr>
</table>
</div>
""", unsafe_allow_html=True)

