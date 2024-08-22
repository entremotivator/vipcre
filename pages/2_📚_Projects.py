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

def save_local_data(data):
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
        "Completed": [list(False for _ in steps)]
    })
    data = pd.concat([data, new_entry], ignore_index=True)
    save_local_data(data)

def edit_title_steps(entry_id, updated_title, updated_steps):
    global data
    data.at[entry_id, "Title"] = updated_title
    data.at[entry_id, "Steps"] = updated_steps
    data.at[entry_id, "Completed"] = [False] * len(updated_steps)
    save_local_data(data)

def delete_entry(entry_id):
    global data
    data = data.drop(index=entry_id).reset_index(drop=True)
    save_local_data(data)

def update_step_completion(entry_id, step_index, status):
    global data
    completed = eval(data.at[entry_id, "Completed"])  # Convert string to list
    completed[step_index] = status
    data.at[entry_id, "Completed"] = str(completed)  # Convert list to string
    save_local_data(data)

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
            "Check for any missed payments or accounts.",
            "Review recent credit inquiries.",
            "Evaluate your credit utilization.",
            "Understand your credit report’s impact on your score.",
            "Download and store your credit reports securely."
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
            "Track your payment history to confirm timely payments.",
            "Review bills for accuracy.",
            "Avoid late fees by scheduling payments in advance.",
            "Maintain a record of all payment confirmations.",
            "Evaluate and adjust payment strategies periodically."
        ]
    },
    # Add other example entries similarly
]

# Add example entries to data if not already present
for entry in example_entries:
    if not any(data['Title'] == entry['Title']):
        add_title_steps(entry['Title'], entry['Steps'])

# Display Titles with Steps
for entry_id, entry_data in data.iterrows():
    with st.expander(entry_data['Title'], expanded=True):
        st.markdown(f"### Steps:")
        steps = eval(entry_data['Steps'])  # Convert string representation of list back to list
        completed = eval(entry_data['Completed'])  # Convert string representation of list back to list
        for step_index, (step, is_checked) in enumerate(zip(steps, completed)):
            is_checked = st.checkbox(step, value=is_checked, key=f"{entry_id}-{step_index}")
            if is_checked != completed[step_index]:
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
