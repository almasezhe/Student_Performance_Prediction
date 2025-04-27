
# 🎓 Student Grade Classifier

A machine learning web application that predicts a student's final grade class (A–F) based on behavioral, demographic, and extracurricular activity data.

Built with:
- **Streamlit** for an interactive web interface
- **Scikit-learn** for training and deploying the classification model
- **Matplotlib** for real-time probability visualization

---

## 🚀 Features

- Predicts grade category (A, B, C, D, or F) from 13 student features
- Real-time probability confidence chart
- Personalized feedback based on prediction result
- Clean, responsive Streamlit web UI

---

## 📂 Project Structure

```
/model/
  └── classifier.pkl   # Trained Random Forest model
/app/
  └── streamlit_app.py  # Frontend app
README.md
requirements.txt
```

---

## 📈 Data Inputs

The model uses the following 13 features:
- Age
- Gender
- Ethnicity
- Parental Education Level
- Weekly Study Time
- Number of Absences
- Tutoring (Yes/No)
- Parental Support Level
- Extracurricular Activities (Yes/No)
- Sports Participation (Yes/No)
- Music Participation (Yes/No)
- Volunteering (Yes/No)

---

## 🔮 How It Works

1. User inputs their personal and academic information through the Streamlit app.
2. The trained Random Forest model predicts the final grade class (A–F).
3. The app displays the prediction result along with a probability distribution chart.
4. Personalized motivational feedback is provided based on the predicted class.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/almasezhe/Student_Performance_Prediction.git
cd Student_Performance_Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

---

## 📜 Example Screenshot

![App Screenshot](assets/screenshot.png)

---

## 🛠 Technologies Used

- Python 3.11
- Scikit-learn
- Streamlit
- Matplotlib
- Pandas
- Numpy

---
