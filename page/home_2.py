import streamlit as st
from css import *
from constants import *

text= """
Welcome to our dashboard! Here, you will find a friendly overview of our current and past projects. 

Each project includes a visual preview, a brief description, and a hyperlink that directs you to a real-time dashboard for the latest updates. 

For past projects, we have also provided a download link so you can access related files. 

:rainbow[Enjoy exploring!]
"""

img = IMAGE

#---APP---

st.image(img,width=200)
st.markdown(text)
"---"

img = Image.open(img)
st.button(st.image(img))
