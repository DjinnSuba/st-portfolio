import streamlit as st
from PIL import Image
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- Helper function for PDFs ---
def display_pdf(file):
    """Display PDF in Streamlit with iframe"""
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
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
    st.write("""
        I'm a **Data Analyst x AI Developer** with a passion for creating impactful real-world solutions.
        
        - 🌱 I’m currently working on...
        - 💼 I’ve worked with: **MSCI Inc, UPM IMS-DIG, Remotasks**
        - 📫 How to reach me: [othedjinn@gmail.com](mailto:othedjinn@gmail.com) | 
          [LinkedIn](https://www.linkedin.com/in/caezar-suba-634453161/)
    """)

    # --- Certifications Section ---
    st.header("📜 Certifications & Badges")

    # Example 1: Display badges in a row
    col1, col2, col3 = st.columns(3)

    with col1:
        try:
            badge1 = Image.open("DS Associate - badge with outline.png")
            st.image(badge1, caption="Data Science Associate Certification", use_container_width=True)
        except FileNotFoundError:
            st.warning("Missing: DS Associate - badge with outline.png")

    with col2:
        try:
            badge2 = Image.open("cert_streamlit.png")
            st.image(badge2, caption="Streamlit Creator Badge", use_container_width=True)
        except FileNotFoundError:
            st.warning("Missing: cert_streamlit.png")

    with col3:
        try:
            badge3 = Image.open("cert_aws.png")
            st.image(badge3, caption="AWS Cloud Practitioner", use_container_width=True)
        except FileNotFoundError:
            st.warning("Missing: cert_aws.png")

    # Example 2: Simple list with links
    st.markdown("""
    - 🏆 [Google Data Analytics Certificate](https://www.credly.com/)
    - ☁️ [AWS Cloud Practitioner](https://www.credly.com/)
    - 📊 [Tableau Desktop Specialist](https://www.credly.com/)
    """)

    # Example 3: PDF Certificates (inline view + download)
    st.subheader("📂 Certificate PDFs")

    try:
        st.markdown("**Associate Data Scienctist (PDF Preview)**")
        display_pdf("DataScienceAssociate-certificate.pdf")
    except FileNotFoundError:
        st.warning("Missing: DataScienceAssociate-certificate.pdf")

    try:
        with open("Intermediate_Python-certificate.pdf", "rb") as pdf_file:
            st.download_button(
                label="☁️ Intermediate Python",
                data=pdf_file,
                file_name="Intermediate_Python-certificate.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Missing: Intermediate_Python-certificate.pdf")

# --- PROJECTS PAGE ---
elif selection == "Projects":
    st.title("💼 Projects")
    st.write("Here are some of my featured projects:")

    st.subheader("Electronic Blockchain-Based Bidding App")
    st.write("""
    - **Description**: What this project is about.
    - **Tech Stack**: Python, Streamlit, etc.
    """)

    st.subheader("📌 Project 2: [Another Project]")
    st.write("""
    - **Description**: Features and links.
    """)

# --- CONTACT PAGE ---
elif selection == "Contact":
    st.title("📫 Contact Me")
    st.write("I'd love to connect!")

    contact_form = """
    <form action="https://formsubmit.co/othedjinn@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Optional form styling
    st.markdown("""
        <style>
        form {
            display: flex;
            flex-direction: column;
        }
        input, textarea {
            margin-bottom: 10px;
            padding: 10px;
            font-size: 1rem;
            width: 100%;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            font-size: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
