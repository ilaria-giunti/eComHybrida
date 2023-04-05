import streamlit as st
import pandas as pd

st.title('Scopri il Tempo di riacquisto dei tuoi clienti')
st.markdown("""
Per scoprire quanto impiega una persona a fare un secondo o un terzo ordine, carica un file CSV con le seguenti colonne con questo esatto nome:

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
    first_order_date = df.groupby("customer_id")["order_date"].min()
    df["primo_ordine"] = df["customer_id"].map(first_order_date)
    second_order_date=df.groupby('customer_id')['order_date'].nsmallest(2).groupby(level='customer_id').last()
    df["secondo_ordine"] = df["customer_id"].map(second_order_date)
    third_order_date=df.groupby('customer_id')['order_date'].nsmallest(3).groupby(level='customer_id').last()
    df["terzo_ordine"] = df['customer_id'].map(third_order_date)
    df['tempo_1-2acquisto']=(df['secondo_ordine']-df['primo_ordine'])
    df['tempo_2-3acquisto']=df['terzo_ordine']-df['secondo_ordine']
    Average1_2acquisto=pd.Timedelta(pd.to_timedelta(df['tempo_1-2acquisto']).mean())
    Average1_2acquisto=Average1_2acquisto.days

    Average2_3acquisto=pd.Timedelta(pd.to_timedelta(df['tempo_2-3acquisto']).mean())
    Average2_3acquisto=Average2_3acquisto.days

    st.write(f'Tra il 1° ed il 2°Acquisto passano {Average1_2acquisto} giorni')
    st.write(f'Tra il 2° ed il 3°Acquisto passano {Average2_3acquisto} giorni')