import streamlit as st

# Set the title of the Streamlit app
st.title("Visitor Management System")

# Create navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Login Page", "Visitor Check-In"])

# Load HTML files based on the selection
if page == "Home":
    with open("index.html", "r") as file:
        html_content = file.read()
    st.components.v1.html(html_content, height=800, scrolling=True)

elif page == "Login Page":
    with open("loginpage.html", "r") as file:
        html_content = file.read()
    st.components.v1.html(html_content, height=600, scrolling=True)

elif page == "Visitor Check-In":
    with open("visitors.html", "r") as file:
        html_content = file.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
