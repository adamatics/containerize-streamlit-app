import streamlit as st


def add_session_state(state: str, value):
    """Add a new state to the Streamlit session."""
    if state not in st.session_state:
        st.session_state[state] = value


def update_session_states():
    """Reload Streamlit session states. This is useful when you want to keep the session states between pages."""
    for k, v in st.session_state.items():
        st.session_state[k] = v
