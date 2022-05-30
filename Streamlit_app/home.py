import streamlit as st

import pandas as pd 
import numpy as np 

train_data = pd.read_csv('./data/train-data.csv')
test_data = pd.read_csv('./data/test-data.csv')

st.title('Pharmaceutical Sales')

if set.checkbox('Train data'):
    st.subheader('Training Dataset')
    st.write(train_data)
    
if set.checkbox('Test data'):
    st.subheader('Testing dataset')
    st.write(test_data)
    
    
