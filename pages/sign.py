import requests
import streamlit as st

# Set up the page layout
st.set_page_config(layout="wide")

# Retrieve the API key from Streamlit's secrets management
API_KEY = st.secrets["wordpress_api_key"]  # Store your API key in Streamlit secrets

# WordPress site URL and JWT endpoints
WP_URL = "https://vipbusinesscredit.com"
JWT_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token"
TOKEN_VALIDATE_ENDPOINT = f"{WP_URL}/wp-json/jwt-auth/v1/token/validate"

def get_token(username, password):
    try:
        # Fetch the IP address from query parameters if available
        ip_address = st.experimental_get_query_params().get('ip', [None])[0]
        
        response = requests.post(
            JWT_ENDPOINT,
            json={'username': username, 'password': password, 'ip_address': ip_address},
            headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            return response.json().get('token')
        else:
            st.error(f"Failed to get token: {response.json().get('message', 'Unknown error')}")
            return None
    except requests.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

def verify_token(token):
    try:
        ip_address = st.experimental_get_query_params().get('ip', [None])[0]
        
        response = requests.post(
            TOKEN_VALIDATE_ENDPOINT,
            headers={'Authorization': f'Bearer {token}', 'X-API-KEY': API_KEY},
            json={'ip_address': ip_address}
        )
        
        return response.status_code == 200
    except requests.RequestException as e:
        st.error(f"An error occurred: {e}")
        return False

def main():
    st.write("Welcome to the main content of the application!")  # Main page content

# Check if the user is already logged in
if 'token' in st.session_state and verify_token(st.session_state['token']):
    main()  # Call the main function
else:
    # Show the login form
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        with st.form(key='login_form'):
            st.title("Please log in")
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            submit_button = st.form_submit_button(label='Log in')

            if submit_button:
                token = get_token(username, password)
                if token and verify_token(token):
                    st.session_state['token'] = token  # Store the token in session state
                    st.experimental_rerun()  # Reload the page to reflect login status
                else:
                    st.error('Access denied')

    with col3:
        st.write("")
