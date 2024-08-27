import streamlit as st
from wordpress_auth import WordpressAuth

def get_user_input():
    """Retrieve and validate user configuration settings."""
    st.sidebar.title("Configuration Settings")
    base_url = st.sidebar.text_input("WordPress Site URL", placeholder="https://vipbusinesscredit.com/")
    api_key = st.sidebar.text_input("API Key", type="password")
    return base_url, api_key

def logout():
    """Handle user logout."""
    if 'token' in st.session_state:
        del st.session_state['token']  # Remove the token from session state
        st.experimental_rerun()  # Reload the page to show the login form again

# Use Streamlit secrets for sensitive data (ensure secrets.toml is configured)
base_url = st.secrets["base_url"]
api_key = st.secrets["api_key"]

# Initialize the WordPressAuth instance
auth = WordpressAuth(api_key=api_key, base_url=base_url)

# Create a page navigation selector
page = st.sidebar.selectbox("Select Page", ["Login", "Main", "Additional", "Page 4", "Page 5"])

# Route to different pages based on selection
if page == "Login":
    import pages.login as login
    if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
        st.sidebar.success("You are already logged in.")
        st.sidebar.button("Log Out", on_click=logout)
        st.sidebar.markdown("---")
        st.write("You are already logged in. Select a different page or log out.")
    else:
        login.render(auth, base_url)
elif page == "Main":
    import pages.main as main
    if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
        main.render()
    else:
        st.warning("You need to log in to access this page.")
        import pages.login as login
        login.render(auth, base_url)
elif page == "Additional":
    import pages.additional as additional
    if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
        additional.render()
    else:
        st.warning("You need to log in to access this page.")
        import pages.login as login
        login.render(auth, base_url)
elif page == "Page 4":
    import pages.page4 as page4
    if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
        page4.render()
    else:
        st.warning("You need to log in to access this page.")
        import pages.login as login
        login.render(auth, base_url)
elif page == "Page 5":
    import pages.page5 as page5
    if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
        page5.render()
    else:
        st.warning("You need to log in to access this page.")
        import pages.login as login
        login.render(auth, base_url)

# Optional logout button
if 'token' in st.session_state:
    st.sidebar.button("Log Out", on_click=logout)
