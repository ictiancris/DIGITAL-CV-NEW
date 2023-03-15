from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"Ian Cris Tocle_CVUPDATE.pdf"
profile_pic = current_dir/"assets"/"PHOTO_IAN CRIS TOCLE.jpg"
video_1 = current_dir/"assets"/"EXCEL + POWER BI RECEIVLA FINAL.mp4"
video_2 = current_dir/"assets"/"CPV FINAL.mp4"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ian Cris Tocle"
PAGE_ICON = ":wave:"
NAME = "Ian Cris Tocle"
DESCRIPTION = """
Filipino, 10/31/2003

Financial Analyst | Accountant | Data Science/Data Analyst | UAE Residence Visa
"""
EMAIL = "ic.tocle@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ian-cris-tocle-6315a4235/",
    "Facebook": "https://www.facebook.com/iancris.tocle/",
}
EDUCATION_AND_CERTIFICATION = {
    "Bachelor's Degree of Applied Accounting Graduate of Oxford Brookes University (OBU)",
    "ACCA Diploma and Advanced Diploma in Accounting and Business",
    "Financial Analyst Certification",
    "IBM Professional Certificate",
    "Google Analytics Professional Certificate",
    "Microsoft Power BI Certificate (On going)"
}
PROJECTS = {
    "Google Data Analytics Capstone Project",
    "IBM Data Analytics Capstone Project",
    "Machine Learning Auto-Attendance + AI Facial Recognition (Python)",
    "Budgeting and Forecasting (Excel Template)",
    "Aged Receivable and Payable Analysis (Excel Template)",
    "Power BI Dashboard and Reports Analysis",
    "Cheque Payment Voucher Template (Excel/VBA)",
    "Tableau - Data Visualization",
    "Full-Depth Financial Report and Research Analysis Thesis (OBU)",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")

#---LOAD CSS, PDF & PROFILE PIC---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#---HERO SECTION---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)
 
#---SOCIAL LINKS---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#---EDUCATION AND CERTIFICATIONS
st.write("#")
st.subheader("Education and Certifications")
st.write(
    """
- Bachelor's Degree of Applied Accounting Graduate of Oxford Brookes University (OBU)
- ACCA Diploma and Advanced Diploma in Accounting and Business
- Financial Analyst Certification
- IBM Professional Certificate
- Google Analytics Professional Certificate
- Microsoft Power BI Certificate (On going)
    """
)

#---Projects
st.write("#")
st.subheader("Projects")
st.write(
    """
    - Google Data Analytics Capstone Project
    - IBM Data Analytics Capstone Project
    - Machine Learning Auto-Attendance + AI Facial Recognition (Python)
    - Budgeting and Forecasting (Excel Template)
    - Aged Receivable and Payable Analysis (Excel Template)
    - Power BI Dashboard and Reports Analysis
    - Cheque Payment Voucher Template (Excel/VBA)
    - Tableau - Data Visualization
    - Full-Depth Financial Report and Research Analysis Thesis (OBU)
    """
)

st.write("""
    Videos

    """
    )

video_1 = open(video_1, "rb")
video_2 = open(video_2, "rb")

st.video(video_1)
st.video(video_2)


#---SKILLS
st.write("#")
st.subheader("SKILLS")
st.write(
    """
    - Financial Data Analysis
    - Power BI and Tableau Data Visualizations
    - Python Framework and Libraries (Jupyter-IDE)
    - HTML-CSS-Javascript/Power Page/Wordpress (VSCode)
    - Public Speaking - (Gavels and PBS)
    - MS Office Excel/Word/Powerpoint/Outlook
    - Photo / Video Editing
    - PC Networking / Gaming


    """
)


#---Language
st.write("#")
st.subheader("Language")
st.write(
    """
    - Filipino
    - English
    """
)

