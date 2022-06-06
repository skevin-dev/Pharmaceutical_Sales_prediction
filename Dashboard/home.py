import streamlit as st

def app():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:1.5rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:2rem;border-radius:0.5rem;'>Rossmann Pharmaceuticals Sales Forecasting</p>", unsafe_allow_html=True)
    
        st.markdown("<p style='font-size:1rem'>With about 56,200 employees and over 4000 locations across Europe, Dirk Rossmann GmbH (commonly known as Rossmann) is one of Europe's major drugstore companies.</p>", unsafe_allow_html=True)

        st.markdown("<p style='font-size:1rem'>The Rosemann pharmaceutical firm can examine sales estimates for its stores six weeks in advance, as well as projected patterns, thanks to this app, which is an end-to-end solution.</p>",unsafe_allow_html=True)
