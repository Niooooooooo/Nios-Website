import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
from pytube import YouTube
import os

title = "Youtube Download"
icon = ":notes:"

st.set_page_config(page_title=title, page_icon=icon,layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

lottie_download = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_EAfMOs/Youtube.json")

with st.sidebar:
    st_lottie(lottie_download, height=300, key="download")

with st.container():
    st.title(title)
    st.error("only works on localhost")

# ----YouTube Download----
PATH_SAVE = "downloads"

with st.container():
    st.write("---")
    st.write("##")
    link = st.text_input(label="", placeholder="Enter URL")

    right_column, left_column = st.columns(2)

    try:

        with left_column:
            option = st.selectbox(label="Select Filetype", label_visibility="collapsed", options=["mp3", "mp4"])

        with right_column:
            if st.button(use_container_width=True, label="Download"):

                if link != "":    
                    if option == "mp3":
                        
                        yt = YouTube(link)
                        audio_file = yt.streams.get_by_itag(140).download(PATH_SAVE)
                        base, ext = os.path.splitext(audio_file)
                        new_file = base + ".mp3"
                        os.rename(audio_file, new_file)
                    
                    if option == "mp4":
                        
                        yt = YouTube(link)
                        video_file = yt.streams.get_highest_resolution()
                        video_file.download(PATH_SAVE)
    except:
        st.error(body="Something went wrong!")
        
