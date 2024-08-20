import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Generate sample data
def generate_sample_data():
    dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
    
    data = {
        "Date": dates,
        "Credit Score": np.random.randint(650, 850, size=12),
        "Credit Utilization": np.random.uniform(0.2, 0.9, size=12),
        "Total Debt": np.random.randint(1000, 5000, size=12),
        "Monthly Payments": np.random.randint(100, 1000, size=12),
        "Income": np.random.randint(3000, 7000, size=12),
        "New Credit Accounts": np.random.randint(0, 3, size=12)
    }
    
    df = pd.DataFrame(data)
    df["Debt-to-Income Ratio"] = df["Total Debt"] / df["Income"]
    
    return df

df = generate_sample_data()

# Streamlit app
st.title("Credit Management Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Credit Score Overview",
    "Credit Utilization",
    "Payment History",
    "Credit Report Summary",
    "Credit Inquiries",
    "Credit Limits",
    "Debt-to-Income Ratio",
    "Loan and Credit Card Balances",
    "Account Age",
    "Monthly Payments",
    "Credit Accounts Breakdown",
    "Top 5 Highest Balances",
    "Top 5 Recent Transactions",
    "Upcoming Payments",
    "Credit Utilization by Account Type",
    "Average Payment History",
    "Credit Score Trend",
    "Monthly Spending Trend",
    "Credit Score vs. Credit Utilization",
    "Debt Repayment Schedule",
    "New Credit Accounts",
    "Credit Score Impact Simulation",
    "Debt Reduction Plan",
    "Credit Score Improvement Tips",
    "Alerts and Recommendations"
])

# Display selected page
if page == "Credit Score Overview":
    st.subheader("Credit Score Overview")
    st.write(f"Current Credit Score: {df['Credit Score'].iloc[-1]}")
    st.line_chart(df[['Date', 'Credit Score']].set_index('Date'))
    
elif page == "Credit Utilization":
    st.subheader("Credit Utilization")
    st.bar_chart(df[['Date', 'Credit Utilization']].set_index('Date'))
    
elif page == "Payment History":
    st.subheader("Payment History")
    st.write(df[['Date', 'Monthly Payments']].set_index('Date'))
    
elif page == "Credit Report Summary":
    st.subheader("Credit Report Summary")
    st.write("This section would include a detailed summary of your credit report.")
    
elif page == "Credit Inquiries":
    st.subheader("Credit Inquiries")
    st.write("This section would display recent credit inquiries.")
    
elif page == "Credit Limits":
    st.subheader("Credit Limits")
    st.write("This section would show your credit limits per account.")
    
elif page == "Debt-to-Income Ratio":
    st.subheader("Debt-to-Income Ratio")
    st.line_chart(df[['Date', 'Debt-to-Income Ratio']].set_index('Date'))
    
elif page == "Loan and Credit Card Balances":
    st.subheader("Loan and Credit Card Balances")
    st.write("This section would display your loan and credit card balances.")
    
elif page == "Account Age":
    st.subheader("Account Age")
    st.write("This section would display the age of your credit accounts.")
    
elif page == "Monthly Payments":
    st.subheader("Monthly Payments")
    st.line_chart(df[['Date', 'Monthly Payments']].set_index('Date'))
    
elif page == "Credit Accounts Breakdown":
    st.subheader("Credit Accounts Breakdown")
    st.write("This section would break down your credit accounts by type.")
    
elif page == "Top 5 Highest Balances":
    st.subheader("Top 5 Highest Balances")
    st.write("This section would list the top 5 highest balances.")
    
elif page == "Top 5 Recent Transactions":
    st.subheader("Top 5 Recent Transactions")
    st.write("This section would list the top 5 recent transactions.")
    
elif page == "Upcoming Payments":
    st.subheader("Upcoming Payments")
    st.write("This section would show upcoming payment dates.")
    
elif page == "Credit Utilization by Account Type":
    st.subheader("Credit Utilization by Account Type")
    st.write("This section would display credit utilization by account type.")
    
elif page == "Average Payment History":
    st.subheader("Average Payment History")
    st.write("This section would show your average payment history.")
    
elif page == "Credit Score Trend":
    st.subheader("Credit Score Trend")
    st.line_chart(df[['Date', 'Credit Score']].set_index('Date'))
    
elif page == "Monthly Spending Trend":
    st.subheader("Monthly Spending Trend")
    st.bar_chart(df[['Date', 'Total Debt']].set_index('Date'))
    
elif page == "Credit Score vs. Credit Utilization":
    st.subheader("Credit Score vs. Credit Utilization")
    fig = px.scatter(df, x="Credit Utilization", y="Credit Score", title="Credit Score vs. Credit Utilization")
    st.plotly_chart(fig)
    
elif page == "Debt Repayment Schedule":
    st.subheader("Debt Repayment Schedule")
    st.write("This section would show your debt repayment schedule.")
    
elif page == "New Credit Accounts":
    st.subheader("New Credit Accounts")
    st.line_chart(df[['Date', 'New Credit Accounts']].set_index('Date'))
    
elif page == "Credit Score Impact Simulation":
    st.subheader("Credit Score Impact Simulation")
    st.write("This section would simulate the impact of various actions on your credit score.")
    
elif page == "Debt Reduction Plan":
    st.subheader("Debt Reduction Plan")
    st.write("This section would outline your debt reduction plan.")
    
elif page == "Credit Score Improvement Tips":
    st.subheader("Credit Score Improvement Tips")
    st.write("This section would provide tips for improving your credit score.")
    
elif page == "Alerts and Recommendations":
    st.subheader("Alerts and Recommendations")
    st.write("This section would show alerts and recommendations for improving credit.")

# Run the app
if __name__ == "__main__":
    st.run()
