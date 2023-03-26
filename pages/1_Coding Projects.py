import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

title = "Coding Projects"
icon = ":computer:"

st.set_page_config(page_title=title, page_icon=icon,layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

lottie_code = load_lottieurl("https://assets10.lottiefiles.com/temporary_files/9SxYT7.json")

with st.sidebar:
    st_lottie(lottie_code, height=300, key="code")

with st.container():
    st.title(title)

# ----Coding Projects----
with st.container():
    st.write("---")
    st.write("##")

    left_column, right_column = st.columns(2)

    with left_column:

        st.subheader("Blockdash [discontinued]")

        with open("tree/master/files/Blockdash.zip", "rb") as file:
            btn = st.download_button(
                    label="Download Blockdash",
                    data=file,
                    file_name="Blockdash.zip",
                    use_container_width=True
                )    

        st.subheader("TicTacToe for fx-CG50")

        with open("tree/master/files/TicTacTo.py", "rb") as file:
            btn = st.download_button(
                  label="Download TicTacToe",
                  data=file,
                  file_name="TicTacToe.py",
                  use_container_width=True
               )


    
    
