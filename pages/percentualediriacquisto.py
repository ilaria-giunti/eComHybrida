import streamlit as st
import pandas as pd
import numpy as np
st.title('Scopri quanti clienti fanno più di un ordine e quanti più di due ordini')

st.markdown("""
Per scoprire quanti clienti fanno più di un ordine e quanti fanno più di due ordine, carica un file CSV con le seguenti colonne con questo esatto nome:

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

button=st.button('Invia il tuo file')
if button:
    df = pd.read_csv(file)
    df['order_date'] = pd.to_datetime(df['order_date'])
    client = df['customer_id'].nunique()
    orders_per_customer = df.groupby('customer_id')['order_id'].count()
    dueordini = (orders_per_customer > 1).sum()
    treordini = (orders_per_customer > 2).sum()
    reprate_12 = round(dueordini / client *100,2)
    reprate_23 = round(treordini / dueordini *100,2)

    st.write (f'Il {reprate_12}% dele persone fa più di un ordine')
    st.write (f'Il {reprate_23}% dele persone che ha fatto 2 ordini, ha fatto almeno un terzo ordine')
