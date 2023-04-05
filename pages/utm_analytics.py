import streamlit as st
import pandas as pd
import numpy as np

st.title('Scopri da dove provengono i tuoi clienti di ritorno, i tuoi clienti nuovi e se stai pagando due volte per un cliente che hai già pagato')
st.markdown("""
Per scoprire da dove provengono i tuoi clienti nuovi e di ritorno, carica due file CSV, uno con i dati clienti e uno con i dati di Google Analytics.

Nel primo file devi avere queste quattro colonne, con questo esatto nome:

- order_id	
- customer_id : Deve contenere o Nome e Cognome del cliente oppure ID oppure email
- order_total : il totale pagato. Non deve avere il simbolo dell'euro e come segno decimale deve avere il punto
- order_date : data di ordine con il formato YYYY-MM-DD

""")

file=st.file_uploader('Carica il tuo file CSV Clienti',key="clienti")
file_path='https://docs.google.com/spreadsheets/d/1stEgE4vlaY65MPQ1obn5MFUwLcbc2JMlwv8Dd5W2PIY/export?format=csv'
st.markdown(f'<a href="{file_path}" download> Clicca qui per scaricare un CSV di esempio</a>', unsafe_allow_html=True)
st.write("") 
st.write("")

st.markdown("""
Nel secondo file che avrai dopo aver fatto l'export da Google Analytics di tutti gli ordini da sempre devi avere queste due colonne, con questo esatto nome:

- order_id	
- Source / Medium

""")

analytics=st.file_uploader('Carica il tuo file CSV con Sorgente e Mezzo',key="analytics")
analytics_path='https://docs.google.com/spreadsheets/d/1HAT0wEaqq0amfRjUiI0SdevkoezsO31X0VFs9ULTNbM/export?format=csv'
video_path='https://www.loom.com/share/f059b1daa7204eb0b345362e18e3e7d4'
st.markdown(f'<a href="{analytics_path}" download> Clicca qui per scaricare un CSV di esempioe</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{video_path}"> Clicca qui per vedere come fare questo export da Universal Analytics</a>', unsafe_allow_html=True)
st.write("") 
st.write("")
button=st.button('Invia i tuo file')

if button:
    googleanalytics=pd.read_csv(analytics)
    order=pd.read_csv(file)
    order['order_date']=pd.to_datetime(order['order_date'])
    resultdf=order.merge(googleanalytics,how="outer",on="order_id")
    first_order_date = resultdf.groupby("customer_id")["order_date"].min()
    resultdf["primo_ordine"] = resultdf["customer_id"].map(first_order_date)
    resultdf['tipo']=np.where(resultdf['order_date']== resultdf['primo_ordine'], 'New', 'Recurring')
    pivot = resultdf.pivot_table(index=['tipo','Source / Medium'],values='order_id',aggfunc='count')
    st.table(pivot)