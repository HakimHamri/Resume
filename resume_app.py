import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Modern Resume", page_icon="📄", layout="wide")

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f0f4ff, #e6faff);
        font-family: 'Segoe UI', sans-serif;
    }
    .main > div {
        padding: 20px;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #004aad;
    }
    .stMarkdown {
        margin-bottom: 15px;
    }
    .resume-card {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .education {background-color: #e8f0fe;}
    .experience {background-color: #e6fffa;}
    .skills {background-color: #fff4e6;}
    .projects {background-color: #fef6e4;}
    .achievements {background-color: #f3e8ff;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Input ---
st.sidebar.title("✍️ Build Your Resume")

uploaded_file = st.sidebar.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])

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
                                    "- Dean’s List 2024\n- Microsoft Azure AI-900 Certified")

# --- Main Layout ---
col1, col2 = st.columns([1, 3])

with col1:
    if uploaded_file is not None:
        st.image(uploaded_file, width=200, caption=full_name, output_format="auto")
    else:
        st.image("https://via.placeholder.com/200", width=200, caption=full_name)

with col2:
    st.title(full_name)
    st.subheader(title)
    st.markdown(f"📧 **Email:** {email} | 📱 **Phone:** {phone}")
    st.markdown(f"🔗 [LinkedIn]({linkedin}) | 💻 [GitHub]({github})")
    st.markdown("---")

# --- Resume Sections with Colors ---
st.markdown("## 🎓 Education")
st.markdown(f"<div class='resume-card education'>{education}</div>", unsafe_allow_html=True)

st.markdown("## 💼 Work Experience")
st.markdown(f"<div class='resume-card experience'>{experience}</div>", unsafe_allow_html=True)

st.markdown("## 🛠 Skills")
st.markdown(f"<div class='resume-card skills'>{skills}</div>", unsafe_allow_html=True)

st.markdown("## 🚀 Projects")
st.markdown(f"<div class='resume-card projects'>{projects}</div>", unsafe_allow_html=True)

st.markdown("## 🏆 Achievements")
st.markdown(f"<div class='resume-card achievements'>{achievements}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("✨ Modern Colorful Resume made with Streamlit ✨")
