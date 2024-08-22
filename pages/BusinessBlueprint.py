import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime
import json

# Initialize Streamlit app
st.set_page_config(page_title="Business Blueprint 101", layout="wide")

# Title and Subheader
st.markdown("<h1 style='font-size:36px;'>Business Blueprint 101 - From Start Up to Funding</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size:24px;'>Organize, Prioritize, and Manage Your Business Setup Effectively!</h3>", unsafe_allow_html=True)

# Local Database
def get_local_data():
    if "local_data.csv" in os.listdir():
        # Read the CSV file
        df = pd.read_csv("local_data.csv")
        # Convert string representations of lists back to lists
        df["Steps"] = df["Steps"].apply(lambda x: json.loads(x))
        df["Completed"] = df["Completed"].apply(lambda x: json.loads(x))
        df["CompletionDates"] = df["CompletionDates"].apply(lambda x: json.loads(x))
        df["Priorities"] = df["Priorities"].apply(lambda x: json.loads(x))
        return df
    else:
        return pd.DataFrame(columns=["ID", "Title", "Steps", "Completed", "CompletionDates", "Priorities"])

def save_local_data(data):
    # Convert lists to JSON strings for storage
    data["Steps"] = data["Steps"].apply(lambda x: json.dumps(x))
    data["Completed"] = data["Completed"].apply(lambda x: json.dumps(x))
    data["CompletionDates"] = data["CompletionDates"].apply(lambda x: json.dumps(x))
    data["Priorities"] = data["Priorities"].apply(lambda x: json.dumps(x))
    data.to_csv("local_data.csv", index=False)

def add_title_steps(data, title, steps):
    new_entry = pd.DataFrame({
        "ID": [str(uuid.uuid4())], 
        "Title": [title], 
        "Steps": [steps], 
        "Completed": [[False]*len(steps)],
        "CompletionDates": ['' for _ in steps],
        "Priorities": ['Low' for _ in steps]  # Default priority
    })
    data = pd.concat([data, new_entry], ignore_index=True)
    save_local_data(data)
    return data

def edit_title_steps(data, entry_id, updated_title, updated_steps):
    index = data[data["ID"] == entry_id].index[0]
    data.at[index, "Title"] = updated_title
    data.at[index, "Steps"] = updated_steps
    data.at[index, "Completed"] = [False]*len(updated_steps)  # Reset completion status
    data.at[index, "CompletionDates"] = ['']*len(updated_steps)  # Reset completion dates
    data.at[index, "Priorities"] = ['Low']*len(updated_steps)  # Reset priorities
    save_local_data(data)
    return data

def delete_entry(data, entry_id):
    data = data[data["ID"] != entry_id].reset_index(drop=True)
    save_local_data(data)
    return data

def toggle_step_completion(data, entry_id, step_index):
    index = data[data["ID"] == entry_id].index[0]
    if not data.at[index, "Completed"][step_index]:  # If the task is not completed
        data.at[index, "Completed"][step_index] = True
        data.at[index, "CompletionDates"][step_index] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:  # If the task is already completed
        data.at[index, "Completed"][step_index] = False
        data.at[index, "CompletionDates"][step_index] = ''
    save_local_data(data)
    return data

def update_priority(data, entry_id, step_index, new_priority):
    index = data[data["ID"] == entry_id].index[0]
    data.at[index, "Priorities"][step_index] = new_priority
    save_local_data(data)
    return data

# Load data from CSV
data = get_local_data()

# Additional demo data
additional_entries = [
    {
        "Title": "Develop Marketing Strategy",
        "Steps": [
            "Identify target audience.",
            "Analyze market trends and competitors.",
            "Create a unique value proposition.",
            "Design marketing materials.",
            "Set up online and offline marketing channels.",
            "Develop a social media strategy.",
            "Create a content marketing plan.",
            "Allocate marketing budget.",
            "Measure marketing effectiveness.",
            "Adjust strategy based on performance."
        ]
    },
    {
        "Title": "Build Online Presence",
        "Steps": [
            "Design and launch a business website.",
            "Set up social media profiles.",
            "Create a content calendar.",
            "Engage with potential customers online.",
            "Optimize your website for search engines.",
            "Develop a blog or news section.",
            "Implement an email marketing strategy.",
            "Run online advertising campaigns.",
            "Monitor website traffic and engagement.",
            "Update content regularly."
        ]
    },
    # Add more entries as needed...
]

# Add additional demo entries
for entry in additional_entries:
    data = add_title_steps(data, entry["Title"], entry["Steps"])

# Display Titles with Steps
for entry_id, entry_data in data.iterrows():
    entry_key = f"title-{entry_data['ID']}"
    with st.expander(entry_data["Title"], expanded=False):
        st.markdown("<h4 style='font-size:20px;'>Steps:</h4>", unsafe_allow_html=True)
        steps = entry_data["Steps"]
        completed = entry_data["Completed"]
        completion_dates = entry_data["CompletionDates"]
        priorities = entry_data["Priorities"]
        
        for step_index, (step, completed_status, date, priority) in enumerate(zip(steps, completed, completion_dates, priorities)):
            checkbox_label = f"{step}"
            if st.checkbox(checkbox_label, value=completed_status, key=f"checkbox-{entry_data['ID']}-{step_index}"):
                data = toggle_step_completion(data, entry_data["ID"], step_index)
            if completed_status:
                st.markdown(f"<p style='color:green;'>Completed on {date}</p>", unsafe_allow_html=True)
            
            # Priority dropdown
            new_priority = st.selectbox(
                "Priority",
                options=["Low", "Medium", "High"],
                index=["Low", "Medium", "High"].index(priority),
                key=f"priority-{entry_data['ID']}-{step_index}"
            )
            if st.button("Update Priority", key=f"update_priority-{entry_data['ID']}-{step_index}"):
                data = update_priority(data, entry_data["ID"], step_index, new_priority)
                st.experimental_rerun()
        
        # Edit button and functionality
        edit_key = f"edit-{entry_data['ID']}"
        if st.button("Edit", key=edit_key):
            updated_title = st.text_input("Title", value=entry_data["Title"])
            updated_steps = st.text_area("Steps (one per line)", value="\n".join(steps), height=300)
            save_key = f"save-{entry_data['ID']}"
            if st.button("Save Changes", key=save_key):
                data = edit_title_steps(data, entry_data["ID"], updated_title, updated_steps.split("\n"))
                st.experimental_rerun()
        
        # Delete button and functionality
        delete_key = f"delete-{entry_data['ID']}"
        if st.button("Delete", key=delete_key):
            data = delete_entry(data, entry_data["ID"])
            st.experimental_rerun()

# Functionality to add a new title with steps
with st.expander("Add New Title and Steps", expanded=False):
    new_title = st.text_input("New Title")
    new_steps = st.text_area("Steps (one per line)", height=300)
    if st.button("Add Title and Steps"):
        data = add_title_steps(data, new_title, new_steps.split("\n"))
        st.experimental_rerun()

# Summary of tasks
completed_tasks = sum([sum(completed) for completed in data["Completed"]])
total_tasks = sum([len(steps) for steps in data["Steps"]])
st.markdown("<h3 style='font-size:20px;'>Task Summary</h3>", unsafe_allow_html=True)
st.markdown(f"<p>Total tasks: {total_tasks}</p>", unsafe_allow_html=True)
st.markdown(f"<p>Completed tasks: {completed_tasks}</p>", unsafe_allow_html=True)
st.markdown(f"<p>Pending tasks: {total_tasks - completed_tasks}</p>", unsafe_allow_html=True)

st.write("### Business Blueprint 101 - Organized and ready to go!")


