# 👨‍⚕️ AI Nutritionist App

An AI-powered Health Management application built with **Streamlit** and **Google Gemini API** that helps users analyze food images to estimate **calories** and **classify food items**.  

## 🚀 Features
- 📷 Upload food images (JPG, JPEG, PNG)  
- 🤖 Analyze food items using **Google Gemini multimodal model**  
- 🔢 Estimate total calories with detailed breakdown  
- 🍎 Classify food into categories (fruits, vegetables, protein, grains, desserts, etc.)  
- 💡 Option to provide additional context (e.g., portion size)  

---

## 🛠️ Tech Stack
- [Python 3.10+](https://www.python.org/downloads/)  
- [Streamlit](https://streamlit.io/) – UI framework  
- [Google Gemini API](https://ai.google.dev/gemini-api) – AI model for image + text understanding  
- [Pillow (PIL)](https://pypi.org/project/Pillow/) – Image processing  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Manage API keys securely  

---

## 📂 Project Structure
```
AI_Nutritionist_App/
    │── app.py # Main Streamlit app
    │── .env # Environment variables
    |    (contains GOOGLE_API_KEY)
    │── requirements.txt # Python dependencies
    │── README.md # Project documentation
```


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/22MH1A42G1/AI_Nutritionist_App.git
   cd AI_Nutritionist_App
   ```

2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate   # For Linux/Mac
    source venv\Scripts\activate # For Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**

- Create a .env file in the root folder and add your Google Gemini API key:
    ```.env
    GOOGLE_API_KEY=your_api_key_here
    ```

5. **Run the app**
    ```bash
    python -m streamlit run app.py
    ```

## 📌 Usage

- Open the app in your browser (default: http://localhost:8501).

- Choose a task:

    1. Calorie Estimation → Get calorie breakdown of detected food items.

    2. Food Classification → Classify food into categories.

- Upload a food image.

- (Optional) Provide additional notes (e.g., portion size).

- Click Analyze → Get AI-powered insights.

### 🧩 Example Output

Input: Uploaded image of rice, chicken curry, and salad.

Output:

1. Rice (1 cup) - 200 calories
2. Chicken Curry - 350 calories
3. Salad - 80 calories
----
Total: 630 calories

## ✅ To-Do / Future Enhancements

- 📊 Daily calorie tracker (using st.session_state)

- 🥗 Personalized health recommendations

- 📅 Meal logging & nutrition history

- ⚡ Deploy to Streamlit Cloud / Hugging Face Spaces

---

# 👨‍💻 Author 
Developed by **Indana Aditya**

🌐 [LinkedIn](https://www.linkedin.com/in/aditya-indana-899734216)

💻 [GitHub](https://github.com/22MH1A42G1)



