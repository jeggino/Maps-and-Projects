import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---COSTANTS---
title_eng = "The invasion of the common rat (Rattus norvegicus) on Terschelling: first eradication efforts"
text_eng = """
This map illustrates the efforts to eradicate the common rat invasion on Terschelling. Terschelling is known for its diverse fauna and is particularly important for bird nests, as many species rely on the island’s ground-level habitats to raise their young. Unfortunately, these nests are highly susceptible to predation by the invasive rodent population. Until recently, the island was largely free of rats; however, a few individuals may have accidentally arrived by boat from the mainland, prompting urgent action.

Two types of traps are being used to contain the rat population, followed by the necessary procedures to remove them. In addition, camera traps are being set up in the field to monitor signs of rodent activity. We hope that our efforts, with the help of the province of Friesland, will help eradicate this invasive species before the bird breeding season begins."""

title_ned = "De invasie van de gewone rat (Rattus norvegicus) op Terschelling: eerste uitroeiingsinspanningen"
text_ned = """
Deze kaart illustreert de inspanningen om de invasie van de gewone rat op Terschelling uit te roeien. Terschelling staat bekend om zijn gevarieerde fauna en is met name belangrijk voor vogelnesten, aangezien veel soorten afhankelijk zijn van de habitats op grondniveau van het eiland om hun jongen groot te brengen. Helaas zijn deze nesten zeer vatbaar voor predatie door de invasieve knaagdierpopulatie. Tot voor kort was het eiland grotendeels vrij van ratten; echter, een paar individuen zijn mogelijk per ongeluk per boot van het vasteland aangekomen, wat aanleiding gaf tot dringende actie.

Er worden twee soorten vallen gebruikt om de rattenpopulatie in te dammen, gevolgd door de nodige procedures om ze te verwijderen. Daarnaast worden er cameravallen in het veld opgezet om tekenen van knaagdieractiviteit te monitoren. We hopen dat onze inspanningen, met de hulp van de provincie Friesland, zullen helpen deze invasieve soort uit te roeien voordat het broedseizoen van de vogels begint.
"""

title_ita = "L'invasione del ratto comune (Rattus norvegicus) su Terschelling: primi sforzi di eradicazione"
text_ita = """
Questa mappa illustra gli sforzi per sradicare l'invasione del ratto comune su Terschelling. Terschelling è nota per la sua variegata fauna selvatica ed è particolarmente importante per i nidi di uccelli, poiché molte specie fanno affidamento sugli habitat a livello del suolo dell'isola per allevare i loro piccoli. Sfortunatamente, questi nidi sono altamente suscettibili alla predazione da parte della popolazione invasiva di roditori. Fino a poco tempo fa, l’isola era in gran parte priva di ratti; tuttavia, alcune persone potrebbero essere arrivate accidentalmente dalla terraferma in barca, richiedendo un'azione urgente.

Per controllare la popolazione di ratti vengono utilizzati due tipi di trappole, seguite dalle procedure necessarie per rimuoverle. Inoltre, sul campo vengono installate trappole fotografiche per monitorare i segni di attività dei roditori. Ci auguriamo che i nostri sforzi, con l'aiuto della provincia della Frisia, contribuiscano a sradicare questa specie invasiva prima che inizi la stagione riproduttiva degli uccelli."""

title_esp = "La invasión de la rata común (Rattus norvegicus) en Terschelling: primeros esfuerzos de erradicación"
text_esp = """
Este mapa ilustra los esfuerzos para erradicar la invasión de la rata común en Terschelling. Terschelling es conocida por su diversa vida silvestre y es particularmente importante por los nidos de aves, ya que muchas especies dependen de los hábitats a nivel del suelo de la isla para criar a sus crías. Desafortunadamente, estos nidos son muy susceptibles a la depredación por parte de la población de roedores invasores. Hasta hace poco, la isla estaba prácticamente libre de ratas; sin embargo, es posible que algunas personas hayan llegado accidentalmente desde el continente en barco, lo que provocó que se tomaran medidas urgentes.

Se utilizan dos tipos de trampas para controlar la población de ratas, seguidos de los procedimientos necesarios para eliminarlas. Además, se instalan cámaras trampa en el campo para monitorear signos de actividad de roedores. Esperamos que nuestros esfuerzos, con la ayuda de la provincia de Frisia, ayuden a erradicar esta especie invasora antes de que comience la temporada de reproducción de las aves."""

img = "images/rats_1.jpg"
link = "https://ratten-terschelling-dashboard.streamlit.app/"

#---APP---
tab1, tab2, tab3, tab4 = st.tabs(["English 🇬🇧", "Nederlands 🇳🇱", "Español 🇪🇸", "Italiano 🇮🇹"])

with tab1:
  st.subheader(title_eng)
  st.image(img)
  st.markdown(text_eng)

with tab2:
  st.subheader(title_ned)
  st.image(img)
  st.markdown(text_ned)

with tab3:
  st.subheader(title_esp)
  st.image(img)
  st.markdown(text_esp)

with tab4:
  st.subheader(title_ita)
  st.image(img)
  st.markdown(text_ita)

st.link_button(":rainbow[Link dashboard]", link,icon='🐀')
"---"

