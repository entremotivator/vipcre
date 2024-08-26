import streamlit as st
import requests

# WordPress site and endpoint
WP_SITE_URL = "https://vipbusinesscredit.com"
JWT_AUTH_URL = f"{WP_SITE_URL}/wp-json/jwt-auth/v1/token"

def authenticate(username, password):
    """Authenticate the user with WordPress JWT."""
    response = requests.post(JWT_AUTH_URL, data={'username': username, 'password': password})
    if response.status_code == 200:
        token = response.json().get('token')
        if token:
            st.session_state.token = token
            return True
        else:
            st.error("Authentication failed: Token not received.")
    else:
        st.error(f"Authentication failed: {response.status_code} - {response.text}")
    return False

def show_login_page():
    st.title("Login / Sign Up")

    login_mode = st.radio("Select your mode", ["Login", "Sign Up"])
    
    if login_mode == "Login":
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

    elif login_mode == "Sign Up":
        st.warning("Sign up is not supported directly through this interface. Please register through the WordPress site.")

if __name__ == "__main__":
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if 'token' not in st.session_state:
        st.session_state.token = None

    if st.session_state.authenticated:
        st.title("Welcome to the main content!")
        # Your main app content here
    else:
        show_login_page()
