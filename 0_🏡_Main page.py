import streamlit as st

from utils.utils import add_session_state, update_session_states

update_session_states()

st.set_page_config(
    page_title="Main page - Advanced Streamlit app",
    page_icon=":slightly_smiling_face:",  # path to your logo
    layout="wide",
)

main_wdgt = dict()


def init_app():
    session_states = {
        "APP_TITLE": "Advanced Streamlit app",
        "LOGO_PATH": ":slightly_smiling_face:",
        "COMPANY_NAME": "Cool ApS",
    }
    for state, value in session_states.items():
        add_session_state(state, value)


def make_page():
    st.title("This is an advanced Streamlit app")
    st.markdown(
        """
        Cool features:
        - Multiple pages. Use the sidebar to navigate.
        - Share data and states across pages using `st.session_state`.
        - Placeholder-based layout. Access the widgets as variables.
        """
    )

    st.divider()
    main_wdgt["lft_col"], main_wdgt["mid_col"], main_wdgt["rgt_col"] = st.columns([1, 2, 1])
    with main_wdgt["lft_col"]:
        st.markdown(
            """
            My name is `main_wdgt['lft_col']`.
            I am the left-most widget in a column-based layout.
            """
        )
    with main_wdgt["mid_col"]:
        st.markdown(
            """
            My name is `main_wdgt['mid_col']`.
            I am the central widget in a column-based layout. I am also bigger than my peers.
            """
        )
    with main_wdgt["rgt_col"]:
        st.markdown(
            """
            My name is `main_wdgt['rgt_col']`.
            I am the right-most widget in a column-based layout.
            """
        )

    st.divider()
    main_wdgt["role_option_text"] = st.empty()
    with main_wdgt["role_option_text"]:
        st.markdown("Select your role, and go to Page One.")
    main_wdgt["role_option"] = st.empty()
    with main_wdgt["role_option"]:
        st.selectbox(
            label="Roles",
            options=("Developer", "Engineer", "Scientist", "Rockstar"),
            index=None,
            placeholder="Choose your role...",
            key="role",
        )


def main():
    init_app()
    make_page()
    add_session_state("main_wdgt", main_wdgt)


if __name__ == "__main__":
    main()
