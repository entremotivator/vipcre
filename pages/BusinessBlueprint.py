import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime
import json

# Initialize Streamlit app
st.set_page_config(page_title="Business Blueprint 101", layout="wide")

# Function to load data
def load_data():
    if os.path.exists("business_blueprint_data.json"):
        with open("business_blueprint_data.json", "r") as f:
            return json.load(f)
    return {"ID": [], "Title": [], "Steps": [], "Completed": [], "Priority": [], "Created": [], "LastUpdated": []}

# Function to save data
def save_data(data):
    with open("business_blueprint_data.json", "w") as f:
        json.dump(data, f)

# Function to add new title and steps
def add_title_steps(data, title, steps):
    data["ID"].append(str(uuid.uuid4()))
    data["Title"].append(title)
    data["Steps"].append(steps)
    data["Completed"].append([False] * len(steps))
    data["Priority"].append("Medium")
    data["Created"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    data["LastUpdated"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    save_data(data)
    return data

# Function to update completion status
def update_completion(data, id, step_index, status):
    entry_index = data["ID"].index(id)
    data["Completed"][entry_index][step_index] = status
    data["LastUpdated"][entry_index] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(data)
    return data

# Function to update priority
def update_priority(data, id, new_priority):
    entry_index = data["ID"].index(id)
    data["Priority"][entry_index] = new_priority
    data["LastUpdated"][entry_index] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(data)
    return data

# Function to edit title and steps
def edit_title_steps(data, id, updated_title, updated_steps):
    entry_index = data["ID"].index(id)
    data["Title"][entry_index] = updated_title
    data["Steps"][entry_index] = updated_steps
    data["Completed"][entry_index] = [False] * len(updated_steps)
    data["LastUpdated"][entry_index] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(data)
    return data

# Function to delete entry
def delete_entry(data, id):
    entry_index = data["ID"].index(id)
    for key in data.keys():
        data[key].pop(entry_index)
    save_data(data)
    return data

# Load data
data = load_data()

# Title and Subheader
st.title("Business Blueprint 101")
st.subheader("From Start Up to Funding")

# Display current date
st.markdown(f"**Completed on {datetime.now().strftime('%B %d, %Y')}**")

# Main content
for index, entry_data in enumerate(zip(data["ID"], data["Title"], data["Steps"], data["Completed"], data["Priority"], data["Created"], data["LastUpdated"])):
    id, title, steps, completed, priority, created, last_updated = entry_data
    
    with st.expander(f"{title} (Priority: {priority})", expanded=False):
        st.write(f"Created: {created}")
        st.write(f"Last Updated: {last_updated}")
        
        for step_index, (step, is_completed) in enumerate(zip(steps, completed)):
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.checkbox(step, value=is_completed, key=f"{id}-{step_index}", 
                            on_change=lambda: update_completion(data, id, step_index, not is_completed))
            with col2:
                st.markdown(f"{'✅' if is_completed else '❌'}")
        
        # Priority dropdown
        new_priority = st.selectbox("Priority", options=["Low", "Medium", "High"], 
                                    index=["Low", "Medium", "High"].index(priority), key=f"priority-{id}")
        if st.button("Update Priority", key=f"update_priority-{id}"):
            data = update_priority(data, id, new_priority)
            st.experimental_rerun()
        
        # Edit functionality
        if st.button("Edit", key=f"edit-{id}"):
            updated_title = st.text_input("Title", value=title)
            updated_steps = st.text_area("Steps (one per line)", value="\n".join(steps), height=300)
            if st.button("Save Changes", key=f"save-{id}"):
                data = edit_title_steps(data, id, updated_title, updated_steps.split("\n"))
                st.experimental_rerun()
        
        # Delete functionality
        if st.button("Delete", key=f"delete-{id}"):
            data = delete_entry(data, id)
            st.experimental_rerun()

# Add new title and steps
with st.expander("Add New Title and Steps", expanded=False):
    new_title = st.text_input("New Title")
    new_steps = st.text_area("Steps (one per line)", height=300)
    if st.button("Add Title and Steps"):
        data = add_title_steps(data, new_title, new_steps.split("\n"))
        st.experimental_rerun()

# Summary of tasks
completed_tasks = sum([sum(completed) for completed in data["Completed"]])
total_tasks = sum([len(steps) for steps in data["Steps"]])

st.markdown("## Summary")
st.markdown(f"**Total tasks:** {total_tasks}")
st.markdown(f"**Completed tasks:** {completed_tasks}")
st.markdown(f"**Pending tasks:** {total_tasks - completed_tasks}")

# Progress bar
st.progress(completed_tasks / total_tasks if total_tasks > 0 else 0)

st.write("### Business Blueprint 101 - Organized and ready to go!")
