import streamlit as st

# Function to authenticate the user
def authenticate(username, password):
    return username == "user" and password == "pass"

# Set page configuration
st.set_page_config(page_title="Login")

# Title
st.title("Login")

# Login form
with st.form(key='login_form'):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")
    
    if login_button:
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.success("Login successful!")
            st.experimental_rerun()  # Rerun to show the authenticated view
        else:
            st.error("Invalid username or password")
