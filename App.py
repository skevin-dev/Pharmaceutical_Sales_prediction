import streamlit as st
from multiapp import MultipleApp
from Dashboard import display_traindataset,home

app = MultipleApp()

st.sidebar.markdown('# **Pharmaceutical Sales forcasting**')
st.sidebar.markdown("""
The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality.
""")

# Add all your application here
app.add_app("Homepage", home.app)
app.add_app("Datasets", display_traindataset.app)

# The main app
app.run()