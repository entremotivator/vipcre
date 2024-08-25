import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

# Sidebar content
st.sidebar.image("path/to/your/logo.png", use_column_width=True)
st.sidebar.success("Select a page above.")

# Main page content
st.title("Main Page")
st.write("Welcome to the Multipage App!")

# Information or description
st.write("""
This application allows you to navigate through multiple pages.
You can input text below, and your input will be displayed on the page.
""")

# Text input and session state handling
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")

# Display entered text
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
