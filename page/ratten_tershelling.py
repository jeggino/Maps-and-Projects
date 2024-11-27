import streamlit as st
from css import *
from constants import *


#---LAYOUT---
st.markdown(collapsedControl,unsafe_allow_html=True,)
st.markdown(header_hidden,unsafe_allow_html=True)
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


#---COSTANTS---
img = "images/rats_1.jpg"
link = "https://ratten-terschelling-dashboard.streamlit.app/"

title_eng = "The invasion of the common rat (Rattus norvegicus) on Terschelling: first eradication efforts"
text_eng = """
This map illustrates the efforts to eradicate the common rat invasion on Terschelling. Terschelling is known for its diverse wildlife and is particularly important for nesting birds, as many species rely on the island's ground-level habitats to raise their young. Unfortunately, these nests are highly vulnerable to predation by the invasive rat population. Until recently, the island was largely free of rats; however, a few individuals may have accidentally arrived by boat from the mainland, prompting urgent action.

Two types of traps are being employed to control the rat population, followed by procedures to remove them. Additionally, camera traps are being set up in the field to monitor signs of rodent activity. From mid-November, a brigade of hunters has been organized to actively hunt and suppress the rat population.

We hope that with the support of the province of Friesland, our efforts will successfully eradicate this invasive species before the bird breeding season begins.
"""

title_ned = "De invasie van de gewone rat (Rattus norvegicus) op Terschelling: eerste uitroeiingsinspanningen"
text_ned = """
Deze kaart illustreert de inspanningen om de veelvoorkomende rattenplaag op Terschelling uit te roeien. Terschelling staat bekend om zijn gevarieerde fauna en is met name belangrijk voor broedende vogels, aangezien veel soorten afhankelijk zijn van de habitats op de begane grond van het eiland om hun jongen groot te brengen. Helaas zijn deze nesten zeer kwetsbaar voor predatie door de invasieve rattenpopulatie. Tot voor kort was het eiland grotendeels vrij van ratten; echter, een paar exemplaren zijn mogelijk per ongeluk per boot van het vasteland aangekomen, wat aanleiding gaf tot dringende actie.

Er worden twee soorten vallen gebruikt om de rattenpopulatie te beheersen, gevolgd door procedures om ze te verwijderen. Daarnaast worden er cameravallen in het veld opgezet om tekenen van knaagdieractiviteit te monitoren. Vanaf half november is er een brigade van jagers georganiseerd om actief te jagen en de rattenpopulatie te onderdrukken.

We hopen dat we met de steun van de provincie Friesland deze invasieve soort met succes zullen uitroeien voordat het broedseizoen van de vogels begint.
"""

title_ita = "L'invasione del ratto comune (Rattus norvegicus) su Terschelling: primi sforzi di eradicazione"
text_ita = """
Questa mappa illustra gli sforzi per sradicare la comune invasione di ratti a Terschelling. Terschelling è nota per la sua fauna selvatica diversificata ed è particolarmente importante per gli uccelli nidificanti, poiché molte specie si affidano agli habitat a livello del suolo dell'isola per crescere i loro piccoli. Sfortunatamente, questi nidi sono altamente vulnerabili alla predazione da parte della popolazione di ratti invasivi. Fino a poco tempo fa, l'isola era in gran parte priva di ratti; tuttavia, alcuni individui potrebbero essere arrivati ​​accidentalmente in barca dalla terraferma, il che ha richiesto un'azione urgente.

Per controllare la popolazione di ratti vengono impiegati due tipi di trappole, seguite da procedure per rimuoverli. Inoltre, vengono installate trappole fotografiche sul campo per monitorare i segni di attività dei roditori. Da metà novembre, è stata organizzata una brigata di cacciatori per cacciare attivamente e sopprimere la popolazione di ratti.

Ci auguriamo che con il supporto della provincia della Frisia, i nostri sforzi sradichino con successo questa specie invasiva prima che inizi la stagione riproduttiva degli uccelli.
"""

title_esp = "La invasión de la rata común (Rattus norvegicus) en Terschelling: primeros esfuerzos de erradicación"
text_esp = """
Este mapa ilustra los esfuerzos para erradicar la invasión de ratas comunes en Terschelling. Terschelling es conocida por su diversa fauna y es particularmente importante para las aves que anidan, ya que muchas especies dependen de los hábitats a nivel del suelo de la isla para criar a sus crías. Desafortunadamente, estos nidos son muy vulnerables a la depredación por parte de la población invasora de ratas. Hasta hace poco, la isla estaba prácticamente libre de ratas; sin embargo, es posible que algunos ejemplares hayan llegado accidentalmente en barco desde el continente, lo que ha obligado a tomar medidas urgentes.

Se están utilizando dos tipos de trampas para controlar la población de ratas, seguidos de procedimientos para eliminarlas. Además, se están instalando cámaras trampa en el campo para monitorear los signos de actividad de roedores. Desde mediados de noviembre, se ha organizado una brigada de cazadores para cazar activamente y suprimir la población de ratas.

Esperamos que con el apoyo de la provincia de Frisia, nuestros esfuerzos logren erradicar con éxito esta especie invasora antes de que comience la temporada de reproducción de las aves.
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

st.link_button(":rainbow[Link dashboard]", link,icon='🐀')
"---"
