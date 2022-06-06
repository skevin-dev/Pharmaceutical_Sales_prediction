import streamlit as st
import pandas as pd

@st.cache
def load_train():
    df = pd.read_csv('./data/train.csv',low_memory=False)
    return df 

@st.cache
def loadtest():
    df = pd.read_csv('./data/test.csv')
    return df 

def app():
    st.title('In this page we display datasets')
    
    with st.spinner("Loading Data ..."):
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:2rem;border-radius:0.8rem;'>Data display page</p>", unsafe_allow_html=True)
     
        st.markdown("<p style='font-size:1rem'>The report includes sales statistics from 1,115 Rossmann outlets over the years.</p>", unsafe_allow_html=True)

        st.markdown("<p style='font-size:1rem'>This challenge's data and feature description can be found at https://www.kaggle.com/c/rossmann-store-sales.</p>",unsafe_allow_html=True)
        
        
        st.header('Training Data')
        train = load_train()
        st.write(train, width=1200)
        
        st.header('Testing Data')
        test = loadtest()
        st.write(test)