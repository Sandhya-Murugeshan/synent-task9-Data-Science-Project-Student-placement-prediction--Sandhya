# Streamlit Deployment
import streamlit as st
import pickle
import numpy as np

def set_bg_from_url(image_url):
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("https://www.thiruvalluvartrust.org/img/project/paceme.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    return bg_style

st.markdown(
    set_bg_from_url("https://www.analytixlabs.co.in/wp-content/uploads/2025/03/Certification-Course-in-Data-Science.webp"),
    unsafe_allow_html=True
)

# 🔥 Optional dark overlay (better readability)
st.markdown("""
<style>
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🎓 Placement Prediction App")

# Inputs
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)

internships = st.selectbox("Internships", ["Yes", "No"])
training = st.selectbox("Training", ["Yes", "No"])
backlog = st.selectbox("Backlog in 5th sem", ["Yes", "No"])
project = st.selectbox("Innovative Project", ["Yes", "No"])
communication = st.slider("Communication Level", 1, 5)
technical = st.selectbox("Technical Course", ["Yes", "No"])

# Convert inputs
def convert(val):
    return 1 if val == "Yes" else 0

input_data = np.array([[
    cgpa,
    convert(internships),
    convert(training),
    convert(backlog),
    convert(project),
    communication,
    convert(technical)
]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Student will be Placed")
    else:
        st.error("Student will NOT be Placed")