import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="🎓 Grade Class Predictor", page_icon="📘")

model = joblib.load('model/classifier.pkl') 

st.title("🎯 Student Grade Classification (A–F)")

age = st.slider("Age", 15, 18, 16)
gender = st.selectbox("Gender", ["Male", "Female"])
ethnicity = st.selectbox("Ethnicity", ["Caucasian", "African American", "Asian", "Other"])
parent_edu = st.selectbox("Parental Education", [
    "None", "High School", "Some College", "Bachelor's", "Higher"
])
study_time = st.slider("📚 Weekly Study Time (hours)", 0, 20, 5)
absences = st.slider("🚫 Absences", 0, 30, 2)
tutoring = st.selectbox("📘 Tutoring Available?", ["No", "Yes"])
parent_support = st.selectbox("👪 Parental Support", [
    "None", "Low", "Moderate", "High", "Very High"
])
extracurricular = st.selectbox("🎭 Extracurricular Activities", ["No", "Yes"])
sports = st.selectbox("🏀 Sports Participation", ["No", "Yes"])
music = st.selectbox("🎵 Music Participation", ["No", "Yes"])
volunteering = st.selectbox("🤝 Volunteering", ["No", "Yes"])

gender = 0 if gender == "Male" else 1
ethnicity_map = {"Caucasian": 0, "African American": 1, "Asian": 2, "Other": 3}
ethnicity = ethnicity_map[ethnicity]
parent_edu = ["None", "High School", "Some College", "Bachelor's", "Higher"].index(parent_edu)
tutoring = 1 if tutoring == "Yes" else 0
parent_support = ["None", "Low", "Moderate", "High", "Very High"].index(parent_support)
extracurricular = 1 if extracurricular == "Yes" else 0
sports = 1 if sports == "Yes" else 0
music = 1 if music == "Yes" else 0
volunteering = 1 if volunteering == "Yes" else 0

input_data = np.array([[age, gender, ethnicity, parent_edu,
                        study_time, absences, tutoring,
                        parent_support, extracurricular, sports,
                        music, volunteering]])

if st.button("🔮 Predict Grade Class"):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    grade_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}
    grade = grade_map[prediction]

    st.subheader(f"📊 Predicted Grade Class: **{grade}**")

    if grade == 'A':
        st.success("🔥 You’re an academic weapon! Keep it up!")
    elif grade == 'B':
        st.info("👍 Solid performance! A little push can get you to the top.")
    elif grade == 'C':
        st.warning("😐 You're doing okay, but there's room to grow.")
    elif grade == 'D':
        st.error("⚠️ You're on thin ice... Time to take action.")
    elif grade == 'F':
        st.error("💀 You've hit rock bottom. Consider getting help or restructuring your study habits.")

    fig, ax = plt.subplots()
    ax.bar(grade_map.values(), probabilities, color='skyblue')
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probability")
    ax.set_title("🔍 Prediction Confidence by Grade Class")
    for i, v in enumerate(probabilities):
        ax.text(i, v + 0.02, f"{v:.2f}", ha='center')
    st.pyplot(fig)
