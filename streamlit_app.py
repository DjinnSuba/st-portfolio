import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide")

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
        st.warning("Profile picture not found. Please place 'your_photo.jpg' in the app folder.")

    # Resume download button
    try:
        with open("resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download My Resume",
                data=pdf_file,
                file_name="CV-Suba, OdeDjinnCaezar.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Resume file not found. Please place 'resume.pdf' in the app folder.")

    # About Me Section
    st.header("About Me")
    st.write("""
        I'm a **Data Analyst x AI Developer** with a passion for creating impactful real-world solutions.
        
        - 🌱 I’m currently working on...
        - 💼 I’ve worked with: **MSCI Inc, UPM IMS-DIG, Remotasks**
        - 📫 How to reach me: [othedjinn@gmail.com](mailto:othedjinn@gmail.com) | 
          [LinkedIn](https://www.linkedin.com/in/caezar-suba-634453161/)
    """)

# --- PROJECTS PAGE ---
elif selection == "Projects":
    st.title("💼 Projects")
    st.write("Here are some of my featured projects:")

    st.subheader("📌 Project 1: [Project Name]")
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
