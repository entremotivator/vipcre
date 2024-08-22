import streamlit as st
import pandas as pd
import os

# Initialize Streamlit app
st.set_page_config(page_title="Credit Building Blueprint")

# Title and Subheader
st.title("**Credit Building Blueprint - 10 Key Projects**")
st.subheader("Organize, Manage, and Track Your Credit Building Projects Effectively!")

# Local Database
@st.cache_data
def get_local_data():
    return pd.DataFrame(columns=["Title", "Steps", "Completed"])

data = get_local_data()

# Functions for interacting with local data
def save_local_data():
    data.to_csv("credit_projects.csv", index=False)

def load_local_data():
    if "credit_projects.csv" in os.listdir():
        return pd.read_csv("credit_projects.csv")
    else:
        return pd.DataFrame(columns=["Title", "Steps", "Completed"])

def add_title_steps(title, steps):
    global data
    new_entry = pd.DataFrame({
        "Title": [title],
        "Steps": [steps],
        "Completed": [[False]*len(steps)]
    })
    global data
    data = pd.concat([data, new_entry], ignore_index=True)
    save_local_data()

def edit_title_steps(entry_id, updated_title, updated_steps):
    global data
    data.at[entry_id, "Title"] = updated_title
    data.at[entry_id, "Steps"] = updated_steps
    data.at[entry_id, "Completed"] = [False]*len(updated_steps)
    save_local_data()

def delete_entry(entry_id):
    global data
    data = data.drop(index=entry_id).reset_index(drop=True)
    save_local_data()

def update_step_completion(entry_id, step_index, status):
    global data
    completed = data.at[entry_id, "Completed"]
    completed[step_index] = status
    data.at[entry_id, "Completed"] = completed
    save_local_data()

# Load data from CSV
data = load_local_data()

# Example Credit Building Projects and Steps
example_entries = [
    {
        "Title": "Review Credit Report",
        "Steps": [
            "Obtain a copy of your credit report from all three bureaus.",
            "Check for errors or inaccuracies.",
            "Dispute any inaccuracies with the credit bureaus.",
            "Review your credit history for trends.",
            "Understand your current credit score.",
            "Identify areas for improvement.",
            "Analyze any negative items impacting your score.",
            "Request updates or corrections to your credit history.",
            "Track changes to your credit report over time.",
            "Set goals for improving your credit score."
        ]
    },
    {
        "Title": "Pay Bills on Time",
        "Steps": [
            "Create a budget to manage expenses.",
            "Set up automatic payments or reminders.",
            "Prioritize paying bills before due dates.",
            "Monitor accounts regularly for missed payments.",
            "Adjust your budget as needed to ensure timely payments.",
            "Review and categorize bills monthly.",
            "Track payment history for accuracy.",
            "Resolve any issues with missed payments promptly.",
            "Consider using a financial app to track bill payments.",
            "Evaluate and adjust payment strategies regularly."
        ]
    },
    {
        "Title": "Reduce Credit Card Balances",
        "Steps": [
            "List all credit card debts and their interest rates.",
            "Create a debt repayment plan.",
            "Focus on paying down high-interest cards first.",
            "Consider balance transfers to lower interest rates.",
            "Avoid adding new charges to paid-off cards.",
            "Monitor credit card statements for errors.",
            "Negotiate lower interest rates with creditors.",
            "Set up automatic payments to avoid late fees.",
            "Review progress and adjust repayment plan as needed.",
            "Seek advice from a financial advisor if necessary."
        ]
    },
    {
        "Title": "Increase Credit Limit",
        "Steps": [
            "Contact your credit card issuer to request a limit increase.",
            "Provide financial information if requested.",
            "Maintain a good payment history before requesting.",
            "Use the increased limit responsibly.",
            "Monitor your credit utilization ratio.",
            "Review your credit report for improvements.",
            "Avoid overusing the increased limit.",
            "Track changes in your credit score.",
            "Consider requesting increases periodically.",
            "Maintain a good credit profile overall."
        ]
    },
    {
        "Title": "Open a Secured Credit Card",
        "Steps": [
            "Research secured credit cards with favorable terms.",
            "Apply for a secured card and deposit the required amount.",
            "Use the card for small purchases and pay off balances in full.",
            "Track your credit score for improvements.",
            "Consider transitioning to an unsecured card over time.",
            "Monitor your credit utilization on the secured card.",
            "Review the terms and conditions regularly.",
            "Ensure timely payments to build credit history.",
            "Seek options for higher credit limits as needed.",
            "Evaluate card performance and benefits periodically."
        ]
    },
    {
        "Title": "Establish Credit History",
        "Steps": [
            "Apply for credit with a retailer or bank.",
            "Use the credit responsibly and make timely payments.",
            "Consider becoming an authorized user on someone else's account.",
            "Avoid applying for too much credit at once.",
            "Monitor your credit report regularly.",
            "Keep old accounts open to lengthen credit history.",
            "Manage a mix of credit types (revolving and installment).",
            "Review credit history for accuracy.",
            "Address any negative items promptly.",
            "Seek professional advice if needed."
        ]
    },
    {
        "Title": "Monitor Credit Regularly",
        "Steps": [
            "Sign up for a credit monitoring service.",
            "Set up alerts for any changes in your credit report.",
            "Review credit reports at least once a year.",
            "Address any issues or changes promptly.",
            "Track your credit score trends over time.",
            "Update your monitoring service settings as needed.",
            "Review accounts for fraudulent activity.",
            "Analyze credit score changes and their causes.",
            "Adjust credit strategies based on monitoring insights.",
            "Seek help if you notice suspicious activities."
        ]
    },
    {
        "Title": "Negotiate with Creditors",
        "Steps": [
            "Identify accounts with high interest rates or fees.",
            "Contact creditors to negotiate better terms.",
            "Request lower interest rates or fee waivers.",
            "Document all agreements and changes.",
            "Follow up to ensure agreements are honored.",
            "Review creditor responses and adjust negotiations as needed.",
            "Evaluate potential benefits of refinancing options.",
            "Seek assistance from credit counseling services if necessary.",
            "Maintain communication with creditors for updates.",
            "Monitor the impact of negotiations on your credit report."
        ]
    },
    {
        "Title": "Build a Positive Credit Mix",
        "Steps": [
            "Maintain a mix of credit accounts (revolving and installment).",
            "Avoid closing old accounts, as they contribute to credit history length.",
            "Manage each type of credit responsibly.",
            "Monitor the impact of your credit mix on your score.",
            "Adjust your credit strategy as needed.",
            "Consider diversifying your credit types if appropriate.",
            "Review account management strategies regularly.",
            "Evaluate credit mix impact on overall credit profile.",
            "Seek advice on optimal credit mix based on financial goals.",
            "Address any negative impacts of credit mix changes promptly."
        ]
    },
    {
        "Title": "Avoid New Hard Inquiries",
        "Steps": [
            "Limit the number of credit applications.",
            "Apply for credit only when necessary.",
            "Research credit options before applying.",
            "Monitor your credit report for hard inquiries.",
            "Understand the impact of hard inquiries on your score.",
            "Plan credit applications strategically to minimize impact.",
            "Use pre-qualification tools to avoid hard inquiries.",
            "Review the reasons for credit denials to improve applications.",
            "Maintain a stable credit profile to reduce unnecessary inquiries.",
            "Seek alternatives to traditional credit applications if needed."
        ]
    },
    {
        "Title": "Create a Credit Improvement Plan",
        "Steps": [
            "Set clear credit goals and objectives.",
            "Develop a step-by-step action plan.",
            "Track progress and adjust strategies as needed.",
            "Seek professional advice if necessary.",
            "Review and revise the plan regularly.",
            "Monitor the effectiveness of implemented strategies.",
            "Evaluate the impact of changes on your credit score.",
            "Incorporate feedback and lessons learned into the plan.",
            "Adjust the plan based on financial changes or goals.",
            "Celebrate milestones and achievements in credit improvement."
        ]
    }
]

# Add example entries to data if not already present
for entry in example_entries:
    if not any(data['Title'] == entry['Title']):
        add_title_steps(entry['Title'], entry['Steps'])

# Display Titles with Steps
for entry_id, entry_data in data.iterrows():
    with st.expander(f"<h1 style='font-size: 32px;'>{entry_data['Title']}</h1>", expanded=True, unsafe_allow_html=True):
        st.write("### Steps:")
        steps = eval(entry_data['Steps'])  # Convert string representation of list back to list
        completed = eval(entry_data['Completed'])  # Convert string representation of list back to list
        for step_index, (step, completed) in enumerate(zip(steps, completed)):
            is_checked = st.checkbox(step, value=completed, key=f"{entry_id}-{step_index}")
            if is_checked != completed:
                update_step_completion(entry_id, step_index, is_checked)

        # Edit functionality
        with st.expander("Edit This Project", expanded=False):
            updated_title = st.text_input("Update Title", value=entry_data['Title'])
            updated_steps = st.text_area("Update Steps (one per line)", value="\n".join(steps))
            if st.button("Save Changes", key=f"save-{entry_id}"):
                edit_title_steps(entry_id, updated_title, updated_steps.split("\n"))
                st.experimental_rerun()

        # Delete button and functionality
        if st.button(f"Delete {entry_id}", key=f"delete-{entry_id}"):
            delete_entry(entry_id)
            st.experimental_rerun()

# Functionality to add a new title with steps
with st.expander("Add New Title and Steps", expanded=True):
    title = st.text_input("New Title")
    steps = st.text_area("Steps (one per line)")
    if st.button("Add Title and Steps"):
        add_title_steps(title, steps.split("\n"))
        st.experimental_rerun()

st.write("### Credit Building Blueprint - Organized and Ready to Go!")


