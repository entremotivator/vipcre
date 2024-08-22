import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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
        "New Credit Accounts": np.random.randint(0, 3, size=12),
        "Credit Limits": np.random.randint(5000, 20000, size=12),
        "Payment History": np.random.choice(["On Time", "Late"], size=12, p=[0.9, 0.1])
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
    "Debt-to-Income Ratio",
    "Monthly Payments",
    "New Credit Accounts",
])

# Display selected page
if page == "Credit Score Overview":
    st.subheader("Credit Score Overview")
    st.write(f"Current Credit Score: {df['Credit Score'].iloc[-1]}")
    st.line_chart(df[['Date', 'Credit Score']].set_index('Date'))

    # Add trend analysis
    st.subheader("Credit Score Trend Analysis")
    st.write("Your credit score has been trending as follows:")
    trend = "increasing" if df['Credit Score'].pct_change().mean() > 0 else "decreasing"
    st.write(f"Overall trend: {trend}")

    # Edit Credit Score
    st.subheader("Edit Credit Score")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0)
    new_score = st.number_input("Enter New Credit Score", min_value=300, max_value=850, value=int(df['Credit Score'].iloc[index_to_edit]))
    if st.button("Update Credit Score"):
        df.at[index_to_edit, 'Credit Score'] = new_score
        st.success(f"Credit Score updated for {df['Date'].iloc[index_to_edit]}")

elif page == "Credit Utilization":
    st.subheader("Credit Utilization")
    st.bar_chart(df[['Date', 'Credit Utilization']].set_index('Date'))

    # Add utilization analysis
    avg_utilization = df['Credit Utilization'].mean()
    st.write(f"Average Credit Utilization: {avg_utilization:.2%}")
    st.write("A utilization rate below 30% is generally recommended.")

    # Edit Credit Utilization
    st.subheader("Edit Credit Utilization")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0)
    new_utilization = st.slider("Enter New Credit Utilization", min_value=0.0, max_value=1.0, value=float(df['Credit Utilization'].iloc[index_to_edit]))
    if st.button("Update Credit Utilization"):
        df.at[index_to_edit, 'Credit Utilization'] = new_utilization
        st.success(f"Credit Utilization updated for {df['Date'].iloc[index_to_edit]}")

elif page == "Payment History":
    st.subheader("Payment History")
    st.write(df[['Date', 'Payment History']].set_index('Date'))

    # Add payment history analysis
    late_payments = df[df['Payment History'] == "Late"].shape[0]
    st.write(f"Number of Late Payments: {late_payments}")
    st.write("Keep your payments on time to maintain a healthy credit score.")

    # Edit Payment History
    st.subheader("Edit Payment History")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0)
    new_history = st.selectbox("Select Payment History", ["On Time", "Late"], index=0 if df['Payment History'].iloc[index_to_edit] == "On Time" else 1)
    if st.button("Update Payment History"):
        df.at[index_to_edit, 'Payment History'] = new_history
        st.success(f"Payment History updated for {df['Date'].iloc[index_to_edit]}")

elif page == "Debt-to-Income Ratio":
    st.subheader("Debt-to-Income Ratio")
    st.line_chart(df[['Date', 'Debt-to-Income Ratio']].set_index('Date'))

    # Add ratio interpretation
    st.write("A lower debt-to-income ratio indicates better financial health.")
    high_ratio = df['Debt-to-Income Ratio'].max()
    st.write(f"Highest Recorded Ratio: {high_ratio:.2%}")

    # Edit Debt-to-Income Ratio
    st.subheader("Edit Debt and Income")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0)
    new_debt = st.number_input("Enter New Total Debt", min_value=0, max_value=100000, value=int(df['Total Debt'].iloc[index_to_edit]))
    new_income = st.number_input("Enter New Income", min_value=0, max_value=100000, value=int(df['Income'].iloc[index_to_edit]))
    if st.button("Update Debt and Income"):
        df.at[index_to_edit, 'Total Debt'] = new_debt
        df.at[index_to_edit, 'Income'] = new_income
        df.at[index_to_edit, 'Debt-to-Income Ratio'] = new_debt / new_income
        st.success(f"Debt and Income updated for {df['Date'].iloc[index_to_edit]}")

elif page == "Monthly Payments":
    st.subheader("Monthly Payments")
    st.line_chart(df[['Date', 'Monthly Payments']].set_index('Date'))

    # Add payment pattern analysis
    st.write("Monitoring your payment amounts helps in budgeting effectively.")
    avg_payment = df['Monthly Payments'].mean()
    st.write(f"Average Monthly Payment: ${avg_payment:.2f}")

    # Edit Monthly Payments
    st.subheader("Edit Monthly Payments")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0)
    new_payment = st.number_input("Enter New Monthly Payment", min_value=0, max_value=10000, value=int(df['Monthly Payments'].iloc[index_to_edit]))
    if st.button("Update Monthly Payment"):
        df.at[index_to_edit, 'Monthly Payments'] = new_payment
        st.success(f"Monthly Payments updated for {df['Date'].iloc[index_to_edit]}")

elif page == "New Credit Accounts":
    st.subheader("New Credit Accounts")
    st.line_chart(df[['Date', 'New Credit Accounts']].set_index('Date'))

    # Add analysis on new credit accounts
    st.write("Opening new credit accounts can temporarily lower your credit score.")
    total_new_accounts = df['New Credit Accounts'].sum()
    st.write(f"Total New Credit Accounts in the Period: {total_new_accounts}")

    # Edit New Credit Accounts
    st.subheader("Edit New Credit Accounts")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0)
    new_accounts = st.number_input("Enter New Credit Accounts", min_value=0, max_value=10, value=int(df['New Credit Accounts'].iloc[index_to_edit]))
    if st.button("Update New Credit Accounts"):
        df.at[index_to_edit, 'New Credit Accounts'] = new_accounts
        st.success(f"New Credit Accounts updated for {df['Date'].iloc[index_to_edit]}")

