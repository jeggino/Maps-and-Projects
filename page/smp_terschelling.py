import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---COSTANTS---
title = "SMP Terschelling 2025"
text = """
:rainbow[FAKE FAKE FAKE]
"""
img = "images/smp_terschelling.jpg"
link = "html/SMP-Terschelling-Bats.html"

#---APP---
st.title(title)


st.image(img)
st.markdown(text)
with open(link, "rb") as file:
    btn = st.download_button(
        label=":rainbow[Download html file]",
        data=file,
        file_name=link,
        mime="html",
    )
"---"
