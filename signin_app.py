import streamlit as st

# Function to display home page and sign-in form
def home_page():
    st.title("Welcome to the Portal")

    # Create a form for the sign-in page
    with st.form(key='sign_in_form'):
        st.subheader("Sign In")
        
        # Username input field
        username = st.text_input("Username")

        # Password input field
        password = st.text_input("Password", type='password')

        # Select user role (student, staff, admin)
        role = st.selectbox("Select Role", ["Student", "Staff", "Admin"])

        # Submit button
        submit_button = st.form_submit_button("Sign In")

        # After submission, check the role and display appropriate messages
        if submit_button:
            if username and password:
                # You can add logic for authentication here, e.g., check username and password
                # (This is just a rough example, ideally, you'll have a proper database and encryption)
                
                st.write(f"Signed in as: {username} ({role})")
                
                # Display role-specific content after sign-in
                if role == "Student":
                    st.write("Welcome Student! Here are your resources...")
                elif role == "Staff":
                    st.write("Welcome Staff! Here are your tools...")
                elif role == "Admin":
                    st.write("Welcome Admin! You have full access to the system...")

            else:
                st.error("Please enter both username and password.")

# Call the home_page function to display the page
if __name__ == '__main__':
    home_page()

import streamlit as st

# Create a dialog function. All elements inside it will appear in the modal dialog.
@st.dialog("Dialog Title")
def show_dialog():
    st.write("This is a dialog box!")
    st.text_input("Enter some text:")
    if st.button("Close"):
        st.rerun()  # Close the dialog programmatically

# Open the dialog when the button is clicked.
if st.button("Open Dialog"):
    show_dialog()

