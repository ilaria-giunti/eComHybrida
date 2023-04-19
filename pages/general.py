import streamlit as st
import pandas as pd
import numpy as np

st.title('Ottieni le info generali sui tuoi clienti, tasso di riacquisto ecc.')
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

budget=st.number_input('Inserisci qui il budget speso negli ultimi 3 mesi')

button=st.button('Invia i tuoi dati')
if button:
    df = pd.read_csv(file)
    df['order_date'] = pd.to_datetime(df['order_date'])

    df2=df
    client = df2['customer_id'].nunique()

    orders_per_customer = df.groupby('customer_id')['order_id'].count()
    dueordini = (orders_per_customer > 1).sum()
    treordini = (orders_per_customer > 2).sum()
    reprate_12 = round(dueordini / client *100,2)
    reprate_23 = round(treordini / dueordini *100,2)

    df3=df
    df3['mese'] = df3['order_date'].dt.strftime('%Y-%m')
    first_order_date = df3.groupby("customer_id")["order_date"].min()
    df3["primo_ordine"] = df3["customer_id"].map(first_order_date)
    df3['order_type'] = np.where(df3['order_date'] == df3['primo_ordine'], 'New', 'Recurring')
    data=df3[df3['order_type']=='New'].groupby('mese')['order_id'].count()
    nuoviclienti=np.mean(data.iloc[-3:])
    CAC=round(budget/nuoviclienti,2)

    df4=df
    df4['mese'] = df4['order_date'].dt.strftime('%Y-%m')
    first_order_date = df4.groupby("customer_id")["order_date"].min()
    df4["primo_ordine"] = df4["customer_id"].map(first_order_date)
    df4['order_type'] = np.where(df4['order_date'] == df4['primo_ordine'], 'New', 'Recurring')
    data2=df4[df4['order_type']=='New'].groupby('mese')['order_id'].count()
    nuoviclienti=np.mean(data2.iloc[-3:])
    CAC=round(budget/nuoviclienti,2)

    df5=df
    first_order_date = df5.groupby("customer_id")["order_date"].min()
    df5["primo_ordine"] = df5["customer_id"].map(first_order_date)
    df5['order_type'] = np.where(df5['order_date'] == df5['primo_ordine'], 'New', 'Recurring')
    data3=df5.groupby('order_type')['order_total','order_id'].agg({'order_total': 'sum', 'order_id': 'count'})
    data3['aov']=round(data3['order_total']/(data3['order_id']),2)


    st.write(f'Nel tuo Database hai {client} clienti')
    st.write (f'Il {reprate_12}% dele persone fa più di un ordine')
    st.write (f'Il {reprate_23}% dele persone che ha fatto un ordine, ha fatto almeno un secondo ordine')
    st.write(f'Negli ultimi 3 mesi hai avuto un CAC di {CAC}€')
    st.table(data3)


