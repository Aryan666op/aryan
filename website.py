import builtins
import keyword
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie as  lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-------page name -----------
st.set_page_config(page_title='Aryan' , page_icon=':sunglasses:' ,layout="wide" )

#-----Animation-----

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")

#------Images------


#-------filling first container--------

with st.container():
    st.subheader("HELLO MYSELF ARYAN CHATURVEDI :wave:")
    st.title("A PROGAMMER :tada:")
    st.write('''TAP THE LINK BELOW TO SEE HOW TO MAKE 
    A BIRHDAY WISHINGPROGRAM USING PYTHON THIS IS MY PERSONAL WEBSITE 
    , WHICH I AM LEARNING TO CREATE NOWAFTER I LEARN HOW TO CREATE A
     WEBSITE I WILL MAKE MANY OF THEM BY THE WAY IF YOU WANNA KNOW HOW
      TO CREATE A PYTHON PROGRAMFOR BIRTHDAY WISHING CLICK THE BELOW BUTTON''')
    st.markdown('[click here](https://youtube.com/shorts/0RReb7FBkXk?feature=share)')

#-------Second container--------

with st.container():
    st.write("---")
    leftcolumn , rightcolumn = st.columns(2)
    with leftcolumn :
        st.write('''I have madethis website actully webpage only for experiment
        and trials . This website is made by aryan chaturvedi .
        i know the animation on the right side is very attractive 
        this you can get from lottie . Thank you for reading !!''')
    with rightcolumn:
        lottie(lottie_coding )

with st.container():
    st.subheader("Channels you may like ")
    st.markdown("[Programming Aryan](https://www.youtube.com/channel/UCCquWagYSDiemdYtJA85KOw)")
    st.markdown("[Code With Haryy](https://www.youtube.com/c/CodeWithHarry)")
    st.markdown("[Code is fun](https://www.youtube.com/c/CodingIsFun)")

with st.container():
    st.write("---")
    st.subheader("GET IN TOUCH WITH ME")
    st.write('##')

    contact_form = '''
    <form action="https://formsubmit.co/aryan.chaturvedi.1209@gmail.com" method="POST">
        <input type="text" placeholder = 'YOUR NAME' name="name" required>
        <input type="email" placeholder = 'YOUR E-MAIL' name="email" required>
        <button type="submit">Send</button>
    </form>'''
    leftcolumn , rightcolumn = st.columns(2)
    with leftcolumn:
        st.markdown(contact_form , unsafe_allow_html=True)
    with rightcolumn:
        st.empty()

with st.container():
    st.header('''THANK YOU FOR VISITING THIS SITE ''')