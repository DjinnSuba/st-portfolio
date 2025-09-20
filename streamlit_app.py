import streamlit as st
import requests
from PIL import Image
import base64
import fitz  # PyMuPDF <-- missing import

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- Helper function for PDFs ---
def display_pdf(file):
    """Display PDF in Streamlit with iframe (local files only)."""
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
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
    st.header("About Me")
    st.markdown("""
        I'm a **Data Analyst x AI Developer** with a passion for creating impactful real-world solutions.
    """)

    # --- Certifications Section ---
    st.header("📜 Certifications & Badges")

    certificates = {
        "AI Agent Fundamentals": "https://github.com/DjinnSuba/st-portfolio/raw/main/AI_Agent_Fundamentals-certificate.pdf",
        "Building AI Agents with Google ADK": "https://github.com/DjinnSuba/st-portfolio/raw/main/Building_AI_Agents_with_Google_ADK-certificate.pdf",
        "Associate Data Scientist": "https://github.com/DjinnSuba/st-portfolio/raw/main/DataScienceAssociate-certificate.pdf",
        "Intermediate Python": "https://github.com/DjinnSuba/st-portfolio/raw/main/Intermediate_Python-certificate.pdf",
        "Intermediate SQL": "https://github.com/DjinnSuba/st-portfolio/raw/main/Intermediate_SQL-certificate.pdf",
        "Introduction to PowerBI": "https://github.com/DjinnSuba/st-portfolio/raw/main/Introduction_PowerBI-certificate.pdf",
    }

    for name, url in certificates.items():
        st.subheader(f"📖 {name}")
        try:
            response = requests.get(url)
            pdf_bytes = response.content

            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            page = doc[0]
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # zoom 2x
            st.image(pix.tobytes("png"), caption=f"{name} (Page 1 Preview)", use_container_width=True)

            with st.expander("View full certificate"):
                for i in range(len(doc)):
                    page = doc[i]
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                    st.image(pix.tobytes("png"), caption=f"{name} - Page {i+1}")

            st.markdown(f"[🔗 Open {name} in New Tab]({url})")

        except Exception as e:
            st.error(f"Could not load {name}: {e}")

        st.markdown("---")

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
            "repo": "https://github.com/DjinnSuba/secure-nlp",
        },
    ]

    for project in projects:
        st.subheader(project["title"])
        st.markdown(f"""
        - **Description**: {project["desc"]}
        - **Tech Stack**: {project["stack"]}
        - **Repo**: [View on GitHub]({project["repo"]})
        """)
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

    st.markdown("""
        <style>
        form {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        input, textarea {
            padding: 10px;
            font-size: 1rem;
            border: 1px solid #ddd;
            border-radius: 6px;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            font-size: 1rem;
            cursor: pointer;
            border-radius: 6px;
        }
        button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)
