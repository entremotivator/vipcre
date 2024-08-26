import streamlit as st
import requests

# WordPress site URL and JWT endpoints
WP_URL = "https://your-wordpress-site.com"  # Replace with your actual WordPress URL
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"

def authenticate(username, password):
    """Authenticate user and return True if successful, otherwise False."""
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
    """Display the login page form."""
    st.title("WordPress Login")
    
    with st.form(key='login_form'):
        st.write("Enter your WordPress credentials below.")
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
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
                st.error("Both username and password are required.")

def main_page():
    """Display the main content after successful login."""
    st.title("Welcome!")
    st.write("You are successfully logged in. This is the main content area.")

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    main_page()  # Show the main page if authenticated
else:
    show_login_page()  # Show the login form if not authenticated
