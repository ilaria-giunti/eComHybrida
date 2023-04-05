import streamlit as st
import pandas as pd
import numpy as np

st.title('Scopri AOV dei clienti nuovi e dei clienti di ritorno')
st.markdown("""
Per scoprire l'AOV da clienti nuovi e di ritorno, carica un file CSV con le seguenti colonne con questo esatto nome:

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
    first_order_date = df.groupby("customer_id")["order_date"].min()
    df["primo_ordine"] = df["customer_id"].map(first_order_date)
    df['order_type'] = np.where(df['order_date'] == df['primo_ordine'], 'New', 'Recurring')
    df2=df.groupby('order_type')['order_total','order_id'].agg({'order_total': 'sum', 'order_id': 'count'})
    df2['aov']=round(df2['order_total']/(df2['order_id']),2)

    st.table(df2)