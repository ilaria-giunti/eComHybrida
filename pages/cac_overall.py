import streamlit as st
import pandas as pd
import numpy as np
st.title('Scopri il tuo CAC Overall negli ultimi 3 mesi')

st.markdown("""
Per scoprire il CAC Overall, inserisci il budget speso negli ultimi 3 mesi e carica un file CSV con le seguenti colonne con questo esatto nome:

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
budget=st.number_input('Inserisci qui il budget speso negli ultimi 3 mesi')

button=st.button('Invia il tuo file')
if button:
    df=pd.read_csv(file)
    df['order_date']=pd.to_datetime(df['order_date'])
    df['mese'] = df['order_date'].dt.strftime('%Y-%m')
    first_order_date = df.groupby("customer_id")["order_date"].min()
    df["primo_ordine"] = df["customer_id"].map(first_order_date)
    df['order_type'] = np.where(df['order_date'] == df['primo_ordine'], 'New', 'Recurring')
    df2=df[df['order_type']=='New'].groupby('mese')['order_id'].count()
    nuoviclienti=np.mean(df2.iloc[-3:])
    CAC=round(budget/nuoviclienti,2)
    st.write(f'Negli ultimi 3 mesi hai avuto un CAC di {CAC}€')