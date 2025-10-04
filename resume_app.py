import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Beautiful Resume", page_icon="✨", layout="wide")

# --- Custom CSS for Modern Design ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-container {
        padding: 25px;
    }
    .profile-pic {
        border-radius: 50%;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        margin-bottom: 15px;
    }
    h1 {
        font-size: 42px;
        font-weight: bold;
        color: #2c3e50;
    }
    h2 {
        font-size: 28px;
        margin-top: 30px;
        color: #004aad;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .highlight {
        color: #16a085;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Input ---
st.sidebar.title("🖊️ Customize Your Resume")

uploaded_file = st.sidebar.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
full_name = st.sidebar.text_input("Full Name", "Muhammad Hakim")
title = st.sidebar.text_input("Title", "IT Student | Cloud & AI Enthusiast")
email = st.sidebar.text_input("Email", "your.email@example.com")
phone = st.sidebar.text_input("Phone", "+60 123-456-789")
linkedin = st.sidebar.text_input("LinkedIn", "https://linkedin.com/in/yourprofile")
github = st.sidebar.text_input("GitHub", "https://github.com/yourusername")

education = st.sidebar.text_area("🎓 Education", "Bachelor of IT, Universiti Malaysia Kelantan (2023 - 2027)")
experience = st.sidebar.text_area("💼 Work Experience", 
    "Intern | Company Name (2024)\n- Assisted with cloud deployment\n- Built automation scripts")
skills = st.sidebar.text_area("🛠 Skills", "Python, Flutter, Streamlit, Azure AI, Git")
projects = st.sidebar.text_area("🚀 Projects", 
    "Metawarisan App: NFT + Digital Heritage Marketplace\nSmart Waste Management System: IoT Bins with AI Recognition")
achievements = st.sidebar.text_area("🏆 Achievements", "- Dean’s List 2024\n- Microsoft Azure AI-900 Certified")

# --- Main Layout ---
col1, col2 = st.columns([1, 3])

with col1:
    if uploaded_file:
        st.image(uploaded_file, width=200, caption=full_name, output_format="auto", use_container_width=False)
    else:
        st.image("https://via.placeholder.com/200", width=200, caption=full_name)
    
with col2:
    st.markdown("<h1>" + full_name + "</h1>", unsafe_allow_html=True)
    st.markdown(f"**<span class='highlight'>{title}</span>**", unsafe_allow_html=True)
    st.markdown(f"📧 {email} | 📱 {phone}") 
    st.markdown(f"🔗 [LinkedIn]({linkedin}) | 💻 [GitHub]({github})")
    st.markdown("---")

# --- Resume Sections ---
st.markdown("## 🎓 Education")
st.markdown(f"<div class='card'>{education}</div>", unsafe_allow_html=True)

st.markdown("## 💼 Work Experience")
st.markdown(f"<div class='card'>{experience}</div>", unsafe_allow_html=True)

st.markdown("## 🛠 Skills")
st.markdown(f"<div class='card'>{skills}</div>", unsafe_allow_html=True)

st.markdown("## 🚀 Projects")
st.markdown(f"<div class='card'>{projects}</div>", unsafe_allow_html=True)

st.markdown("## 🏆 Achievements")
st.markdown(f"<div class='card'>{achievements}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🌟 Beautiful Resume created with Streamlit 🌟")
