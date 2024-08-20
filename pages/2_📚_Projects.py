import streamlit as st
import pandas as pd
import os

# Initialize Streamlit app
st.set_page_config(page_title="Business Blueprint 101")

# Title and Subheader
st.title("***Business Blueprint 101 - From Start Up to Funding***")
st.subheader("Organize, Prioritize, and Manage Your Business Setup Effectively!")

# Local Database
@st.cache_data
def get_local_data():
    return pd.DataFrame(columns=["Title", "Steps"])

data = get_local_data()

# Functions for interacting with local data
def save_local_data():
    data.to_csv("local_data.csv", index=False)

def load_local_data():
    if "local_data.csv" in os.listdir():
        return pd.read_csv("local_data.csv")
    else:
        return pd.DataFrame(columns=["Title", "Steps"])

def add_title_steps(title, steps):
    global data
    new_entry = {"Title": title, "Steps": steps}
    data = data.append(new_entry, ignore_index=True)
    save_local_data()

def edit_title_steps(entry_id, updated_title, updated_steps):
    global data
    data.at[entry_id, "Title"] = updated_title
    data.at[entry_id, "Steps"] = updated_steps
    save_local_data()

def delete_entry(entry_id):
    global data
    data = data.drop(index=entry_id).reset_index(drop=True)
    save_local_data()

# Load data from CSV
data = load_local_data()

# Example Business Blueprint Titles and Steps
example_entries = [
    {
        "Title": "Research Business Name",
        "Steps": [
            "Brainstorm potential business names.",
            "Check the availability of domain names.",
            "Search for existing businesses with the same name.",
            "Ensure the name is easy to spell and remember.",
            "Confirm the name aligns with your brand vision."
        ]
    },
    # ... (other entries are similar, so they're omitted for brevity)
]

# Display Titles with Steps
for entry_id, entry_data in enumerate(example_entries):
    entry_key = f"title-{entry_id}"
    with st.expander(entry_data["Title"], expanded=False):
        st.write("### Steps:")
        for step in entry_data["Steps"]:
            st.write(f"- {step}")
        
        # Edit button and functionality
        if st.button("Edit", key=f"edit-{entry_id}"):
            updated_title = st.text_input("Title", value=entry_data["Title"])
            updated_steps = st.text_area("Steps (one per line)", value="\n".join(entry_data["Steps"]))
            if st.button("Save Changes", key=f"save-{entry_id}"):
                edit_title_steps(entry_id, updated_title, updated_steps.split("\n"))
                st.experimental_rerun()
        
        # Delete button and functionality
        if st.button("Delete", key=f"delete-{entry_id}"):
            delete_entry(entry_id)
            st.experimental_rerun()

# Functionality to add a new title with steps
with st.expander("Add New Title and Steps", expanded=False):
    title = st.text_input("New Title")
    steps = st.text_area("Steps (one per line)")
    if st.button("Add Title and Steps"):
        add_title_steps(title, steps.split("\n"))
        st.experimental_rerun()

st.write("### Business Blueprint 101 - Organized and ready to go!")
