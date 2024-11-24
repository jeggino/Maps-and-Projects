import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---COSTANTS---
title = "Bunker & Batbox Mapping Project"
text = """
Het Bunker & Batbox Mapping Project is een toegewijd initiatief dat zich richt op het grondig documenteren en analyseren van de verspreiding van vleermuisroostplaatsen op het eiland Terchelling tijdens de cruciale winterslaapperiode. Dit project omvat het nauwkeurig in kaart brengen van de locaties van verschillende bunkers en vleermuiskasten verspreid over het eiland. Naast het in kaart brengen voeren we uitgebreide onderzoeken uit die niet alleen de aangetroffen vleermuissoorten identificeren, maar ook belangrijke omgevingsgegevens vastleggen, zoals temperatuur- en vochtigheidsniveaus die op het moment van elke waarneming zijn waargenomen.

Ons primaire doel is om de ingewikkelde relaties tussen vleermuispopulaties en hun omringende omgevingskenmerken te onthullen. Door inzicht te krijgen in deze dynamiek, hopen we belangrijke kenmerken te identificeren die bijdragen aan het voortbestaan ​​en welzijn van vleermuissoorten in het gebied.

We nodigen gepassioneerde ecologen en natuurliefhebbers van harte uit om zich bij ons aan te sluiten in dit gezamenlijke onderzoeksproject. Als u geïnteresseerd bent om deel uit te maken van dit opwindende project en meer wilt weten over hoe u kunt meedoen, aarzel dan niet om contact met ons op te nemen voor meer informatie. Uw betrokkenheid kan een groot verschil maken in ons begrip en behoud van deze opmerkelijke wezens.
"""
img = "images/bunkers_1.jpg"
link = "https://bunkers-vleermuizenkasten-dashboard.streamlit.app/"

#---APP---
st.title(title)


st.image(img)
st.markdown(text)
st.link_button("Link dashboard", link,icon='🐀')
