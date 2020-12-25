
from re import split
import streamlit as st
import spacy
from spacy_syllables import SpacySyllables

nlp = spacy.load('es_core_news_sm')
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after='tagger')

st.title('Poematronic')
st.subheader('el ayudante del poeta')

col1, col2 = st.beta_columns(2)

with col1:
    poema = st.text_area('vuela poeta...', key='poema', height=500)

with col2:
    versos = split('\n', poema)

    poema_contado = []
    for verso in versos:  
        doc = nlp(verso)
        verso_n = [
        (token.text, token._.syllables, token._.syllables_count)
        for token in doc
        ]
        verso_s = sum( [x[2] for x in verso_n if type(x[2]) == int])
        poema_contado.append(verso + ' (' + str(verso_s) + ')')
    p = '<br>'
    poema_contado = p.join(poema_contado)


    st.markdown('<br>' + poema_contado, unsafe_allow_html=True)


