import streamlit as st

# Page Config
st.set_page_config(page_title="Interactive Resume", page_icon="📄", layout="centered")

st.title("📄 Interactive Resume Builder")

# --- Upload Profile Picture ---
st.sidebar.header("👤 Upload Profile Picture")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, width=200, caption="Profile Picture")

# --- Input Fields ---
st.sidebar.header("✍️ Enter Your Details")

full_name = st.sidebar.text_input("Full Name", "Your Name")
email = st.sidebar.text_input("Email", "your.email@example.com")
phone = st.sidebar.text_input("Phone", "+60 123-456-789")
linkedin = st.sidebar.text_input("LinkedIn", "https://linkedin.com/in/yourprofile")
github = st.sidebar.text_input("GitHub", "https://github.com/yourusername")

education = st.sidebar.text_area("Education", "Degree, University Name, Year")
experience = st.sidebar.text_area("Work Experience", "Job Title, Company Name, Year\n- Responsibility\n- Achievement")
skills = st.sidebar.text_area("Skills", "- Python\n- Java\n- Streamlit")
projects = st.sidebar.text_area("Projects", "Project Name: Description")
achievements = st.sidebar.text_area("Achievements", "- Award / Certification")

# --- Resume Display ---
st.header(full_name)

st.subheader("📞 Contact Information")
st.write(f"**Email:** {email}")
st.write(f"**Phone:** {phone}")
st.write(f"**LinkedIn:** [{linkedin}]({linkedin})")
st.write(f"**GitHub:** [{github}]({github})")

st.subheader("🎓 Education")
st.write(education)

st.subheader("💼 Work Experience")
st.write(experience)

st.subheader("🛠 Skills")
st.write(skills)

st.subheader("🚀 Projects")
st.write(projects)

st.subheader("🏆 Achievements")
st.write(achievements)

st.markdown("---")
st.write("✅ Resume generated with Streamlit")
