import streamlit as st
import pandas as pd
import numpy as np

st.title('Scopri il prodotto che se comprato come primo ti genera un LTV più alto')
st.markdown("""
Per scoprire il prodotto con LTV più alto, carica due file CSV, uno con i dati clienti e uno con i dati prodotto.

Nel primo file devi avere queste quattro colonne, con questo esatto nome:

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

st.markdown("""
Nel secondo file devi avere queste due colonne, con questo esatto nome:

- order_id	
- Product Name

""")

product=st.file_uploader('Carica il tuo file CSV Clienti',key="product")
product_path='https://docs.google.com/spreadsheets/d/1J7k65uQaWLoURVecgJZJ7TvB8qMUXPtXZHr_sXPe0BU/export?format=csv'
st.markdown(f'<a href="{product_path}" download> Clicca qui per scaricare un CSV di esempioe</a>', unsafe_allow_html=True)
st.write("") 
st.write("")
button=st.button('Invia i tuo file')

if button:
    df_prodotto=pd.read_csv(product)
    df_clienti=pd.read_csv(file) 
    first_order_date = df_clienti.groupby("customer_id")["order_date"].min()
    df_clienti["primo_ordine"] = df_clienti["customer_id"].map(first_order_date)
    df_clienti['order_type'] = np.where(df_clienti['order_date'] == df_clienti['primo_ordine'], 'New', 'Recurring')
    ltv = df_clienti.groupby("customer_id")["order_total"].sum()
    df_clienti["ltv"] = df_clienti["customer_id"].map(ltv)
    df2=df_clienti[df_clienti['order_type']=='New']
    resultdf=df_prodotto.merge(df2,how="inner",on="order_id")
    prodotto=resultdf.groupby("Product Name")["order_total"].mean().round(2)
    prodotto=prodotto.sort_values(ascending=False)
    prodotto2=resultdf.groupby("Product Name")["order_id"].count()
    prodotto2 = prodotto2.sort_values(ascending=False)
    
    st.write('Ecco i prodotti con LTV più alto')
    st.table(prodotto.head())

    st.write('Ecco i prodotti che sono stati acquistati più spesso da Nuovi Clienti')
    st.table(prodotto2.head())