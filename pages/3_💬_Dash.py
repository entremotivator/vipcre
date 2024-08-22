import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# Connect to SQLite Database (persistent storage)
conn = sqlite3.connect('credit_data.db')
c = conn.cursor()

# Create a table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS credit_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id TEXT,
                date TEXT,
                credit_score INTEGER,
                credit_utilization REAL,
                total_debt INTEGER,
                monthly_payments INTEGER,
                income INTEGER,
                new_credit_accounts INTEGER,
                payment_history TEXT,
                credit_limits INTEGER
            )''')
conn.commit()

# Generate and insert sample data
def generate_sample_data(account_id):
    dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
    data = []
    
    for date in dates:
        entry = (account_id, date.strftime('%Y-%m-%d'),
                 np.random.randint(650, 850),
                 np.random.uniform(0.2, 0.9),
                 np.random.randint(1000, 5000),
                 np.random.randint(100, 1000),
                 np.random.randint(3000, 7000),
                 np.random.randint(0, 3),
                 np.random.choice(["On Time", "Late"], p=[0.9, 0.1]),
                 np.random.randint(5000, 20000))
        data.append(entry)
    
    c.executemany('''INSERT INTO credit_info (
                        account_id, date, credit_score, credit_utilization, total_debt,
                        monthly_payments, income, new_credit_accounts, payment_history, credit_limits
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
    conn.commit()

# Load data from the database
def load_data(account_id):
    query = f"SELECT * FROM credit_info WHERE account_id = '{account_id}'"
    df = pd.read_sql(query, conn)
    df['Date'] = pd.to_datetime(df['date'])
    df['Debt-to-Income Ratio'] = df['total_debt'] / df['income']
    return df

# Initialize and combine data for multiple accounts
account_ids = [f"Account {i}" for i in range(1, 4)]
for account_id in account_ids:
    if not c.execute(f"SELECT 1 FROM credit_info WHERE account_id = '{account_id}'").fetchone():
        generate_sample_data(account_id)

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
    "Summary Report",
    "Edit Credit Info"
])

# Load filtered data for the selected account
df_filtered = load_data(selected_account)

# Export data to CSV
def export_data(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{selected_account}_credit_data.csv">Download {selected_account} Credit Data</a>'
    return href

# Generate plots for trend analysis
def plot_trend(df, column_name, title, y_axis_label):
    fig = px.line(df, x="Date", y=column_name, title=title)
    fig.update_layout(yaxis_title=y_axis_label, xaxis_title="Date")
    st.plotly_chart(fig)

# Display summary report
def display_summary_report(df):
    st.subheader("Summary Report")
    summary_stats = df.describe().T
    st.dataframe(summary_stats)

    st.subheader("Correlation Matrix")
    corr_matrix = df.corr()
    fig, ax = plt.subplots()
    cax = ax.matshow(corr_matrix, cmap='coolwarm')
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    fig.colorbar(cax)
    st.pyplot(fig)

# Display selected page
if page == "Credit Score Overview":
    st.subheader("Credit Score Overview")
    st.write(f"Current Credit Score for {selected_account}: {df_filtered['credit_score'].iloc[-1]}")
    plot_trend(df_filtered, 'credit_score', 'Credit Score Over Time', 'Credit Score')

    st.subheader("Credit Score Trend Analysis")
    trend = "increasing" if df_filtered['credit_score'].pct_change().mean() > 0 else "decreasing"
    st.write(f"Overall trend: {trend}")

    st.subheader("Edit Credit Score")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='score_index')
    new_score = st.number_input("Enter New Credit Score", min_value=300, max_value=850, value=int(df_filtered['credit_score'].iloc[index_to_edit]), key='new_score')
    if st.button("Update Credit Score"):
        c.execute('''UPDATE credit_info SET credit_score = ? WHERE id = ?''',
                  (new_score, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"Credit Score updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Credit Utilization":
    st.subheader("Credit Utilization")
    plot_trend(df_filtered, 'credit_utilization', 'Credit Utilization Over Time', 'Credit Utilization')

    avg_utilization = df_filtered['credit_utilization'].mean()
    st.write(f"Average Credit Utilization: {avg_utilization:.2%}")
    st.write("A utilization rate below 30% is generally recommended.")

    st.subheader("Edit Credit Utilization")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='util_index')
    new_utilization = st.slider("Enter New Credit Utilization", min_value=0.0, max_value=1.0, value=float(df_filtered['credit_utilization'].iloc[index_to_edit]), key='new_utilization')
    if st.button("Update Credit Utilization"):
        c.execute('''UPDATE credit_info SET credit_utilization = ? WHERE id = ?''',
                  (new_utilization, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"Credit Utilization updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Payment History":
    st.subheader("Payment History")
    st.write(df_filtered[['Date', 'payment_history']].set_index('Date'))

    late_payments = df_filtered[df_filtered['payment_history'] == "Late"].shape[0]
    st.write(f"Number of Late Payments: {late_payments}")

    st.subheader("Edit Payment History")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='history_index')
    new_history = st.selectbox("Select Payment History", ["On Time", "Late"], index=0 if df_filtered['payment_history'].iloc[index_to_edit] == "On Time" else 1, key='new_history')
    if st.button("Update Payment History"):
        c.execute('''UPDATE credit_info SET payment_history = ? WHERE id = ?''',
                  (new_history, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"Payment History updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Debt-to-Income Ratio":
    st.subheader("Debt-to-Income Ratio")
    plot_trend(df_filtered, 'Debt-to-Income Ratio', 'Debt-to-Income Ratio Over Time', 'Debt-to-Income Ratio')

    st.write("A lower debt-to-income ratio indicates better financial health.")
    high_ratio = df_filtered['Debt-to-Income Ratio'].max()
    st.write(f"Highest Recorded Ratio: {high_ratio:.2%}")

    st.subheader("Edit Debt and Income")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='debt_index')
    new_debt = st.number_input("Enter New Total Debt", min_value=0, max_value=100000, value=int(df_filtered['total_debt'].iloc[index_to_edit]), key='new_debt')
    new_income = st.number_input("Enter New Income", min_value=0, max_value=100000, value=int(df_filtered['income'].iloc[index_to_edit]), key='new_income')
    if st.button("Update Debt and Income"):
        c.execute('''UPDATE credit_info SET total_debt = ?, income = ? WHERE id = ?''',
                  (new_debt, new_income, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"Debt and Income updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Monthly Payments":
    st.subheader("Monthly Payments")
    plot_trend(df_filtered, 'monthly_payments', 'Monthly Payments Over Time', 'Monthly Payments')

    avg_payments = df_filtered['monthly_payments'].mean()
    st.write(f"Average Monthly Payments: ${avg_payments:.2f}")

    st.subheader("Edit Monthly Payments")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='payment_index')
    new_payment = st.number_input("Enter New Monthly Payment", min_value=0, max_value=10000, value=int(df_filtered['monthly_payments'].iloc[index_to_edit]), key='new_payment')
    if st.button("Update Monthly Payment"):
        c.execute('''UPDATE credit_info SET monthly_payments = ? WHERE id = ?''',
                  (new_payment, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"Monthly Payment updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "New Credit Accounts":
    st.subheader("New Credit Accounts")
    plot_trend(df_filtered, 'new_credit_accounts', 'New Credit Accounts Over Time', 'New Credit Accounts')

    total_new_accounts = df_filtered['new_credit_accounts'].sum()
    st.write(f"Total New Credit Accounts: {total_new_accounts}")

    st.subheader("Edit New Credit Accounts")
    index_to_edit = st.number_input("Select Index (0-11)", min_value=0, max_value=11, value=0, key='accounts_index')
    new_accounts = st.number_input("Enter New Number of Accounts", min_value=0, max_value=10, value=int(df_filtered['new_credit_accounts'].iloc[index_to_edit]), key='new_accounts')
    if st.button("Update New Credit Accounts"):
        c.execute('''UPDATE credit_info SET new_credit_accounts = ? WHERE id = ?''',
                  (new_accounts, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"New Credit Accounts updated for {df_filtered['Date'].iloc[index_to_edit]}")

elif page == "Summary Report":
    display_summary_report(df_filtered)

elif page == "Edit Credit Info":
    st.subheader("Edit Credit Info")
    metric_to_edit = st.selectbox("Select Metric", df_filtered.columns[3:])
    index_to_edit = st.number_input(f"Select Index (0-{len(df_filtered) - 1})", min_value=0, max_value=len(df_filtered) - 1, value=0, key='edit_info_index')
    new_value = st.number_input(f"Enter New Value for {metric_to_edit}", value=float(df_filtered[metric_to_edit].iloc[index_to_edit]))
    
    if st.button("Update Credit Info"):
        c.execute(f'''UPDATE credit_info SET {metric_to_edit} = ? WHERE id = ?''',
                  (new_value, df_filtered['id'].iloc[index_to_edit]))
        conn.commit()
        st.success(f"{metric_to_edit} updated for {selected_account} on {df_filtered['Date'].iloc[index_to_edit]}")

# Display export option in sidebar
st.sidebar.markdown(export_data(df_filtered), unsafe_allow_html=True)
