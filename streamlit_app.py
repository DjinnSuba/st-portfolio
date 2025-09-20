import streamlit as st
import requests
from PIL import Image
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- Helper function for PDFs ---
def display_pdf(file):
    """Display PDF in Streamlit with iframe (local files only)."""
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- Cache PDF fetch from URLs ---
@st.cache_data
def fetch_pdf(url):
    try:
        return requests.get(url).content
    except Exception:
        return None

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# --- GLOBAL STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
        font-family: "Segoe UI", sans-serif;
    }
    .stButton button {
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
    }
    iframe {
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if selection == "Home":
    st.title("👋 Hi, I'm OdeDjinn Caezar Y. Suba")
    st.write("Welcome to my portfolio website built with Streamlit!")

    # Profile image
    try:
        profile_pic = Image.open("profile.jpg")  
        st.image(profile_pic, caption="This is me!", width=200)
    except FileNotFoundError:
        st.warning("Profile picture not found. Please place 'profile.jpg' in the app folder.")

    # Resume download button
    try:
        with open("CV-Suba, OdeDjinnCaezar.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download My Resume",
                data=pdf_file,
                file_name="CV-Suba, OdeDjinnCaezar.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Resume file not found. Please place 'CV-Suba, OdeDjinnCaezar.pdf' in the app folder.")

    # About Me Section
    st.header("About Me")
    st.markdown("""
        I'm a **Data Analyst x AI Developer** with a passion for creating impactful real-world solutions.
        
        - 🌱 I’m currently working on...
        - 💼 I’ve worked with: **MSCI Inc, UPM IMS-DIG, Remotasks**
        - 📫 Reach me at: [othedjinn@gmail.com](mailto:othedjinn@gmail.com) | 
          [LinkedIn](https://www.linkedin.com/in/caezar-suba-634453161/)
    """)

    # --- Certifications Section ---
    st.header("📜 Certifications & Badges")

    # Badge row
    col1, col2, col3 = st.columns(3)
    for col, (file, caption) in zip(
        [col1, col2, col3],
        [
            ("DS Associate - badge with outline.png", "Data Science Associate Certification"),
            ("cert_streamlit.png", "Streamlit Creator Badge"),
            ("cert_aws.png", "AWS Cloud Practitioner"),
        ],
    ):
        with col:
            try:
                img = Image.open(file)
                st.image(img, caption=caption, use_container_width=True)
            except FileNotFoundError:
                st.warning(f"Missing: {file}")

    # Example list with links
    st.markdown("""
    - 🏆 [Google Data Analytics Certificate](https://www.credly.com/)
    - ☁️ [AWS Cloud Practitioner](https://www.credly.com/)
    - 📊 [Tableau Desktop Specialist](https://www.credly.com/)
    """)

    # Certificate PDFs from GitHub
    certificates = {
        "AI Agent Fundamentals": "https://raw.githubusercontent.com/DjinnSuba/st-portfolio/main/AI_Agent_Fundamentals-certificate.pdf",
        "Building AI Agents with Google ADK": "https://raw.githubusercontent.com/DjinnSuba/st-portfolio/main/Building_AI_Agents_with_Google_ADK-certificate.pdf",
        "Associate Data Scientist": "https://raw.githubusercontent.com/DjinnSuba/st-portfolio/main/DataScienceAssociate-certificate.pdf",
        "Intermediate Python": "https://raw.githubusercontent.com/DjinnSuba/st-portfolio/main/Intermediate_Python-certificate.pdf",
        "Intermediate SQL": "https://raw.githubusercontent.com/DjinnSuba/st-portfolio/main/Intermediate_SQL-certificate.pdf",
        "Introduction to PowerBI": "https://raw.githubusercontent.com/DjinnSuba/st-portfolio/main/Introduction_PowerBI-certificate.pdf",
    }
    
    for name, url in certificates.items():
        with st.expander(f"📖 {name}", expanded=False):
            st.markdown(f"[🔗 Open in Browser]({url})")
            st.markdown(f"""<iframe src="{url}" width="100%" height="500"></iframe>""", unsafe_allow_html=True)

            pdf_data = fetch_pdf(url)
            if pdf_data:
                st.download_button(
                    label=f"📥 Download {name}",
                    data=pdf_data,
                    file_name=f"{name.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )
            else:
                st.warning(f"Could not load {name}.")

# --- PROJECTS PAGE ---
elif selection == "Projects":
    st.title("💼 Projects")
    st.write("Here are some of my featured projects:")

    projects = [
        {
            "title": "📌 Electronic Blockchain-Based Bidding App",
            "desc": "A decentralized application for secure and transparent university bidding processes.",
            "stack": "Python, Streamlit, Hyperledger Fabric, IPFS",
            "repo": "https://github.com/DjinnSuba/blockchain-bidding-app",
        },
        {
            "title": "📌 Hospital Readmission Dashboard",
            "desc": "Django + PostgreSQL dashboard with role-based access (admin, clinician, analyst).",
            "stack": "Django, PostgreSQL, Streamlit (for analytics)",
            "repo": "https://github.com/DjinnSuba/hospital-dashboard",
        },
        {
            "title": "📌 Secure NLP Project",
            "desc": "A research project on privacy-preserving natural language processing using federated learning.",
            "stack": "Python, PyTorch, Transformers",
            "repo": "https://github.com/DjinnSuba/se
