import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64

# Generate sample data for multiple accounts
def generate_sample_data(account_id):
    dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
    
    data = {
        "Date": dates,
        "Account ID": account_id,
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

# Combine data from multiple accounts
def combine_data(account_ids):
    return pd.concat([generate_sample_data(account_id) for account_id in account_ids])

account_ids = [f"Account {i}" for i in range(1, 4)]
df = combine_data(account_ids)

# Sidebar for account selection and navigation
st.sidebar.title("Navigation")
selected_account = st.sidebar.selectbox("Select Account", account_ids)
page = st.sidebar.radio("Go to", [
    "Credit Score Overview",
    "Credit Utilization",
    "Payment History",
    "Debt-to-Income Ratio",
    "Monthly Payments",
    "New Credit Accounts",
    "Edit Credit Info"
])

# Filter data for selected account
df_filtered = df[df['Account ID'] == selected_account]

# Export data to CSV
def export_data(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{selected_account}_credit_data.csv">Download {selected_account} Credit Data</a>'
    return href

# Display selected page
if page == "Credit Score Overview":
    st.subheader("Credit Score Overview")
    st.write(f"Current Credit Score for {selected_account}: {df_filtered['Credit Score'].iloc[-1]}")
    st.line_chart(df_filtered[['Date', 'Credit Score']].set_index('Date'))

    st.subheader("Credit Score Trend Analysis")
    trend = "increasing" if df_filtered['Credit Score'].pct_change().mean() > 0 else "decreasing"
    st.write(f"Overall trend: {trend}")

    st.subheader("Edit Credit Score")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='score_index')
    new_score = st.number_input("Enter New Credit Score", min_value=300, max_value=850, value=int(df_filtered['Credit Score'].iloc[index_to_edit]), key='new_score')
    if st.button("Update Credit Score"):
        df.loc[df_filtered.index[index_to_edit], 'Credit Score'] = new_score
        st.success(f"Credit Score updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Credit Utilization":
    st.subheader("Credit Utilization")
    st.bar_chart(df_filtered[['Date', 'Credit Utilization']].set_index('Date'))

    avg_utilization = df_filtered['Credit Utilization'].mean()
    st.write(f"Average Credit Utilization: {avg_utilization:.2%}")
    st.write("A utilization rate below 30% is generally recommended.")

    st.subheader("Edit Credit Utilization")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='util_index')
    new_utilization = st.slider("Enter New Credit Utilization", min_value=0.0, max_value=1.0, value=float(df_filtered['Credit Utilization'].iloc[index_to_edit]), key='new_utilization')
    if st.button("Update Credit Utilization"):
        df.loc[df_filtered.index[index_to_edit], 'Credit Utilization'] = new_utilization
        st.success(f"Credit Utilization updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Payment History":
    st.subheader("Payment History")
    st.write(df_filtered[['Date', 'Payment History']].set_index('Date'))

    late_payments = df_filtered[df_filtered['Payment History'] == "Late"].shape[0]
    st.write(f"Number of Late Payments: {late_payments}")

    st.subheader("Edit Payment History")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='history_index')
    new_history = st.selectbox("Select Payment History", ["On Time", "Late"], index=0 if df_filtered['Payment History'].iloc[index_to_edit] == "On Time" else 1, key='new_history')
    if st.button("Update Payment History"):
        df.loc[df_filtered.index[index_to_edit], 'Payment History'] = new_history
        st.success(f"Payment History updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Debt-to-Income Ratio":
    st.subheader("Debt-to-Income Ratio")
    st.line_chart(df_filtered[['Date', 'Debt-to-Income Ratio']].set_index('Date'))

    st.write("A lower debt-to-income ratio indicates better financial health.")
    high_ratio = df_filtered['Debt-to-Income Ratio'].max()
    st.write(f"Highest Recorded Ratio: {high_ratio:.2%}")

    st.subheader("Edit Debt and Income")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='debt_index')
    new_debt = st.number_input("Enter New Total Debt", min_value=0, max_value=100000, value=int(df_filtered['Total Debt'].iloc[index_to_edit]), key='new_debt')
    new_income = st.number_input("Enter New Income", min_value=0, max_value=100000, value=int(df_filtered['Income'].iloc[index_to_edit]), key='new_income')
    if st.button("Update Debt and Income"):
        df.loc[df_filtered.index[index_to_edit], 'Total Debt'] = new_debt
        df.loc[df_filtered.index[index_to_edit], 'Income'] = new_income
        df.loc[df_filtered.index[index_to_edit], 'Debt-to-Income Ratio'] = new_debt / new_income
        st.success(f"Debt and Income updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Monthly Payments":
    st.subheader("Monthly Payments")
    st.line_chart(df_filtered[['Date', 'Monthly Payments']].set_index('Date'))

    avg_payment = df_filtered['Monthly Payments'].mean()
    st.write(f"Average Monthly Payment: ${avg_payment:.2f}")

    st.subheader("Edit Monthly Payments")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='payment_index')
    new_payment = st.number_input("Enter New Monthly Payment", min_value=0, max_value=10000, value=int(df_filtered['Monthly Payments'].iloc[index_to_edit]), key='new_payment')
    if st.button("Update Monthly Payment"):
        df.loc[df_filtered.index[index_to_edit], 'Monthly Payments'] = new_payment
        st.success(f"Monthly Payments updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "New Credit Accounts":
    st.subheader("New Credit Accounts")
    st.line_chart(df_filtered[['Date', 'New Credit Accounts']].set_index('Date'))

    total_new_accounts = df_filtered['New Credit Accounts'].sum()
    st.write(f"Total New Credit Accounts in the Period: {total_new_accounts}")

    st.subheader("Edit New Credit Accounts")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='accounts_index')
    new_accounts = st.number_input("Enter New Credit Accounts", min_value=0, max_value=10, value=int(df_filtered['New Credit Accounts'].iloc[index_to_edit]), key='new_accounts')
    if st.button("Update New Credit Accounts"):
        df.loc[df_filtered.index[index_to_edit], 'New Credit Accounts'] = new_accounts
        st.success(f"New Credit Accounts updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Edit Credit Info":
    st.subheader("Edit Credit Info for All Accounts")
    
    account_to_edit = st.selectbox("Select Account to Edit", account_ids)
    metric_to_edit = st.selectbox("Select Metric to Edit", df.columns[2:])
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='edit_info_index')
    new_value = st.number_input(f"Enter New Value for {metric_to_edit}", value=float(df[df['Account ID'] == account_to_edit][metric_to_edit].iloc[index_to_edit]))
    
    if st.button("Update Credit Info"):
        df.loc[(df['Account ID'] == account_to_edit) & (df.index == df[df['Account ID'] == account_to_edit].index[index_to_edit]), metric_to_edit] = new_value
        st.success(f"{metric_to_edit} updated for {account_to_edit} on {df['Date'].iloc[index_to_edit]}")

# Export Data Option
st.sidebar.markdown(export_data(df_filtered), unsafe_allow_html=True)
