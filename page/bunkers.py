import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---COSTANTS---
img = "images/bunkers_1.jpg"
link = "https://bunkers-vleermuizenkasten-dashboard.streamlit.app/"

title_eng = "Bunker & bat box mapping project"
text_eng = """
The Bunker & Batbox Mapping Project is a dedicated initiative that aims to thoroughly document and analyze the distribution of bat roosts on the island of Terchelling during the crucial hibernation period. This project involves the accurate mapping of the locations of various bunkers and bat boxes across the island. In addition to mapping, we conduct extensive surveys that not only identify the bat species encountered, but also record important environmental data such as temperature and humidity levels observed at the time of each observation.

Our primary goal is to reveal the intricate relationships between bat populations and their surrounding environmental features. By gaining insight into these dynamics, we hope to identify important features that contribute to the survival and well-being of bat species in the area.

We warmly invite passionate ecologists and nature lovers to join us in this collaborative research project. If you are interested in being part of this exciting project and would like to know more about how you can get involved, please do not hesitate to contact us for more information. Your involvement can make a huge difference to our understanding and conservation of these remarkable creatures."""

title_ned = "Bunker & vleermuiskasten in kaart brengen project"
text_ned = """
Het Bunker & Batbox Mapping Project is een toegewijd initiatief dat zich richt op het grondig documenteren en analyseren van de verspreiding van vleermuisroostplaatsen op het eiland Terchelling tijdens de cruciale winterslaapperiode. Dit project omvat het nauwkeurig in kaart brengen van de locaties van verschillende bunkers en vleermuiskasten verspreid over het eiland. Naast het in kaart brengen voeren we uitgebreide onderzoeken uit die niet alleen de aangetroffen vleermuissoorten identificeren, maar ook belangrijke omgevingsgegevens vastleggen, zoals temperatuur- en vochtigheidsniveaus die op het moment van elke waarneming zijn waargenomen.

Ons primaire doel is om de ingewikkelde relaties tussen vleermuispopulaties en hun omringende omgevingskenmerken te onthullen. Door inzicht te krijgen in deze dynamiek, hopen we belangrijke kenmerken te identificeren die bijdragen aan het voortbestaan ​​en welzijn van vleermuissoorten in het gebied.

We nodigen gepassioneerde ecologen en natuurliefhebbers van harte uit om zich bij ons aan te sluiten in dit gezamenlijke onderzoeksproject. Als u geïnteresseerd bent om deel uit te maken van dit opwindende project en meer wilt weten over hoe u kunt meedoen, aarzel dan niet om contact met ons op te nemen voor meer informatie. Uw betrokkenheid kan een groot verschil maken in ons begrip en behoud van deze opmerkelijke wezens.
"""

title_ita = "Progetto di mappatura di bunker e batbox"
text_ita = """
Il Bunker & Batbox Mapping Project è un'iniziativa dedicata volta a documentare e analizzare in modo approfondito la distribuzione dei rifugi dei pipistrelli sull'isola di Terchelling durante il periodo cruciale del letargo. Questo progetto prevede la mappatura accurata delle posizioni dei vari bunker e cassette per pipistrelli in tutta l'isola. Oltre alla mappatura, conduciamo indagini approfondite che non solo identificano le specie di pipistrelli incontrate, ma registrano anche importanti dati ambientali come i livelli di temperatura e umidità osservati al momento di ogni avvistamento.

Il nostro obiettivo principale è rivelare le complicate relazioni tra le popolazioni di pipistrelli e le caratteristiche ambientali circostanti. Comprendendo queste dinamiche, speriamo di identificare caratteristiche importanti che contribuiscono alla sopravvivenza e al benessere delle specie di pipistrelli nell’area.

Invitiamo cordialmente ecologisti appassionati e amanti della natura a unirsi a noi in questo progetto di ricerca congiunto. Se sei interessato a far parte di questo entusiasmante progetto e vorresti sapere di più su come partecipare, non esitare a contattarci per ulteriori informazioni. Il tuo coinvolgimento può fare una grande differenza nella nostra comprensione e conservazione di queste straordinarie creature."""

title_esp = "Proyecto de mapeo de búnkeres y cajas para murciélagos"
text_esp = """
El Proyecto de Mapeo de Bunker & Batbox es una iniciativa dedicada a documentar y analizar en profundidad la distribución de los refugios de los murciélagos en la isla de Terchelling durante el crucial período de hibernación. Este proyecto implica mapear con precisión las ubicaciones de varios búnkeres y cajas de murciélagos en toda la isla. Además del mapeo, realizamos estudios extensos que no solo identifican las especies de murciélagos encontradas, sino que también registran datos ambientales importantes, como los niveles de temperatura y humedad observados en el momento de cada avistamiento.

Nuestro objetivo principal es revelar las complicadas relaciones entre las poblaciones de murciélagos y las características ambientales que las rodean. Al comprender esta dinámica, esperamos identificar características importantes que contribuyan a la supervivencia y el bienestar de las especies de murciélagos en el área.

Invitamos cordialmente a apasionados ecologistas y amantes de la naturaleza a unirse a nosotros en este proyecto de investigación conjunto. Si está interesado en ser parte de este emocionante proyecto y le gustaría saber más sobre cómo puede participar, no dude en contactarnos para obtener más información. Su participación puede marcar una gran diferencia en nuestra comprensión y conservación de estas notables criaturas.
"""


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

st.link_button(":rainbow[Link dashboard]", link,icon='🦇')
"---"

