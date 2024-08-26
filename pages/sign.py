import streamlit as st
import requests

# WordPress site URL and JWT endpoints
WP_URL = "https://vipbusinesscredit.com"
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"
REGISTER_ENDPOINT = f"{WP_URL}/wp-json/wp/v2/users/register"

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

def show_login_form():
    st.title("Login")
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Log In")

        if login_button:
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.experimental_rerun()  # Reload the page to show the main content
            else:
                st.error("Invalid username or password")

def show_signup_form():
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

def main_page():
    st.write("Welcome to the main content!")

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    main_page()  # Show the main page if authenticated
else:
    # Show login or signup options
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.write("")  # Spacer

    with col2:
        option = st.radio("Select an option", ["Log In", "Sign Up"])
        
        if option == "Log In":
            show_login_form()
        elif option == "Sign Up":
            show_signup_form()

    with col3:
        st.write("")  # Spacer


