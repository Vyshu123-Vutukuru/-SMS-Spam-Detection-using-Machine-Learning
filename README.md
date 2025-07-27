# -SMS-Spam-Detection-using-Machine-Learning
A simple yet effective machine learning project to classify SMS messages as "spam" or "ham" using the Naive Bayes classifier and TF-IDF vectorization.
# Spam Detection Web App

A Streamlit web app that classifies SMS messages as spam or ham using a Naive Bayes model trained on the SMS Spam Collection dataset.

## Model
Multinomial Naive Bayes with TF-IDF Vectorizer.

## How to use
Just enter a message in the text box and click "Detect" to see if it's spam.

## Built with
- Python
- Scikit-learn
- Streamlit


  To deploy your **Spam Detection app** on **Hugging Face Spaces**, you'll use the **Streamlit app** you've already built.

---

## 🚀 Deploy on Hugging Face Spaces (Step-by-step)

### ✅ 1. **Prepare Your Project Structure**

Make sure your folder has the following:

```
spam-detector-hf/
├── app/
│   └── spam_web_app.py
├── model/
│   ├── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

---

### 🌍 2. **Create a Space on Hugging Face**

1. Go to: [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Choose:

   * **SDK**: `Streamlit`
   * **Repository name**: `spam-detector`
   * **Visibility**: Public or Private

---

### 📤 3. **Push Code to Hugging Face**

You can either upload files manually on the website or use `git` to push:

#### Git Method:

```bash
git lfs install
git clone https://huggingface.co/spaces/YOUR_USERNAME/spam-detector
cd spam-detector

# Copy your project files into this folder
cp -r ../your-local-spam-project/* .

git add .
git commit -m "Initial commit for spam detector app"
git push
```

---

### ✅ Done!

Hugging Face will **automatically install dependencies** and **run your Streamlit app**. You'll get a live link like:

🔗 `https://huggingface.co/spaces/YOUR_USERNAME/spam-detector`

---



