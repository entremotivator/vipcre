import streamlit as st
from wordpress_auth import WordpressAuth

def get_user_input():
    with st.sidebar:
        st.title("Configuration Settings")
        base_url = st.text_input("WordPress Site URL", placeholder="https://yourwordpressurl.com")
        api_key = st.text_input("API Key", type="password")
        return base_url, api_key

def main_page():
    st.title("Welcome to the Application")
    st.write("This is the main content of the application.")
    # Additional main page content can be added here.

def login_page(auth):
    st.title("Please Log In")
    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Log In')

        if submit_button:
            token = auth.get_token(username, password)
            if token and auth.verify_token(token):
                st.session_state['token'] = token  # Store the token in the session state
                st.success("Logged in successfully!")
                st.experimental_rerun()  # Reload the page to show the main content
            else:
                st.error('Access denied. Please check your credentials and try again.')

# Sidebar for configuration
base_url, api_key = get_user_input()

if base_url and api_key:
    # Initialize the WordPressAuth instance
    auth = WordpressAuth(api_key=api_key, base_url=base_url)
    
    # Check if the user is already logged in
    if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
        main_page()  # User is authenticated, show the main page
    else:
        login_page(auth)  # Show the login form
else:
    st.warning("Please enter the WordPress site URL and API key in the sidebar.")

# Optionally, add a logout button
if 'token' in st.session_state:
    if st.sidebar.button('Log Out'):
        del st.session_state['token']  # Remove the token from session state
        st.experimental_rerun()  # Reload the page to show the login form again
