import streamlit as st
import requests
import webbrowser

# WordPress site URL and JWT endpoints
WP_URL = "https://vipbusinesscredit.com"
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"
SIGNUP_URL = f"{WP_URL}/register"  # Assuming this is the sign-up page URL

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

def show_login_signup_page():
    st.title("Welcome to VIP Business Credit")
    
    # Tabs for Login and Sign Up
    tab_login, tab_signup = st.tabs(["Login", "Sign Up"])
    
    # Login Tab
    with tab_login:
        st.header("Login")
        with st.form(key='login_form'):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
    
            if login_button:
                if authenticate(username, password):
                    st.session_state.authenticated = True
                    st.success("Login successful!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")

    # Sign Up Tab
    with tab_signup:
        st.header("Sign Up")
        st.markdown("To create a new account, please click the button below to visit our registration page.")
        if st.button("Go to Sign Up Page"):
            webbrowser.open_new_tab(SIGNUP_URL)

# Ensure user is not already authenticated
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Show login/signup page if not authenticated, else show main content
if not st.session_state.authenticated:
    show_login_signup_page()
else:
    st.write("Welcome to the main content!")
