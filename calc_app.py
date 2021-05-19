import streamlit as st
from multiapp import MultiApp
from apps import home, calculator # import your app modules here

app = MultiApp()

st.markdown("""
Ahmad Moiz
# Simple Calculator
""")

st.text("Use Drop Down menu below to navigate between Homepage and Calculator.")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Calculator", calculator.app)
# The main app
app.run()