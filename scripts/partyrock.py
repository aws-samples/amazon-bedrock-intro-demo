import streamlit as st
from st_pages import show_pages_from_config

st.set_page_config(
    page_title="Amazon Bedrock - Introductory Demo",
    page_icon="👋",
    layout="wide"
)
show_pages_from_config(".streamlit/pages_sections.toml")
css = '''
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
    </style>
'''
st.write(css, unsafe_allow_html=True)
st.write("# PartyRock 💽")

st.markdown(
"""
**[PartyRock](https://partyrock.aws/)** is an Amazon Bedrock playground for building and sharing generative AI apps as part of an *educational* and *fun* experience! PartyRock provides an easy, **no-code**, interactive UI for getting introduced to the power of foundation models with Amazon Bedrock. **Anyone** (no AWS account required) can access PartyRock with free trial use for a limited time, by creating a profile using a social login from amazon.com, Apple, or Google. 
    
Check out the video below of some PartyRock apps.

""")
video_file = open('video/partyrock_myapps.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.markdown(
"""   
### PartyRock App URLs
You may click the following URLs to access the PartyRock apps shown in the above video and remix.

-  [Foundation model comparison](https://partyrock.aws/u/cybergavin/Qx0z-VlrU/Foundation-model-comparison)
-  [Code Translator](https://partyrock.aws/u/cybergavin/M1wTop3Zz/Code-Translator)
-  [School Quiz Generator](https://partyrock.aws/u/cybergavin/zmjxFS4k3/School-Quiz-Generator)
-  [Guitar Tablature](https://partyrock.aws/u/cybergavin/LXryWAB2K/Guitar-Tablature)
-  [CyberG Chat](https://partyrock.aws/u/cybergavin/P6Rtls9bb/CyberG-Chat)
""")
