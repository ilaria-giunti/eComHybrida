import streamlit as st
import pandas as pd

st.title('Scopri quanti clienti hai a Database!')

st.markdown("""
Se vuoi semplicemente sapere quanti clienti hai in Database, carica qui un file CSV con le seguenti colonne:

- order_id	
- customer_id : Deve contenere o Nome e Cognome del cliente oppure ID oppure email
- order_total : il totale pagato. Non deve avere il simbolo dell'euro e come segno decimale deve avere il punto
- order_date : data di ordine con il formato YYYY-MM-DD

""")

file=st.file_uploader('Carica il tuo file CSV Clienti',key="clienti")
file_path='https://docs.google.com/spreadsheets/d/1stEgE4vlaY65MPQ1obn5MFUwLcbc2JMlwv8Dd5W2PIY/export?format=csv'
st.markdown(f'<a href="{file_path}" download> Clicca qui per scaricare un CSV di esempioe</a>', unsafe_allow_html=True)
st.write("") 
st.write("")
button=st.button('Invia il tuo file')
if button:
    df = pd.read_csv(file)
    df['order_date'] = pd.to_datetime(df['order_date'])
    client = df['customer_id'].nunique()

    st.write(f'Nel tuo Database hai {client} clienti')