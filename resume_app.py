import streamlit as st

# Page Config
st.set_page_config(page_title="Resume | Your Name", page_icon="📄", layout="centered")

# Title
st.title("Your Name's Resume")

# --- Contact Info ---
st.header("📞 Contact Information")
st.write("**Email:** your.email@example.com")
st.write("**Phone:** +60 123-456-789")
st.write("**LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")
st.write("**GitHub:** [github.com/yourusername](https://github.com/yourusername)")

# --- Education ---
st.header("🎓 Education")
st.subheader("Degree, University Name (Year - Year)")
st.write("- Relevant coursework, achievements, or thesis title")

# --- Work Experience ---
st.header("💼 Work Experience")
st.subheader("Job Title | Company Name (Year - Year)")
st.write("- Responsibility 1")
st.write("- Responsibility 2")
st.write("- Achievement 1")

st.subheader("Intern | Another Company (Year)")
st.write("- Assisted with XYZ project")
st.write("- Learned ABC skills")

# --- Skills ---
st.header("🛠 Skills")
st.write("- Programming: Python, Java, C++")
st.write("- Tools: Git, Docker, Streamlit")
st.write("- Others: Problem-Solving, Teamwork")

# --- Projects ---
st.header("🚀 Projects")
st.subheader("Portfolio Optimization using Deep Reinforcement Learning")
st.write("Built a model to optimize investment portfolios using DRL techniques.")

st.subheader("Smart Waste Management System")
st.write("Developed IoT-enabled bins with image recognition for waste segregation.")

# --- Achievements ---
st.header("🏆 Achievements")
st.write("- Microsoft Azure AI-900 Certified (2025)")
st.write("- Dean’s List (Year)")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
