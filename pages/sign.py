import streamlit as st
from wordpress_auth import WordpressAuth

def main():
    # Sidebar configuration input
    st.sidebar.title("Configuration")
    wordpress_url = st.sidebar.text_input("WordPress Site URL", placeholder="https://yourwordpressurl.com")
    api_key = st.sidebar.text_input("API Key", type="password")

    if wordpress_url and api_key:
        # Initialize the WordPressAuth instance
        auth = WordpressAuth(api_key=api_key, base_url=wordpress_url)

        # Check if the user is already logged in
        if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
            st.title("Welcome to the Application")
            st.write("You are logged in!")
        else:
            # Show the login form
            st.title("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Log In"):
                token = auth.get_token(username, password)
                if token and auth.verify_token(token):
                    st.session_state['token'] = token  # Store token in session state
                    st.success("Logged in successfully!")
                    st.experimental_rerun()  # Reload to show content
                else:
                    st.error("Invalid username or password.")
    else:
        st.warning("Please enter your WordPress URL and API key in the sidebar.")

    # Logout button
    if 'token' in st.session_state and st.sidebar.button("Log Out"):
        del st.session_state['token']  # Remove token from session state
        st.experimental_rerun()  # Reload to show login form

if __name__ == "__main__":
    main()
