import streamlit as st

def authenticate(username, password):
    if username == "user" and password == "pass":
        return True
    return False

def show_login_page():
    st.title("Login")
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")
        
        if login_button:
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.experimental_rerun()  # Rerun the app to display the main content
            else:
                st.error("Invalid username or password")
