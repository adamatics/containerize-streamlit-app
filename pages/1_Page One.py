import streamlit as st

from utils.utils import add_session_state, update_session_states

update_session_states()

st.set_page_config(
    page_title="Page One - Advanced Streamlit app",
    page_icon=":slightly_smiling_face:",  # path to your logo
    layout="wide",
)

st.title("Page One")
st.markdown("Welcome to Page One!")
st.write(f"Your role is {st.session_state.role}")
add_session_state("STATE", "state")
