import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="VIP Credit Systems",
    page_icon="💳",
    layout="wide"
)

# Function to authenticate the user
def authenticate(username, password):
    # Demo credentials: username = 'user', password = 'pass'
    return username == "user" and password == "pass"

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Sidebar for login
if not st.session_state.authenticated:
    with st.sidebar:
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
else:
    # Sidebar with logo and navigation prompt
    with st.sidebar:
        st.image("logooo.png", use_column_width=True)
        st.success("Select a page above.")

    # Main content
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        # Main page logo at the top of the headers
        st.image("logooo.png", use_column_width=True)

        # App Header
        st.title("VIP Credit Systems")
        st.subheader("Your Comprehensive Credit Management Solution")

        # Introduction
        st.write("""
        Welcome to **VIP Credit Systems**, where managing your credit has never been easier. Our system provides a wide range of tools and insights to help you understand and optimize your credit profile. Below is a detailed list of features we offer to assist you in taking control of your financial future.
        """)

        # Feature List with Descriptions
        st.markdown("""
        ## Features:
        
        ### Credit Overview
        - 📊 **Credit Score Overview**
        - 💳 **Credit Utilization**
        - 🗓️ **Payment History**
        - 📑 **Credit Report Summary**

        ### Account Management
        - 🔍 **Credit Inquiries**
        - 🎯 **Credit Limits**
        - ⚖️ **Debt-to-Income Ratio**
        - 💰 **Loan and Credit Card Balances**

        ### Analytics and Insights
        - ⏳ **Account Age**
        - 💵 **Monthly Payments**
        - 📂 **Credit Accounts Breakdown**
        - 🏆 **Top 5 Highest Balances**

        ### Transactions and Payments
        - 📝 **Top 5 Recent Transactions**
        - 📅 **Upcoming Payments**
        - 🔄 **Credit Utilization by Account Type**
        - 📈 **Average Payment History**

        ### Trends and Forecasting
        - 📊 **Credit Score Trend**
        - 💸 **Monthly Spending Trend**
        - 📉 **Credit Score vs. Credit Utilization**
        - 📅 **Debt Repayment Schedule**

        ### Credit Management Tools
        - 🆕 **New Credit Accounts**
        - 🧠 **Credit Score Impact Simulation**
        - 📉 **Debt Reduction Plan**
        - 💡 **Credit Score Improvement Tips**

        ### Customization and Alerts
        - ⚠️ **Alerts and Recommendations**
        - ✏️ **Edit Credit Info**
        - 📤 **Export Data**
        """)

        # Conclusion
        st.write("""
        Explore these features and more in the VIP Credit Systems app. Whether you are looking to improve your credit score, manage your debts, or simply stay on top of your financial health, we've got you covered. Start making informed financial decisions today!
        """)

if __name__ == "__main__":
    # You can add any initialization code here if needed
    pass
