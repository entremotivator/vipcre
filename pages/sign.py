import streamlit as st
import requests

# Retrieve configurations from Streamlit secrets
WP_URL = st.secrets["wordpress"]["wp_url"]
JWT_ENDPOINT = f"{WP_URL}{st.secrets['wordpress']['jwt_endpoint']}"
REGISTER_ENDPOINT = f"{WP_URL}{st.secrets['wordpress']['register_endpoint']}"

def authenticate(username, password):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(JWT_ENDPOINT, json={'username': username, 'password': password}, headers=headers)
        
        if response.status_code == 200:
            st.session_state.jwt_token = response.json().get('token')
            return True
        else:
            error_message = response.json().get('message', 'Unknown error occurred')
            st.error(f"Login failed: {error_message}")
            return False
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return False

def register(username, password, email):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(REGISTER_ENDPOINT, json={
            'username': username,
            'password': password,
            'email': email
        }, headers=headers)

        if response.status_code == 201:
            st.success("Registration successful! Please log in.")
        else:
            error_message = response.json().get('message', 'Unknown error occurred')
            st.error(f"Registration failed: {error_message}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")

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

def show_signup_page():
    st.title("Sign Up")
    with st.form(key='signup_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        signup_button = st.form_submit_button("Sign Up")

        if signup_button:
            if username and password and email:
                register(username, password, email)
            else:
                st.error("All fields are required")

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Display content based on authentication status
if st.session_state.authenticated:
    st.write("Welcome to the main content!")  # Replace this with your main content or functionality
else:
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.write("")

    with col2:
        show_login_page()
        st.write("")  # Space between Login and Sign Up

        if st.button("Sign Up"):
            show_signup_page()

    with col3:
        st.write("")
