import streamlit as st
import pandas as pd

st.title('Benvenuto!')
st.write('Scegli dal Menù a sinistra cosa vuoi fare')

loom_embed_url = "https://www.loom.com/embed/1b9ab8c05cec4351859af027a0a3a7b2"

st.markdown('Se hai bisogno di una mano per usare questo tool, guarda il video')
st.markdown(f'<iframe src="{loom_embed_url}" style="width:100%; height:400px; border:none;" allowfullscreen></iframe>', unsafe_allow_html=True)
