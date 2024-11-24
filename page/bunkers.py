import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---APP---
st.html(
    "html/SMP-Terschelling-Bats.html"
)
