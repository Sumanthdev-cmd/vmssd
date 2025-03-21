import streamlit as st

st.set_page_config(page_title="Malnad College Visitors Management System", layout="centered")

st.title("Malnad College Visitors Management System")
st.markdown("---")

menu = ["Home", "Login", "Visitor Check-In", "Visitor Log", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("About Us")
    st.write("Welcome to our prestigious college where excellence meets education.")

elif choice == "Login":
    st.subheader("Login Page")
    user_id = st.text_input("Enter User ID")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if (user_id, password) in [("user1", "password1"), ("user2", "password2")]:
            st.success("Login successful!")
        else:
            st.error("Invalid User ID or Password")

elif choice == "Visitor Check-In":
    st.subheader("Visitor Check-In Form")
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    purpose = st.text_input("Purpose of Visit")
    person = st.text_input("Person to Visit")
    designation = st.text_input("Designation")
    if st.button("Submit"):
        st.success("Visitor Checked In Successfully!")

elif choice == "Visitor Log":
    st.subheader("Visitor Log")
    sample_data = [
        ["John Doe", "1234567890", "Meeting", "Dr. Smith", "Professor"],
        ["Jane Smith", "0987654321", "Interview", "Dr. John", "Dean"]
    ]
    st.table(sample_data)

elif choice == "Contact":
    st.subheader("Contact Us")
    st.write("Email: contact@collegename.edu | Phone: 123-456-7890")

st.markdown("---")
st.text("© 2025 Malnad College of Engineering. All rights reserved.")

