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
    if "local_data.csv" in os.listdir():
        return pd.read_csv("local_data.csv")
    else:
        return pd.DataFrame(columns=["Title", "Steps", "Completed"])

def save_local_data(data):
    data.to_csv("local_data.csv", index=False)

def add_title_steps(data, title, steps):
    new_entry = pd.DataFrame({
        "Title": [title], 
        "Steps": [steps], 
        "Completed": [[False]*len(steps)]
    })
    data = pd.concat([data, new_entry], ignore_index=True)
    save_local_data(data)
    return data

def edit_title_steps(data, entry_id, updated_title, updated_steps):
    data.at[entry_id, "Title"] = updated_title
    data.at[entry_id, "Steps"] = updated_steps
    data.at[entry_id, "Completed"] = [False]*len(updated_steps)  # Reset completion status
    save_local_data(data)
    return data

def delete_entry(data, entry_id):
    data = data.drop(index=entry_id).reset_index(drop=True)
    save_local_data(data)
    return data

def toggle_step_completion(data, entry_id, step_index):
    data.at[entry_id, "Completed"][step_index] = not data.at[entry_id, "Completed"][step_index]
    save_local_data(data)
    return data

# Load data from CSV
data = get_local_data()

# Expanded demo data
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
    {
        "Title": "Hire Team Members",
        "Steps": [
            "Define roles and responsibilities.",
            "Create job descriptions.",
            "Post job openings on relevant platforms.",
            "Conduct interviews and select candidates.",
            "Onboard new employees and provide training.",
            "Develop a team-building program.",
            "Set performance expectations.",
            "Implement employee feedback mechanisms.",
            "Offer professional development opportunities.",
            "Review and adjust team structure as needed."
        ]
    },
    {
        "Title": "Prepare Financial Plan",
        "Steps": [
            "Estimate startup costs and ongoing expenses.",
            "Create a budget and financial projections.",
            "Determine pricing strategies.",
            "Plan for funding sources and investments.",
            "Monitor and adjust financial plans regularly.",
            "Establish financial controls and processes.",
            "Prepare for tax obligations.",
            "Set up accounting software.",
            "Review financial performance monthly.",
            "Create a financial risk management plan."
        ]
    },
    {
        "Title": "Set Up Customer Support",
        "Steps": [
            "Choose a customer support platform.",
            "Develop a customer service policy.",
            "Train staff on customer service best practices.",
            "Implement a ticketing system.",
            "Gather and analyze customer feedback.",
            "Set up an FAQ and knowledge base.",
            "Develop a live chat support option.",
            "Create a customer feedback loop.",
            "Monitor and improve response times.",
            "Evaluate customer satisfaction regularly."
        ]
    },
    {
        "Title": "Compliance and Legal Requirements",
        "Steps": [
            "Research local, state, and federal regulations.",
            "Obtain necessary licenses and permits.",
            "Register trademarks and patents as needed.",
            "Draft and review legal documents.",
            "Ensure compliance with data protection laws.",
            "Set up a legal advisory team.",
            "Implement a compliance monitoring system.",
            "Conduct regular legal audits.",
            "Stay updated on legal changes.",
            "Develop a legal risk management plan."
        ]
    },
    {
        "Title": "Create Product Development Plan",
        "Steps": [
            "Define product vision and objectives.",
            "Conduct market research and analysis.",
            "Develop product specifications.",
            "Create a prototype or MVP (Minimum Viable Product).",
            "Test the prototype with target users.",
            "Gather feedback and iterate on design.",
            "Plan for product manufacturing or production.",
            "Develop a product launch strategy.",
            "Establish a product support system.",
            "Monitor product performance and gather post-launch feedback."
        ]
    },
    {
        "Title": "Develop Sales Strategy",
        "Steps": [
            "Identify target market segments.",
            "Develop a sales funnel and process.",
            "Create sales goals and metrics.",
            "Train sales team on strategies and techniques.",
            "Implement CRM (Customer Relationship Management) software.",
            "Develop sales collateral and presentations.",
            "Conduct market and competitor analysis.",
            "Launch sales campaigns and promotions.",
            "Monitor sales performance and adjust strategy.",
            "Build and maintain customer relationships."
        ]
    },
    {
        "Title": "Establish Partnership Agreements",
        "Steps": [
            "Identify potential business partners.",
            "Define partnership goals and benefits.",
            "Negotiate terms and agreements.",
            "Draft and review partnership contracts.",
            "Establish communication and collaboration processes.",
            "Monitor partnership performance.",
            "Resolve conflicts and issues as they arise.",
            "Review and update partnership agreements regularly.",
            "Celebrate successes and achievements.",
            "Explore opportunities for expanding partnerships."
        ]
    },
    {
        "Title": "Plan for Business Expansion",
        "Steps": [
            "Identify growth opportunities and markets.",
            "Develop a business expansion strategy.",
            "Create a detailed expansion plan and timeline.",
            "Secure funding for expansion.",
            "Implement expansion initiatives.",
            "Monitor and evaluate expansion progress.",
            "Adjust strategies based on market feedback.",
            "Expand product or service offerings.",
            "Scale operations and infrastructure.",
            "Review and optimize expansion processes."
        ]
    },
    {
        "Title": "Implement Quality Assurance Processes",
        "Steps": [
            "Define quality standards and metrics.",
            "Develop quality assurance procedures.",
            "Train staff on quality standards.",
            "Conduct regular quality inspections.",
            "Implement a quality management system.",
            "Gather and analyze quality data.",
            "Address quality issues and implement improvements.",
            "Review and update quality procedures.",
            "Engage in continuous quality improvement.",
            "Ensure compliance with industry standards."
        ]
    },
]

# Add additional demo entries
for entry in additional_entries:
    data = add_title_steps(data, entry["Title"], entry["Steps"])

# Display Titles with Steps
for entry_id, entry_data in data.iterrows():
    entry_key = f"title-{entry_id}"
    with st.expander(entry_data["Title"], expanded=False):
        st.write("### Steps:")
        steps = eval(entry_data["Steps"])
        completed = eval(entry_data["Completed"])
        for step_index, (step, completed_status) in enumerate(zip(steps, completed)):
            checkbox_label = f"{step}"
            if st.checkbox(checkbox_label, value=completed_status, key=f"checkbox-{entry_id}-{step_index}"):
                data = toggle_step_completion(data, entry_id, step_index)
        
        # Edit button and functionality
        if st.button("Edit", key=f"edit-{entry_id}"):
            updated_title = st.text_input("Title", value=entry_data["Title"])
            updated_steps = st.text_area("Steps (one per line)", value="\n".join(steps))
            if st.button("Save Changes", key=f"save-{entry_id}"):
                data = edit_title_steps(data, entry_id, updated_title, updated_steps.split("\n"))
                st.experimental_rerun()
        
        # Delete button and functionality
        if st.button("Delete", key=f"delete-{entry_id}"):
            data = delete_entry(data, entry_id)
            st.experimental_rerun()

# Functionality to add a new title with steps
with st.expander("Add New Title and Steps", expanded=False):
    title = st.text_input("New Title")
    steps = st.text_area("Steps (one per line)")
    if st.button("Add Title and Steps"):
        data = add_title_steps(data, title, steps.split("\n"))
        st.experimental_rerun()

st.write("### Business Blueprint 101 - Organized and ready to go!")
