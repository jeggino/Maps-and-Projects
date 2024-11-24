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
# page_5 = st.Page("page/smp_amsterdam.py", title="SMP Amterdam 2024",icon="📊" )

#---APP---
st.logo(IMAGE,  link=LINK, icon_image=IMAGE,size="large")
pages = {
  'Aplications and projects':[page_1],
  'A':[page_3,]
        }
pg = st.navigation(pages)
  
pg.run()
