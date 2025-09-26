import streamlit as st
import requests
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- GLOBAL CSS STYLE ---
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main {
        padding: 20px;
    }
    /* Titles */
    h1, h2, h3 {
        color: #fca311 !important;
    }
    /* Card styling */
    .card {
        background: #1c1e24;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.25);
        transition: transform 0.2s ease-in-out;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.35);
    }
    /* Links */
    a {
        color: #00c4ff !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    /* Contact form */
    form {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 20px;
    }
    input, textarea {
        padding: 10px;
        font-size: 1rem;
        border: 1px solid #333;
        border-radius: 6px;
        background: #1c1e24;
        color: #fafafa;
    }
    button {
        padding: 10px;
        background-color: #fca311;
        color: black;
        border: none;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        border-radius: 6px;
        transition: 0.3s;
    }
    button:hover {
        background-color: #ffb933;
    }
    </style>
""", unsafe_allow_html=True)

# --- Helper function for PDFs ---
def display_pdf_from_url(url: str, height: int = 400):
    """Embed a remote PDF in Streamlit via iframe without auto-download."""
    pdf_display = f"""
        <iframe src="https://docs.google.com/gview?url={url}&embedded=true" 
                width="100%" height="{height}" style="border: none; border-radius:8px;"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📌 Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

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
    st.header("💡 About Me")
    st.markdown("""
        I'm a **Data Analyst x AI Developer** with a passion for creating impactful real-world solutions.
    """)

    # --- Certifications Section ---
    st.header("📜 Certifications & Badges")

    # Badges row
    st.subheader("🏅 Badges")
    col1, col2, col3 = st.columns(3)

    with col1:
        try:
            badge1 = Image.open("DS Associate - badge with outline.png")
            st.image(badge1, caption="Data Science Associate", width=120)  # 👈 fixed size
        except FileNotFoundError:
            st.warning("Missing: DS Associate badge")

    with col2:
        try:
            badge2 = Image.open("cert_streamlit.png")
            st.image(badge2, caption="Streamlit Creator", width=120)  # 👈 fixed size
        except FileNotFoundError:
            st.warning("Missing: Streamlit badge")

    with col3:
        try:
            badge3 = Image.open("cert_aws.png")
            st.image(badge3, caption="AWS Cloud Practitioner", width=120)  # 👈 fixed size
        except FileNotFoundError:
            st.warning("Missing: AWS badge")

    # Certificates grid
    st.subheader("📖 Certificates")
    certificates = {
        "AI Agent Fundamentals": "https://github.com/DjinnSuba/st-portfolio/raw/main/AI_Agent_Fundamentals-certificate.pdf",
        "Building AI Agents with Google ADK": "https://github.com/DjinnSuba/st-portfolio/raw/main/Building_AI_Agents_with_Google_ADK-certificate.pdf",
        "Associate Data Scientist": "https://github.com/DjinnSuba/st-portfolio/raw/main/DataScienceAssociate-certificate.pdf",
        "Intermediate Python": "https://github.com/DjinnSuba/st-portfolio/raw/main/Intermediate_Python-certificate.pdf",
        "Intermediate SQL": "https://github.com/DjinnSuba/st-portfolio/raw/main/Intermediate_SQL-certificate.pdf",
        "Introduction to PowerBI": "https://github.com/DjinnSuba/st-portfolio/raw/main/Introduction_PowerBI-certificate.pdf",
    }

    cols = st.columns(3)
    for idx, (name, url) in enumerate(certificates.items()):
        with cols[idx % 3]:
            st.markdown(f"<div class='card'><b>{name}</b>", unsafe_allow_html=True)
            with st.expander("📂 View Full Certificate", expanded=False):
                display_pdf_from_url(url, height=300)
            st.markdown(f"[🔗 Open in New Tab]({url})", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS PAGE ---
elif selection == "Projects":
    st.title("💼 Projects")

    projects = [
        {
            "title": "📌 Automated Laboratory Inventory System",
            "desc": "A blockchain-based system for secure and transparent laboratory inventory management.",
            "stack": "Python, Streamlit, Hyperledger Fabric, IPFS",
            "repo": "https://github.com/DjinnSuba/automated-laboratory-inventory",
            "images": [
                "https://raw.githubusercontent.com/DjinnSuba/automated-laboratory-inventory/main/alims.png",
                "https://raw.githubusercontent.com/DjinnSuba/automated-laboratory-inventory/main/alims1.png"
            ],
        },
        {
            "title": "📌 Hospital Readmission Dashboard",
            "desc": "Django + PostgreSQL dashboard with role-based access (admin, clinician, analyst).",
            "stack": "Django, PostgreSQL, Streamlit (for analytics)",
            "repo": "https://github.com/DjinnSuba/hospital-readmission-dashboard",
            "images": [
                "https://raw.githubusercontent.com/DjinnSuba/hospital-readmission-dashboard/main/screenshots/dashboard1.png",
                "https://raw.githubusercontent.com/DjinnSuba/hospital-readmission-dashboard/main/screenshots/dashboard2.png"
            ],
        },
        {
            "title": "📌 Electronic Health Record",
            "desc": "An EHR web application for managing patient medical records securely.",
            "stack": "Django, PostgreSQL, Bootstrap",
            "repo": "https://github.com/DjinnSuba/Electronic-Health-Records",
            "images": [
                "https://raw.githubusercontent.com/DjinnSuba/Electronic-Health-Records/main/screenshots/ehr1.png",
                "https://raw.githubusercontent.com/DjinnSuba/Electronic-Health-Records/main/screenshots/ehr2.png"
            ],
        },
    ]

    for project in projects:
        st.markdown(f"### {project['title']}")
        st.write(project["desc"])
        st.write(f"**Tech Stack:** {project['stack']}")
        st.markdown(f"[🔗 View on GitHub]({project['repo']})")

        # Image "carousel" via radio buttons
        if project["images"]:
            img_choice = st.radio(
                f"Select screenshot for {project['title']}",
                options=list(range(len(project["images"]))),
                format_func=lambda i: f"Screenshot {i+1}",
                horizontal=True,
                key=project["title"]
            )
            st.image(project["images"][img_choice], use_column_width=True)

        st.markdown("---")



# --- CONTACT PAGE ---
elif selection == "Contact":
    st.title("📫 Contact Me")
    st.write("I'd love to connect! Please drop me a message:")

    contact_form = """
    <form action="https://formsubmit.co/othedjinn@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
