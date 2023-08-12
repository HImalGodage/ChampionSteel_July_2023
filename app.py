import streamlit as st
import streamlit.components.v1 as components

import time

# st.set_page_config(layout='wide')
st.set_page_config(page_title='Champion Steel', layout = 'wide', initial_sidebar_state = 'auto')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)
st.title("CHAMPION STEEL - BUSINESS PERFORMANCE AS OF JULY 2023", anchor=None)
# bootstrap 4 collapse example
with st.spinner('Wait for it...'):
    time.sleep(0.1)
components.html(

    """
    <iframe title="Report Section" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiM2YyODUyNGUtODM5Yy00YjY2LWI4YTItZTY3ODBmNTI3ZGJhIiwidCI6IjE0NzUxNTliLTAwNmEtNGZiNC1iYjBiLTk2MWNlZWFlMTI4YyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>
  
    
    """,
    height=768,
    width=1366
)

