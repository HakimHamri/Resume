import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Modern Resume", page_icon="📄", layout="wide")

# --- Sidebar Input ---
st.sidebar.title("✍️ Build Your Resume")

# Upload Profile Picture
uploaded_file = st.sidebar.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])

# User Inputs
full_name = st.sidebar.text_input("Full Name", "Muhammad Hakim")
title = st.sidebar.text_input("Headline / Title", "IT Student | AI & Cloud Enthusiast")
email = st.sidebar.text_input("Email", "your.email@example.com")
phone = st.sidebar.text_input("Phone", "+60 123-456-789")
linkedin = st.sidebar.text_input("LinkedIn", "https://linkedin.com/in/yourprofile")
github = st.sidebar.text_input("GitHub", "https://github.com/yourusername")

education = st.sidebar.text_area("🎓 Education", "Bachelor of IT, Universiti Malaysia Kelantan (2023 - 2027)")
experience = st.sidebar.text_area("💼 Work Experience", 
                                  "Intern | Company Name (2024)\n- Assisted with cloud deployment\n- Developed automation scripts")
skills = st.sidebar.text_area("🛠 Skills", "Python, Flutter, Streamlit, Azure AI, Git")
projects = st.sidebar.text_area("🚀 Projects", 
                                "Metawarisan App: NFT + Digital Heritage Marketplace\n"
                                "Smart Waste Management System: IoT Bins with AI Recognition")
achievements = st.sidebar.text_area("🏆 Achievements", 
                                    "-
