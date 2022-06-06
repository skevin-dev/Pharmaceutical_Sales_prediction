import streamlit as st
import pandas as pd

def app():
    st.title('In this page we display datasets')
    
    with st.spinner("Loading Data ..."):
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:2rem;border-radius:0.8rem;'>Data display page</p>", unsafe_allow_html=True)
     
        st.markdown("<p style='font-size:1rem'>The report includes sales statistics from 1,115 Rossmann outlets over the years.</p>", unsafe_allow_html=True)

        st.markdown("<p style='font-size:1rem'>This challenge's data and feature description can be found at https://www.kaggle.com/c/rossmann-store-sales.</p>",unsafe_allow_html=True)
        
        
#         @st.cache
        st.header('Training Data')
        train = pd.read_csv('./data/train.csv',low_memory=False)
        st.write(train, width=1200)
        
        st.header('Testing Data')
        test = pd.read_csv('./data/test.csv')
        st.write(test)