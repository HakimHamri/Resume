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
                                    "- Dean’s List 2024\n- Microsoft Azure AI-900 Certified")

# --- Main Page ---
col1, col2 = st.columns([1, 3])

with col1:
    if uploaded_file is not None:
        st.image(uploaded_file, width=200, caption=full_name, output_format="auto")
    else:
        st.image("https://via.placeholder.com/200", width=200, caption=full_name)  # Placeholder if no image

with col2:
    st.title(full_name)
    st.subheader(title)
    st.markdown(f"📧 **Email:** {email} | 📱 **Phone:** {phone}")
    st.markdown(f"🔗 [LinkedIn]({linkedin}) | 💻 [GitHub]({github})")
    st.markdown("---")

# --- Resume Sections ---
st.markdown("## 🎓 Education")
st.info(education)

st.markdown("## 💼 Work Experience")
st.success(experience)

st.markdown("## 🛠 Skills")
st.warning(skills)

st.markdown("## 🚀 Projects")
st.write(projects)

st.markdown("## 🏆 Achievements")
st.write(achievements)

# Footer
st.markdown("---")
st.caption("✨ Modern Resume made with Streamlit ✨")
