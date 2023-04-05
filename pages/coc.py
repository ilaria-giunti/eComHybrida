import streamlit as st
import pandas as pd

st.title('Scopri il Numero di Ordini medio che fanno i tuoi clienti')
st.markdown("""
Per scoprire il numero di ordini che fa in media un cliente, carica un file CSV con le seguenti colonne con questo esatto nome:

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
    df=pd.read_csv(file)
    df['order_date']=pd.to_datetime(df['order_date'])
    df=df.groupby('customer_id')['order_id'].count()
    coc=df.mean().round(2)

    st.write(f'I tuoi clienti fanno in media {coc} ordini')