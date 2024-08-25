import streamlit as st

# Set page configuration with a custom page title and icon
st.set_page_config(
    page_title="Multipage App",
    page_icon="💳",
)

# Sidebar with logo and navigation prompt
st.sidebar.image("/logooo.png", use_column_width=True)
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

- 📊 **Credit Score Overview**  
  Get a quick snapshot of your current credit score, along with historical trends and key factors influencing your score.

- 💳 **Credit Utilization**  
  Monitor how much of your available credit you're using. Lower utilization rates can improve your credit score.

- 🗓️ **Payment History**  
  Review your on-time payments and any late payments that could affect your credit score.

- 📑 **Credit Report Summary**  
  Access a concise summary of your credit report, highlighting crucial information about your credit history.

- 🔍 **Credit Inquiries**  
  Keep track of any hard and soft inquiries made on your credit report, helping you understand who has been checking your credit.

- 🎯 **Credit Limits**  
  View your credit limits across all accounts and analyze how much of your credit is being utilized.

- ⚖️ **Debt-to-Income Ratio**  
  Calculate and monitor your debt-to-income ratio, a key factor in creditworthiness.

- 💰 **Loan and Credit Card Balances**  
  Stay updated on your outstanding loan and credit card balances, so you know exactly what you owe.

- ⏳ **Account Age**  
  Understand the impact of the age of your credit accounts on your overall credit score.

- 💵 **Monthly Payments**  
  View and manage your upcoming monthly payments to ensure you never miss a due date.

- 📂 **Credit Accounts Breakdown**  
  A detailed breakdown of all your credit accounts, including credit cards, loans, and other types of credit.

- 🏆 **Top 5 Highest Balances**  
  Identify which of your accounts have the highest balances, helping you prioritize debt repayment.

- 📝 **Top 5 Recent Transactions**  
  Keep an eye on your most recent transactions to spot any unusual or unauthorized activity.

- 📅 **Upcoming Payments**  
  Never miss a payment again with a clear view of all your upcoming payments.

- 🔄 **Credit Utilization by Account Type**  
  Analyze your credit utilization by account type to see where you might need to make adjustments.

- 📈 **Average Payment History**  
  Get an average overview of your payment history, showing how consistent you've been with payments over time.

- 📊 **Credit Score Trend**  
  Track the trend of your credit score over time to see how your financial decisions impact your score.

- 💸 **Monthly Spending Trend**  
  Visualize your spending habits over the months to identify patterns and areas where you can save.

- 📉 **Credit Score vs. Credit Utilization**  
  See the relationship between your credit score and your credit utilization to better manage both.

- 📅 **Debt Repayment Schedule**  
  Plan out your debt repayment strategy with a detailed schedule to help you become debt-free faster.

- 🆕 **New Credit Accounts**  
  Monitor the opening of any new credit accounts and understand how they might affect your credit score.

- 🧠 **Credit Score Impact Simulation**  
  Simulate different scenarios to see how potential actions could impact your credit score.

- 📉 **Debt Reduction Plan**  
  Get personalized tips on how to reduce your debt effectively and improve your credit score.

- 💡 **Credit Score Improvement Tips**  
  Receive actionable advice on how to improve your credit score based on your current credit profile.

- ⚠️ **Alerts and Recommendations**  
  Set up alerts for important events that might impact your credit and receive personalized recommendations.

- ✏️ **Edit Credit Info**  
  Easily update and correct any information in your credit profile to ensure it’s accurate and up-to-date.

- 📤 **Export Data**  
  Export your credit information in various formats for easy sharing or record-keeping.
""")

# Conclusion
st.write("""
Explore these features and more in the VIP Credit Systems app. Whether you are looking to improve your credit score, manage your debts, or simply stay on top of your financial health, we’ve got you covered. Start making informed financial decisions today!
""")
