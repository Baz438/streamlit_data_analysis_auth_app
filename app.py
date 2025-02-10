import streamlit as st
import pandas as pd
import os

# Load user data
def load_users():
    return pd.read_csv("users.csv")

users_df = load_users()

# Login page
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users_df[(users_df["name"] == username) & (users_df["password"] == password)]
        
        if not user.empty:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")

# Home page
def home_page():
    st.title("Data Analysis page")
    st.write("Welcome to the Data Analysis page of Bazzah! Use the sidebar to navigate.")

    image_url = "https://cdn.pixabay.com/photo/2023/11/19/06/07/business-8398064_640.jpg"  
    st.image(image_url, caption="Dive into Data!", use_container_width=True)

# Gallery page with images
def gallery_page():
    st.title("Data Analysis Gallery")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Data Visualization")
        st.image("https://cdn.pixabay.com/photo/2024/04/05/05/16/businesswoman-8676522_640.jpg", caption="Charts & Graphs")
    
    with col2:
        st.header("Machine Learning")
        st.image("https://cdn.pixabay.com/photo/2023/02/05/19/05/robot-7770312_640.jpg ", caption="AI & ML Models")
    
    with col3:
        st.header("Big Data")
        st.image("https://cdn.pixabay.com/photo/2022/12/09/11/47/big-data-7645171_640.jpg", caption="Large-Scale Processing")

# Main function
def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
    else:
        st.sidebar.title(f"Hello, {st.session_state['username']}!")
        page = st.sidebar.radio("Navigation", ["Home", "Gallery"])

        if st.sidebar.button("Logout"):
            st.session_state["logged_in"] = False

        if page == "Home":
            home_page()
        elif page == "Gallery":
            gallery_page()

# Run the app
if __name__ == "__main__":
    main()
