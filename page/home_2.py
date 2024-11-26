import streamlit as st
from css import *
from constants import *
import base64

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

with st.expander("Ongoing projects"):
    col_1,col_2 = st.columns([1,1])
    
    col_1.markdown(
        """<a href="https://bunkers-vleermuizenkasten-dashboard.streamlit.app/">
        <img src="data:image/png;base64,{}" width="250"></a>
        <br><font size="5">Ciao</font><br>
        """.format(
            base64.b64encode(open('images/bunkers_1.jpg', "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
    
    col_2.markdown(
        """<a href="https://ratten-terschelling-dashboard.streamlit.app/">
        <img src="data:image/png;base64,{}" width="250">
        </a>""".format(
            base64.b64encode(open('images/rats_1.jpg', "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )

"---"
