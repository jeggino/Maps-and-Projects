import streamlit as st
from css import *
from constants import *
import base64

text= """
Welcome to our dashboard! 

Here, you will find a friendly overview of our current and past projects. 

Each project includes a visual preview, a brief description, and a hyperlink that directs you to a real-time dashboard for the latest updates. 

For past projects, we have also provided a download link so you can access related files. 

:rainbow[Enjoy exploring!]
"""

col_1,col_2,col_3 = st.columns([1,2,1])
col_2.markdown(
    """<a href="https://www.elskenecologie.nl/contact-elsken-ecologie-nh-terschelling/">
    <img src="data:image/png;base64,{}" width="350">
    </a>
    <br><br>
    """.format(
        base64.b64encode(open(IMAGE, "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

"---"

st.markdown(text)


with st.expander("""**Ongoing projects**"""):
    col_1,col_2 = st.columns([1,1])
    
    col_1.markdown(
        """<a href="https://maps-and-projects.streamlit.app/bunkers">
        <img src="data:image/png;base64,{}" width="250">
        </a>
        <br><font size="2" style="font-family:'Courier New'">Bunkers en vleermuizenkasten</font><be>
        """.format(
            base64.b64encode(open('images/bunkers_1.jpg', "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
    
    col_2.markdown(
        """<a href="https://maps-and-projects.streamlit.app/ratten_tershelling">
        <img src="data:image/png;base64,{}" width="250">
        </a>
        <br><font size="2" style="font-family:'Courier New'">Ratten in Terschelling</font><be>
        """.format(
            base64.b64encode(open('images/rats_1.jpg', "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )

"---"
