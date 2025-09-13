### Health Management APP
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("❌ Google API key not found. Please check your .env file.")

# Function to load Gemini response
def get_gemini_response(prompt, user_text, image):
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content([prompt, user_text, image[0]])
    return response.text

# Handle uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
    return None

# Prompt template
input_prompt = """
    You are an expert nutritionist. Analyze the uploaded food image and
    calculate the total calories. Provide details in the format:
    1. Item 1 - X calories
    2. Item 2 - Y calories
    ----
    Total: Z calories
"""

# Streamlit app settings
st.set_page_config(page_title="AI Nutritionist", page_icon="🥗", layout="wide")

st.header("🥑 AI Nutritionist APP")
user_input = st.text_input("Optional Note / Context (e.g., portion size): ", key="input")

uploaded_file = st.file_uploader("📷 Upload a food image...", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

if st.button("Tell me the total calories"):
    image_data = input_image_setup(uploaded_file)

    if not image_data:
        st.error("⚠️ Please upload an image before analyzing.")
    else:
        with st.spinner("Analyzing image..."):
            response = get_gemini_response(input_prompt, user_input, image_data)
            st.subheader("✅ Result")
            st.write(response)
