import streamlit as st
import requests

# Define the URL for JWT login
WORDPRESS_LOGIN_URL = "https://vipbusinesscredit.com/?rest_route=/simple-jwt-login/v1/autologin"

def authenticate(email):
    # Prepare the URL with email as a query parameter
    url = f"{https://vipbusinesscredit.com/wp-admin}&JWT=email={email}"
    
    # Make a request to the WordPress endpoint
    response = requests.get(url)
    
    # Check if authentication was successful
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Authentication failed. Please check your email.")
        return None

def main():
    st.title("WordPress JWT Authentication")

    # Input field for user email
    email = st.text_input("Enter your email address")

    # Button to submit email for authentication
    if st.button("Log In"):
        if email:
            # Call authenticate function
            result = authenticate(email)
            if result:
                st.success("Login successful!")
                st.write(result)
            else:
                st.error("Login failed.")
        else:
            st.error("Please enter an email address.")

if __name__ == "__main__":
    main()
        show_login_page()
