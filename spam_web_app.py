import streamlit as st
import joblib

model = joblib.load('model/spam_classifier.pkl')
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')

st.set_page_config(page_title="Spam Detector", layout="centered")
st.title("📩 SMS Spam Detector")
st.write("Enter an SMS message to check if it's spam or ham.")

user_input = st.text_area("Your message:", "")

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)
        result = "🚫 SPAM" if prediction[0] == 1 else "✅ HAM"
        st.success(f"Result: {result}")
