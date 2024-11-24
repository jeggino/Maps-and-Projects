import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---COSTANTS---
title = "De invasie van de gewone rat (Rattus norvegicus) op Terschelling: eerste uitroeiingsinspanningen"
text = """
Deze kaart illustreert de inspanningen om de invasie van de gewone rat op Terschelling uit te roeien. Terschelling staat bekend om zijn gevarieerde fauna en is met name belangrijk voor vogelnesten, aangezien veel soorten afhankelijk zijn van de habitats op grondniveau van het eiland om hun jongen groot te brengen. Helaas zijn deze nesten zeer vatbaar voor predatie door de invasieve knaagdierpopulatie. Tot voor kort was het eiland grotendeels vrij van ratten; echter, een paar individuen zijn mogelijk per ongeluk per boot van het vasteland aangekomen, wat aanleiding gaf tot dringende actie.

Er worden twee soorten vallen gebruikt om de rattenpopulatie in te dammen, gevolgd door de nodige procedures om ze te verwijderen. Daarnaast worden er cameravallen in het veld opgezet om tekenen van knaagdieractiviteit te monitoren. We hopen dat onze inspanningen, met de hulp van de provincie Friesland, zullen helpen deze invasieve soort uit te roeien voordat het broedseizoen van de vogels begint.
"""
img = "images/rats_1.jpg"
link = "https://ratten-terschelling-dashboard.streamlit.app/"

#---APP---
st.title(title)
st.image(img)
st.markdown(text)
st.link_button(":rainbow[Link dashboard]", link,icon='🐀')
"---"

