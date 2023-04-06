import streamlit as st
import pandas as pd
import numpy as np

st.title('Ottieni LTV generale e a 90 giorni')
st.markdown("""
Per ottenere queste info, carica un file CSV con le seguenti colonne con questo esatto nome:
- order_id	
- customer_id : Deve contenere o Nome e Cognome del cliente oppure ID oppure email
- order_total : il totale pagato. Non deve avere il simbolo dell'euro e come segno decimale deve avere il punto
- order_date : data di ordine con il formato YYYY-MM-DD
""")
file=st.file_uploader('Carica il tuo file CSV Clienti')
file_path='https://docs.google.com/spreadsheets/d/1stEgE4vlaY65MPQ1obn5MFUwLcbc2JMlwv8Dd5W2PIY/export?format=csv'
st.markdown(f'<a href="{file_path}" download> Clicca qui per scaricare un CSV di esempioe</a>', unsafe_allow_html=True)
st.write("") 
st.write("") 

button=st.button('Invia i tuoi dati')
if button:
    df = pd.read_csv(file)
    df['order_date'] = pd.to_datetime(df['order_date']) # Convert 'order_date' to datetime
    df['primo_ordine'] = df.groupby('customer_id')['order_date'].transform('min') # Add 'primo_ordine' column
    
    ltv90= df[(df["order_date"] - df["primo_ordine"]).dt.days <= 90].groupby("customer_id")["order_total"].sum()
    df["lt_90"]=df["customer_id"].map(ltv90)
    
    ltv_90days=ltv90.mean().round(2)
    st.write(f'il LTV a 90 giorni dei tuoi clienti è {ltv_90days}€')
    
    ltvnormal=df.groupby("customer_id")["order_total"].sum()
    ltv=ltvnormal.mean()
    st.write(f'il LTV generale dei tuoi clienti è {ltv}€')
