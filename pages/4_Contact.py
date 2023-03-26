import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

title = "Contact"
icon = ":speech_balloon:"

st.set_page_config(page_title=title, page_icon=icon,layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

lottie_contact = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_wbhpdrhp.json")

with st.sidebar:
    st_lottie(lottie_contact, height=300, key="contact")

# ----Use local CSS----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# ----Contact----

with st.container():
    st.header("it'sa meeee Niooo lol")
    st.write("---")

    contact_form =  """
                    <form action="https://formsubmit.co/tofutorben89@gmail.com" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="name" placeholder="Your name" required>
                        <input type="email" name="email" placeholder="Your email" required>
                        <textarea name="message" placeholder="Your message here" required></textarea>
                        <button type="submit">Send</button>
                    </form>
                    """
    
    
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        
    with right_column:
        st.empty()

with st.container():
    st.write("---")
    discord_img = "https://i.imgur.com/xS9eDhA.png"    
    st.markdown(f"[![Foo]({discord_img})](https://discord.gg/REdzRzTJ)")