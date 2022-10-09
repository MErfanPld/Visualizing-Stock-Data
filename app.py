#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
from PIL import Image


# In[6]:


st.write('''
# visualizing stock data
''')

img = Image.open('/home/erfan/Desktop/Stock WebApp/trading.jpg')
st.image(img,width=400, caption="visualizing stock data")

st.sidebar.header('Input Data')


# In[13]:


def get_input():
    numb=st.sidebar.text_input('N Last Days',50)
    stock_symbol=st.sidebar.text_input('insert stock symbol','FOOLAD')
    return stock_symbol , numb


# In[14]:


def get_company_name(symbol):
    if symbol=='FOOLAD':
        return 'FOOLAD'
    elif symbol== 'KHODRO':
        return 'KHODRO'
    elif symbol== 'AMZN':
        return 'AMAZON'
    elif symbol=='TSLA':
        return 'TESLA'
    else :
        'NONE'


# In[15]:


def get_data(symbol,n):
    if symbol.upper()=='FOOLAD':
        df=pd.read_csv('/home/erfan/Desktop/Stock WebApp/foolad.csv')
    elif symbol.upper()=='KHODRO':
        df=pd.read_csv('/home/erfan/Desktop/Stock WebApp/khodro.csv')
    elif symbol.upper()=='AMZN':
        df=pd.read_csv('/home/erfan/Desktop/Stock WebApp/amzn.csv')
    elif symbol.upper()=='TSLA':
        df=pd.read_csv('/home/erfan/Desktop/Stock WebApp/tsla.csv')
    else:
        df=pd.DataFrame(columns=['Date','First','High','Low','Close','Value','Volume','Openint','Per','Open','last'])
        
    df=df.set_index(pd.DatetimeIndex(df['Date'].values))
    n= int(n)
    df=df.head(n)
    return df


# In[17]:


symbol , n = get_input()
df=get_data(symbol,n)
company=get_company_name(symbol.upper())

st.header(company + ' Close Price\n')
st.line_chart(df['Close'])

st.header(company + ' Volume\n')
st.line_chart(df['Volume'])

st.header('Stock Datas')

st.write(df.describe())


# In[ ]:




