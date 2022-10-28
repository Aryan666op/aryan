import streamlit as st
from  PIL import Image as image
from streamlit_lottie import st_lottie as  lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Programming Aryan" ,layout="wide")

with st.container():
    st.header("HEY GUY'S :wave:")
    st.header("MYSELF PROGRAMMING ARYAN")

with st.container():
    st.subheader("Click below to subscribe me")
    st.markdown("[click here](https://www.youtube.com/channel/UCCquWagYSDiemdYtJA85KOw?sub_confirmation=1)")