import streamlit as st
import pandas as pd

st.title('Benvenuto!')
st.write('Scegli dal Menù a sinistra cosa vuoi fare')

loom_embed_url = "https://www.loom.com/embed/1b9ab8c05cec4351859af027a0a3a7b2"

st.markdown('Se hai bisogno di una mano per usare questo tool, guarda il video')
st.markdown(f'<iframe src="{loom_embed_url}" style="width:100%; height:400px; border:none;" allowfullscreen></iframe>', unsafe_allow_html=True)

video_path='https://www.loom.com/share/521b9bfc03844421b556776dc7a6bac2'
st.markdown(f'<a href="{video_path}"> Clicca qui per vedere come fare questo export Clienti da Shopify</a>', unsafe_allow_html=True)

video_wordpress='https://www.loom.com/share/ac8bebac1793447f938806725dc4fd5c'
st.markdown(f'<a href="{video_wordpress}"> Clicca qui per vedere come fare questo export Clienti da Woocommerce</a>', unsafe_allow_html=True)
