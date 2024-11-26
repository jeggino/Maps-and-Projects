import streamlit as st
from css import *
from constants import *



#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)





#---APP---
page_1 = st.Page("page/bunkers.py", title="Bunkers & Vleermuiskasten",icon="🦇" )
# page_2 = st.Page("page/exotem_planten.py", title="Invasive plants",icon="✍️" )
page_3 = st.Page("page/ratten_tershelling.py", title="Ratten in Terschelling",icon="🐀" )
# page_4 = st.Page("page/smp_app.py", title="Field map",icon="📊" )
page_5 = st.Page("page/smp_terschelling.py", title="Terschelling 2025" )

#---APP---
st.logo(IMAGE,  link=LINK, icon_image=IMAGE,size="large")
pages = {
  'On-going projects':[page_1,page_3],
  'Old projects':[page_5]
        }
pg = st.navigation(pages,expanded=True)
  
pg.run()
