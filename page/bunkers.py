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
The Bunker and Batbox Mapping Project focuses on documenting bat roosts on Terchelling during hibernation. We are mapping the locations of bunkers and batboxes while conducting surveys to identify bat species and collect environmental data like temperature and humidity.

Our goal is to understand the relationship between bat populations and their environment, identifying key factors for their survival. 

We invite ecologists and nature enthusiasts to join us in this research effort. If you're interested in participating or want to learn more, please reach out. Your contribution could significantly advance our understanding and conservation of bats."""

title_ned = "Bunker & vleermuiskasten in kaart brengen project"
text_ned = """
Het Bunker and Batbox Mapping Project richt zich op het documenteren van vleermuisroosts op Terchelling tijdens de winterslaap. We brengen de locaties van bunkers en vleermuiskasten in kaart terwijl we onderzoeken uitvoeren om vleermuissoorten te identificeren en omgevingsgegevens zoals temperatuur en vochtigheid te verzamelen.

Ons doel is om de relatie tussen vleermuispopulaties en hun omgeving te begrijpen en sleutelfactoren voor hun overleving te identificeren.

We nodigen ecologen en natuurliefhebbers uit om zich bij ons aan te sluiten bij dit onderzoeksproject. Als u geïnteresseerd bent in deelname of meer wilt weten, neem dan contact met ons op. Uw bijdrage kan ons begrip en behoud van vleermuizen aanzienlijk vergroten.
"""

title_ita = "Progetto di mappatura di bunker e batbox"
text_ita = """
Il Bunker and Batbox Mapping Project si concentra sulla documentazione dei rifugi dei pipistrelli a Terchelling durante il letargo. Stiamo mappando le posizioni dei bunker e delle batbox mentre conduciamo indagini per identificare le specie di pipistrelli e raccogliere dati ambientali come temperatura e umidità.

Il nostro obiettivo è comprendere la relazione tra le popolazioni di pipistrelli e il loro ambiente, identificando i fattori chiave per la loro sopravvivenza.

Invitiamo ecologi e amanti della natura a unirsi a noi in questo sforzo di ricerca. Se sei interessato a partecipare o vuoi saperne di più, contattaci. Il tuo contributo potrebbe far progredire significativamente la nostra comprensione e conservazione dei pipistrelli.
"""

title_esp = "Proyecto de mapeo de búnkeres y cajas para murciélagos"
text_esp = """
El proyecto de mapeo de búnkeres y cajas para murciélagos se centra en documentar los refugios de murciélagos en Terchelling durante la hibernación. Estamos mapeando las ubicaciones de búnkeres y cajas para murciélagos mientras realizamos estudios para identificar especies de murciélagos y recolectar datos ambientales como temperatura y humedad.

Nuestro objetivo es comprender la relación entre las poblaciones de murciélagos y su entorno, identificando factores clave para su supervivencia.

Invitamos a los ecologistas y entusiastas de la naturaleza a unirse a nosotros en este esfuerzo de investigación. Si está interesado en participar o desea obtener más información, comuníquese con nosotros. Su contribución podría hacer avanzar significativamente nuestra comprensión y conservación de los murciélagos.
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

