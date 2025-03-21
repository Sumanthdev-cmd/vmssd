import streamlit as st

# Page Configuration
st.set_page_config(page_title="Malnad College Visitors", layout="wide")

# Navigation
menu = ["Home", "Login", "Visitor Check-In"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.title("Welcome to Malnad College of Engineering!")
    st.markdown("Here's the Visitor's Management System.")

    st.image("./WhatsApp Image 2025-03-04 at 16.24.44_1b7a5269.jpg", width=700)
    st.write("### About Us")
    st.write("Welcome to our prestigious college where excellence meets education.")
    st.write("### Contact Us")
    st.write("Email: contact@collegename.edu | Phone: 123-456-7890")

elif choice == "Login":
    st.title("Login Page")
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if (user_id == 'user1' and password == 'password1') or (user_id == 'user2' and password == 'password2'):
            st.success("Login successful!")
            st.session_state['authenticated'] = True
        else:
            st.error("Invalid User ID or Password")

elif choice == "Visitor Check-In":
    if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
        st.warning("Please login first.")
    else:
        st.title("Visitor Check-In")
        with st.form("checkin_form"):
            name = st.text_input("Full Name:")
            phone = st.text_input("Phone Number:")
            purpose = st.text_input("Purpose of Visit:")
            person = st.text_input("Person to Visit:")
            designation = st.text_input("Designation:")
            date = st.date_input("Date:")
            time = st.time_input("Check-In Time:")
            submit = st.form_submit_button("Check-In")

        if submit:
            st.success("Visitor checked in successfully!")
            if 'visitor_log' not in st.session_state:
                st.session_state['visitor_log'] = []
            st.session_state['visitor_log'].append(
                {"Name": name, "Phone": phone, "Purpose": purpose, "Person": person, "Designation": designation, "Date": date, "Time": time}
            )

        st.write("### Visitor Log")
        if 'visitor_log' in st.session_state:
            st.table(st.session_state['visitor_log'])
