import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

title = "Cloud"
icon = ":cloud:"

st.set_page_config(page_title=title, page_icon=icon,layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

lottie_cloud = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9h7vr2l7.json")

with st.sidebar:
    st_lottie(lottie_cloud, height=300, key="cloud")

with st.container():
    st.title(title)

with st.container():

    left_column, right_column = st.columns(2)

    with left_column:
        uploaded_file = st.file_uploader(label="File Uploader", label_visibility="collapsed", accept_multiple_files=False)

    with right_column:
        if uploaded_file is not None:
            st.download_button(label="File Download", data=uploaded_file)