import streamlit as st
import requests

# WordPress site URL and JWT endpoints
WP_URL = "https://your-wordpress-site.com"
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"

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

def show_login_page():
    st.title("WordPress Login")
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Log In")

        if login_button:
            if username and password:
                if authenticate(username, password):
                    st.success("Login successful!")
                    st.session_state.authenticated = True
                    st.experimental_rerun()  # Reload the page to show the main content
                else:
                    st.error("Invalid username or password")
            else:
                st.error("Username and password are required")

def main_page():
    st.write("Welcome to the main content! You are successfully logged in.")

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    main_page()  # Show the main page if authenticated
else:
    show_login_page()  # Show the login form if not authenticated
