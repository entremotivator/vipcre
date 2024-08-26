import streamlit as st
import requests

# WordPress site URL and JWT endpoints
WP_URL = "https://vipbusinesscredit.com"
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"
REGISTER_ENDPOINT = f"{WP_URL}/wp-json/wp/v2/users/register"

def authenticate(username, password):
    try:
        response = requests.post(JWT_ENDPOINT, data={'username': username, 'password': password})
        if response.status_code == 200:
            st.session_state.jwt_token = response.json().get('token')
            return True
        else:
            st.error(f"Login failed: {response.json().get('message')}")
            return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

def register(username, password, email):
    try:
        response = requests.post(REGISTER_ENDPOINT, data={
            'username': username,
            'password': password,
            'email': email
        })
        if response.status_code == 201:
            st.success("Registration successful! Please log in.")
        else:
            st.error(f"Registration failed: {response.json().get('message')}")
    except Exception as e:
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
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

    if st.button("Sign Up"):
        show_signup_page()

def show_signup_page():
    st.title("Sign Up")
    with st.form(key='signup_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        signup_button = st.form_submit_button("Sign Up")

        if signup_button:
            register(username, password, email)

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    show_login_page()
else:
    st.write("Welcome to the main content!")

