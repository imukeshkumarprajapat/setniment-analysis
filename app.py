# # app.py
# import streamlit as st
# import pickle

# # --- Load saved artifacts ---
# @st.cache_resource
# def load_model_and_vectorizer():
#     model = pickle.load(open("logistic_model.pkl", "rb"))
#     vectorizer = pickle.load(open("bow.pkl", "rb"))
#     return model, vectorizer

# model, vectorizer = load_model_and_vectorizer()

# # --- Streamlit UI ---
# st.set_page_config(page_title="Emotion Classifier", page_icon="🎬", layout="centered")

# st.title("🎭 Emotion Classification App")
# st.write("अपना टेक्स्ट डालिए और मॉडल बताएगा कि उसमें कौन-सी emotion है।")

# # User input
# user_text = st.text_area("टेक्स्ट लिखें:", "")

# if st.button("Predict"):
#     if user_text.strip() == "":
#         st.warning("कृपया कोई टेक्स्ट डालें।")
#     else:
#         # Transform input
#         vectorized = vectorizer.transform([user_text])
#         # Predict
#         prediction = model.predict(vectorized)[0]
#         st.success(f"Predicted Emotion: **{prediction}**")
# app.py
import streamlit as st
import pickle

# --- Load saved artifacts ---
@st.cache_resource
def load_model_and_vectorizer():
    model = pickle.load(open("logistic_model.pkl", "rb"))
    vectorizer = pickle.load(open("bow.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# --- Streamlit UI ---
st.set_page_config(
    page_title="Emotion Classifier",
    page_icon="🎬",
    layout="centered"
)

# Modern header
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2em;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
    }
    .sub-text {
        font-size: 1.1em;
        color: #555;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🎭 Emotion Classification App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Enter your text and let the model detect the emotion.</div>', unsafe_allow_html=True)

# User input
user_text = st.text_area("📝 Write your text here:", placeholder="Type something...")

# Prediction button
if st.button("🔍 Predict Emotion"):
    if user_text.strip() == "":
        st.warning("⚠️ Please enter some text before predicting.")
    else:
        # Transform input
        vectorized = vectorizer.transform([user_text])
        # Predict
        prediction = model.predict(vectorized)[0]

        # Display result
        st.success(f"✨ Predicted Emotion: **{prediction}**")