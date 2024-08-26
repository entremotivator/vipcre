import streamlit as st
import requests

# WordPress site URL and JWT endpoints
WP_URL = "https://vipbusinesscredit.com"
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"
REGISTER_ENDPOINT = f"{WP_URL}/wp-json/wp/v2/users/register"

def authenticate(username, password):
    try:
        # Adding necessary headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        # Sending a POST request to the JWT Authentication endpoint
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
        # Sending a POST request to the registration endpoint
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
        login_button = st.form_submit_button


