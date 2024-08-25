import streamlit as st

# Set page configuration with a custom page title and icon
st.set_page_config(
    page_title="VIP Credit Systems",
    page_icon="💳",
)

# Sidebar with logo and navigation prompt
st.sidebar.image("logooo.png", use_column_width=True)
st.sidebar.success("Select a page above.")

# App Header
st.title("VIP Credit Systems")
st.subheader("Your Comprehensive Credit Management Solution")

# Introduction
st.write("""
Welcome to **VIP Credit Systems**, where managing your credit has never been easier. Our system provides a wide range of tools and insights to help you understand and optimize your credit profile. Below is a detailed list of features we offer to assist you in taking control of your financial future.
""")

# Feature List with Descriptions
st.markdown("""
### Features:
... (remaining content is the same) ...
""")

# Conclusion
st.write("""
Explore these features and more in the VIP Credit Systems app. Whether you are looking to improve your credit score, manage your debts, or simply stay on top of your financial health, we’ve got you covered. Start making informed financial decisions today!
""")
