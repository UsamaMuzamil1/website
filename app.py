from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DigitalCV.pdf"
profile_pic = current_dir / "assets" / "usama.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Usama Muzamil"
PAGE_ICON = ":wave:"
NAME = "Usama Muzamil"
DESCRIPTION = """
Python Developer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "usamamuzammil54@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Objective ---
st.write('\n')
st.subheader("Objective")
st.write(
    """
- ✔️ Seeking a challenging position in a reputed organization where I can learn new skills, expand my knowledge, and leverage
my learnings
"""
)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience &  Knowledge")
st.write(
    """
- ✔️ Expereince in extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of Database & MySql
- ✔️ Knowledge about different softwares such as Pycharm, Jupytor etc
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Python Developer | Tpl Maps**")
st.write("08/2021 - Present")
st.write(
    """
- ► Queried MYSQL database queries from Python using Python-MYSQL Connector and MYSQL DB
package to retrieve information
- ► Basic understanding of machine learning, algorithms, supervised and un-supervised learning
- ► Make csv files, read, write and append files in python
- ► Store large amount of data in tables, insert, select, delete and update data in database using python
- ► Knowledge of popular Python libraries and frameworks
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Customer Executive | Ufone**")
st.write("03/2020 - 09/2021")
st.write(
    """
- ► Resolving a wide range of product and service issues speedily and satisfactorily
- ► Maintaining composure while handling challenging customer demands
- ► Solid experience in defining and analyzing customer requests to resolve issues accurately and quickly
with high first contact resolution rates
- ► Strong computer skills in a Windows-based environment and proven ability to learn unique software
- ► Confident and effective communicator who receives excellent customer feedback
"""
)


# --- Education ---
st.write('\n')
st.subheader("Education ")
st.write(
    """
- ► Bachelors in Information Technology- 2020(University Of The Punjab) 
"""
)
