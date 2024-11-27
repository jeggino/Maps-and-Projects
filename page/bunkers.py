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
The Bunker and Batbox Mapping Project is a dedicated initiative focused on thoroughly documenting and analyzing the distribution of bat roosts on the island of Terchelling during the crucial hibernation period. This project involves meticulously mapping the locations of various bunkers and batboxes scattered across the island. Alongside the mapping, we conduct extensive surveys that not only identify the bat species encountered but also record important environmental data, such as temperature and humidity levels observed at the time of each sighting.

Our primary objective is to uncover the intricate relationships between bat populations and their surrounding environmental features. By gaining insight into these dynamics, we hope to identify key characteristics that contribute to the survival and well-being of bat species in the area. 

We warmly invite passionate ecologists and nature enthusiasts to join us in this collaborative research effort. If you're interested in being a part of this exciting project and wish to learn more about how you can get involved, please don’t hesitate to reach out to us for further information. Your involvement could make a significant difference in our understanding and conservation of these remarkable creatures.
"""

title_ned = "Bunker & vleermuiskasten in kaart brengen project"
text_ned = """
Het Bunker and Batbox Mapping Project is een toegewijd initiatief dat zich richt op het grondig documenteren en analyseren van de verspreiding van vleermuisroostplaatsen op het eiland Terchelling tijdens de cruciale winterslaapperiode. Dit project omvat het nauwkeurig in kaart brengen van de locaties van verschillende bunkers en vleermuiskasten verspreid over het eiland. Naast het in kaart brengen voeren we uitgebreide onderzoeken uit die niet alleen de aangetroffen vleermuissoorten identificeren, maar ook belangrijke omgevingsgegevens vastleggen, zoals temperatuur- en vochtigheidsniveaus die op het moment van elke waarneming zijn waargenomen.

Ons primaire doel is om de ingewikkelde relaties tussen vleermuispopulaties en hun omringende omgevingskenmerken te onthullen. Door inzicht te krijgen in deze dynamiek, hopen we belangrijke kenmerken te identificeren die bijdragen aan het voortbestaan ​​en welzijn van vleermuissoorten in het gebied.

We nodigen gepassioneerde ecologen en natuurliefhebbers van harte uit om zich bij ons aan te sluiten in dit gezamenlijke onderzoeksproject. Als u geïnteresseerd bent om deel uit te maken van dit opwindende project en meer wilt weten over hoe u kunt meedoen, aarzel dan niet om contact met ons op te nemen voor meer informatie. Uw betrokkenheid kan een groot verschil maken in ons begrip en behoud van deze opmerkelijke wezens.
"""

title_ita = "Progetto di mappatura di bunker e batbox"
text_ita = """
Il Bunker and Batbox Mapping Project è un'iniziativa dedicata incentrata sulla documentazione e l'analisi approfondita della distribuzione dei rifugi dei pipistrelli sull'isola di Terchelling durante il cruciale periodo di letargo. Questo progetto prevede la mappatura meticolosa delle posizioni di vari bunker e batbox sparsi sull'isola. Oltre alla mappatura, conduciamo indagini approfondite che non solo identificano le specie di pipistrelli incontrate, ma registrano anche importanti dati ambientali, come i livelli di temperatura e umidità osservati al momento di ogni avvistamento.

Il nostro obiettivo principale è scoprire le complesse relazioni tra le popolazioni di pipistrelli e le caratteristiche ambientali circostanti. Acquisendo informazioni su queste dinamiche, speriamo di identificare le caratteristiche chiave che contribuiscono alla sopravvivenza e al benessere delle specie di pipistrelli nella zona.

Invitiamo calorosamente ecologi appassionati e amanti della natura a unirsi a noi in questo sforzo di ricerca collaborativo. Se sei interessato a far parte di questo entusiasmante progetto e desideri saperne di più su come puoi essere coinvolto, non esitare a contattarci per ulteriori informazioni. Il tuo coinvolgimento potrebbe fare una differenza significativa nella nostra comprensione e conservazione di queste straordinarie creature.
"""

title_esp = "Proyecto de mapeo de búnkeres y cajas para murciélagos"
text_esp = """
El Proyecto de Mapeo de Búnkeres y Cajas para Murciélagos es una iniciativa dedicada a documentar y analizar minuciosamente la distribución de los refugios de murciélagos en la isla de Terchelling durante el crucial período de hibernación. Este proyecto implica mapear meticulosamente las ubicaciones de varios búnkeres y cajas para murciélagos dispersos por toda la isla. Junto con el mapeo, realizamos estudios exhaustivos que no solo identifican las especies de murciélagos encontradas, sino que también registran datos ambientales importantes, como los niveles de temperatura y humedad observados en el momento de cada avistamiento.

Nuestro objetivo principal es descubrir las intrincadas relaciones entre las poblaciones de murciélagos y las características ambientales que las rodean. Al obtener información sobre estas dinámicas, esperamos identificar características clave que contribuyen a la supervivencia y el bienestar de las especies de murciélagos en el área.

Invitamos cordialmente a los ecologistas apasionados y entusiastas de la naturaleza a unirse a nosotros en este esfuerzo de investigación colaborativa. Si está interesado en ser parte de este emocionante proyecto y desea obtener más información sobre cómo puede participar, no dude en comunicarse con nosotros para obtener más información. Su participación podría marcar una diferencia significativa en nuestra comprensión y conservación de estas notables criaturas.
"""


#---APP---
tab1, tab2, tab3, tab4 = st.tabs(["🇬🇧", "🇳🇱", "🇪🇸", "🇮🇹"])

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

