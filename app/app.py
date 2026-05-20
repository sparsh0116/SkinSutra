import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from PIL import Image
from src.predict import predict

# PAGE CONFIG
st.set_page_config(page_title="Skin AI Detector", layout="wide")

#  HEADER
st.title("🧴 Skin Disease AI Detector")
st.markdown("AI-based skin disease prediction with medical insights")

st.divider()

#DISEASE INFO + PRECAUTIONS + CANCER STATUS
disease_data = {
    "Actinic Keratosis": {
        "info": "A rough, scaly patch caused by sun damage. Considered pre-cancerous.",
        "precautions": "Use sunscreen regularly, avoid excessive sun exposure, consult dermatologist.",
        "cancer": True
    },
    "Basal Cell Carcinoma": {
        "info": "Most common type of skin cancer, usually slow growing.",
        "precautions": "Seek medical treatment early, avoid UV exposure, regular skin checkups.",
        "cancer": True
    },
    "Benign Keratosis": {
        "info": "Non-cancerous skin growth.",
        "precautions": "Generally harmless, but monitor for changes and consult doctor if needed.",
        "cancer": False
    },
    "Dermatofibroma": {
        "info": "Harmless skin nodule.",
        "precautions": "No treatment needed usually, consult if painful or changing.",
        "cancer": False
    },
    "Melanoma": {
        "info": "Serious and aggressive skin cancer.",
        "precautions": "Immediate medical attention required, avoid sun, regular screening.",
        "cancer": True
    },
    "Nevus": {
        "info": "Common mole, usually harmless.",
        "precautions": "Monitor size/color changes, use sun protection.",
        "cancer": False
    },
    "Vascular Lesion": {
        "info": "Blood vessel abnormality.",
        "precautions": "Usually harmless, consult if it grows or bleeds.",
        "cancer": False
    }
}

# INPUT MODE
input_mode = st.radio("Choose Input Method 👇", ["Upload Image", "Use Camera"])

image = None

if input_mode == "Upload Image":
    uploaded_file = st.file_uploader("📤 Upload Skin Image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")

elif input_mode == "Use Camera":
    camera_image = st.camera_input("📸 Take a picture")
    if camera_image:
        image = Image.open(camera_image).convert("RGB")

# MAIN OUTPUT
if image:
    col1, col2 = st.columns([1, 1])

    # IMAGE
    with col1:
        st.image(image, caption="📷 Input Image", use_column_width=True)

    # PREDICTION
    with col2:
        st.subheader("📊 Prediction Results")

        with st.spinner("Analyzing image..."):
            results = predict(image)

        for i, (label, confidence) in enumerate(results):
            st.markdown(f"### {i+1}. {label}")
            st.progress(int(confidence * 100))
            st.write(f"Confidence: {confidence:.2f}")

            #  GET DATA
            info = disease_data[label]["info"]
            precautions = disease_data[label]["precautions"]
            cancer = disease_data[label]["cancer"]

            # INFO
            st.info(f"🧠 {info}")

            # PRECAUTIONS
            st.warning(f"⚕️ Precautions: {precautions}")

            # CANCER ALERT
            if cancer:
                st.error("⚠️ This condition may be cancerous. Please consult a doctor.")
            else:
                st.success("✅ This condition is generally non-cancerous.")

            st.markdown("---")

st.divider()

# FOOTER
st.caption("⚠️ This is not a medical diagnosis tool. Always consult a healthcare professional.")