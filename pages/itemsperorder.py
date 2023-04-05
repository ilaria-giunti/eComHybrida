import streamlit as st
import pandas as pd
import numpy as np

st.title('Scopri il numero di prodotti che un cliente acquista per ordine')
st.markdown("""
Per scoprire il numero di prodotti acquistati per ordine in media, carica un file CSV con queste due colonne, con questo esatto nome:

- order_id	
- Product Name

""")

product=st.file_uploader('Carica il tuo file CSV Clienti',key="product")
product_path='https://docs.google.com/spreadsheets/d/1J7k65uQaWLoURVecgJZJ7TvB8qMUXPtXZHr_sXPe0BU/export?format=csv'
st.markdown(f'<a href="{product_path}" download> Clicca qui per scaricare un CSV di esempioe</a>', unsafe_allow_html=True)
st.write("") 
st.write("")
button=st.button('Invia il tuo file')

if button:
    df_prodotto=pd.read_csv(product)
    df.dropna()
    df=df.groupby("order_id")["Product Name"].count()
    items=df.mean().round(2)
    st.write(f"in media i tuoi clienti acquistano {items} prodotti per ordine")
