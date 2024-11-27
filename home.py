import streamlit as st
from css import *
from constants import *

# st.set_page_config(layout='wide')


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)





#---APP---
page_1 = st.Page("page/bunkers.py", title="Bunkers & Vleermuiskasten" )
page_2 = st.Page("page/home_2.py", title="Home")
page_3 = st.Page("page/ratten_tershelling.py", title="Ratten in Terschelling" )
# page_4 = st.Page("page/smp_app.py", title="Field map",icon="📊" )
page_5 = st.Page("page/smp_terschelling.py", title="Terschelling 2025" )

#---APP---
# st.logo(IMAGE,  link=LINK, icon_image=IMAGE,size="large")
pages = {
    'Old projects':[page_2],
  'On-going projects':[page_1,page_3],

        }
pg = st.navigation(pages,expanded=False,position ='hidden')
  
pg.run()
