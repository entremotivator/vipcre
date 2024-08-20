import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Initialize Streamlit app
st.set_page_config(page_title="Business Blueprint 101")

# UI
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
    return pd.read_csv("local_data.csv") if "local_data.csv" in os.listdir() else pd.DataFrame(columns=["Title", "Steps"])

def add_title_steps(title, steps):
    global data
    new_entry = {"Title": title, "Steps": steps}
    data = data.append(new_entry, ignore_index=True)
    save_local_data()

def edit_title_steps(entry_id, updated_title, updated_steps):
    global data
    entry_index = entry_id
    data.at[entry_index, "Title"] = updated_title
    data.at[entry_index, "Steps"] = updated_steps
    save_local_data()

def delete_entry(entry_id):
    global data
    data = data.drop(index=entry_id).reset_index(drop=True)
    save_local_data()

# Load data from CSV
load_local_data()

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
    {
        "Title": "Logo & Tag Line",
        "Steps": [
            "Hire a designer or use a logo design tool.",
            "Brainstorm taglines that represent your brand's mission.",
            "Ensure the logo and tagline are consistent with brand identity.",
            "Test your logo and tagline with your target audience.",
            "Refine and finalize the design based on feedback."
        ]
    },
    {
        "Title": "Secure Business Address",
        "Steps": [
            "Decide whether you need a physical or virtual address.",
            "Research potential business address locations.",
            "Consider using a virtual mailbox service.",
            "Register your business address with government agencies.",
            "Update all your business documents with the new address."
        ]
    },
    {
        "Title": "Purchase State Corporation",
        "Steps": [
            "Choose the state to incorporate your business.",
            "Select the type of corporation (LLC, S-Corp, C-Corp, etc.).",
            "File the Articles of Incorporation with the state.",
            "Create an operating agreement or bylaws.",
            "Obtain your Certificate of Incorporation."
        ]
    },
    {
        "Title": "EIN Number",
        "Steps": [
            "Determine if your business needs an EIN.",
            "Apply for an EIN through the IRS website.",
            "Receive your EIN immediately after applying.",
            "Keep your EIN number in a secure place.",
            "Use the EIN for tax filing and business accounts."
        ]
    },
    {
        "Title": "Business Accounts",
        "Steps": [
            "Research banks that offer business accounts.",
            "Compare account features, fees, and requirements.",
            "Gather required documentation (EIN, Articles of Incorporation, etc.).",
            "Open a business checking account.",
            "Consider setting up a business savings account."
        ]
    },
    {
        "Title": "Business License",
        "Steps": [
            "Identify the licenses required for your business.",
            "Apply for necessary local, state, and federal licenses.",
            "Pay the applicable fees for each license.",
            "Display the business licenses in your workplace.",
            "Renew licenses as required by law."
        ]
    },
    {
        "Title": "Business Insurance",
        "Steps": [
            "Determine the types of insurance your business needs.",
            "Get quotes from multiple insurance providers.",
            "Choose the best coverage for your budget and needs.",
            "Purchase the required insurance policies.",
            "Review and update insurance policies annually."
        ]
    },
    {
        "Title": "Trademarks & Copy Rights",
        "Steps": [
            "Search for existing trademarks similar to yours.",
            "File a trademark application with the USPTO.",
            "Register your business's original content with the Copyright Office.",
            "Monitor your intellectual property for infringements.",
            "Renew your trademarks and copyrights as needed."
        ]
    },
    {
        "Title": "Domain Name & Website",
        "Steps": [
            "Choose a domain name that matches your business name.",
            "Check domain name availability and purchase it.",
            "Choose a reliable web hosting service.",
            "Design and develop your website or hire a web developer.",
            "Optimize your website for search engines (SEO)."
        ]
    },
    {
        "Title": "Business Email & Number",
        "Steps": [
            "Set up a professional business email address.",
            "Choose a business phone service provider.",
            "Set up a dedicated business phone number.",
            "Consider adding a toll-free number if needed.",
            "Ensure contact information is consistent across all platforms."
        ]
    },
    {
        "Title": "Duns Number",
        "Steps": [
            "Determine if your business needs a DUNS number.",
            "Apply for a DUNS number through the D&B website.",
            "Provide accurate business information during the application.",
            "Use the DUNS number to establish business credit.",
            "Keep your DUNS information up to date."
        ]
    },
    {
        "Title": "Nav Number",
        "Steps": [
            "Understand the purpose of a Nav Number.",
            "Register for a Nav account online.",
            "Use the Nav Number to monitor your business credit.",
            "Check for discrepancies in your business credit report.",
            "Regularly update your Nav Number information."
        ]
    },
    {
        "Title": "Sams Number",
        "Steps": [
            "Determine if your business requires a SAMS number.",
            "Register for a SAMS number through the federal SAM system.",
            "Complete the registration process by providing necessary documents.",
            "Use the SAMS number for government contracting opportunities.",
            "Update your SAMS registration annually."
        ]
    },
    {
        "Title": "SAMHSA - 501c3",
        "Steps": [
            "Determine if your nonprofit qualifies for 501c3 status.",
            "File for 501c3 status with the IRS.",
            "Provide detailed information about your nonprofit's purpose.",
            "Maintain compliance with federal 501c3 regulations.",
            "Renew your 501c3 status as required."
        ]
    },
    {
        "Title": "Learn About Business Trade-lines",
        "Steps": [
            "Research the benefits of business trade-lines.",
            "Identify potential trade-line partners.",
            "Apply for trade-lines with vendors.",
            "Monitor your trade-line accounts regularly.",
            "Use trade-lines to build business credit."
        ]
    },
    {
        "Title": "Business Funding",
        "Steps": [
            "Identify the funding needs of your business.",
            "Research potential funding sources (loans, grants, investors).",
            "Prepare a detailed business plan and financial projections.",
            "Apply for funding from various sources.",
            "Manage the funds to ensure financial sustainability."
        ]
    },
    {
        "Title": "Business Accounting & Taxes",
        "Steps": [
            "Set up a reliable accounting system.",
            "Track all business income and expenses accurately.",
            "Hire an accountant or use accounting software.",
            "File taxes according to local, state, and federal regulations.",
            "Review financial statements regularly to assess business health."
        ]
    },
    {
        "Title": "Company Branding Tools",
        "Steps": [
            "Identify the core values of your brand.",
            "Design branding materials (logo, business cards, etc.).",
            "Develop a consistent brand message.",
            "Implement branding across all business platforms.",
            "Evaluate and refine your brand strategy regularly."
        ]
    },
    {
        "Title": "CDIA & EDGAR & Data Furnishing",
        "Steps": [
            "Understand the role of CDIA and EDGAR in business data.",
            "Ensure compliance with CDIA and EDGAR regulations.",
            "Use CDIA & EDGAR resources to manage business data.",
            "Implement data furnishing practices in your business.",
            "Regularly review and update data practices to remain compliant."
        ]
    }
]

# Display Titles with Steps
for entry_id, entry_data in enumerate(example_entries):
    entry_key = f"title-{entry_id}"
    with st.expander(entry_key):
        with st.expander(entry_data["Title"]):
            st.write("### Steps:")
            for step in entry_data["Steps"]:
                st.write(f"- {step}")
            if st.button("Edit Title and Steps"):
                updated_title = st.text_input("Title", value=entry_data["Title"])
                updated_steps = st.text_area("Steps (one per line)", value="\n".join(entry_data["Steps"]))
                edit_title_steps(entry_id, updated_title, updated_steps.split("\n"))
            if st.button("Delete Entry"):
                delete_entry(entry_id)

# Functionality to add a new title with steps
with st.expander("Add New Title and Steps"):
    title = st.text_input("Title")
    steps = st.text_area("Steps (one per line)")
    if st.button("Add Title and Steps"):
        add_title_steps(title, steps.split("\n"))

st.write("### Business Blueprint 101 - Organized and ready to go!")
