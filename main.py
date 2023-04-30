# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:20:44 2023

@author: RITHVIK
"""

import streamlit as st
import heart as h
import database as db
import bcrypt

# Third change in april
st.set_page_config(page_title="Heart Disease prediction")
r = st.container()
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
def register():
    with r:
        st.header("Create an account")
        username = st.text_input("Username",placeholder="Enter")
        password = st.text_input("Password", type="password",placeholder="Enter")
        if st.session_state['loggedIn']:
            st.session_state['loggedIn'] = False
        if st.button("Register"):
            if username and password:
                if db.get_user(username):
                    st.warning("Username already exists. Please choose a different one.")
                else:
                    # Hash the password before storing it
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                    
                    # Convert the hashed password to a str object
                    hashed_password_str = hashed_password.decode('utf-8')
                    
                    db.insert_user(username,hashed_password_str)
                    st.success("Account created. click on login box ")
                
            else:
                st.warning("Enter values")
        
 
def show_main_page():
    mainSection.empty();
    with mainSection:
        if st.session_state['loggedIn']:
            h.main(st.session_state['loggedIn'],st.session_state.name) 
        
 
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    st.session_state.name=None
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.sidebar.title(f'WELCOME {st.session_state.name}!')
        st.sidebar.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(username1, password1):
    if len(username1)==0 or len(password1)==0:
        st.warning("enter username/password")
    else:
        if not db.get_user(username1):
            st.session_state['loggedIn'] = False;
            st.session_state.name=None
            st.warning("Invalid username. Please try again.")
        elif db.compare(username1, password1):
            st.session_state.name=username1
            st.session_state['loggedIn'] = True
        else:
            st.session_state['loggedIn'] = False;
            st.session_state.name=None
            st.warning("Invalid password. Please try again.")
        
    
def show_login_page():
    with loginSection:
        col1, col2 = st.columns(2,gap="large")
        s=True
        with col2:
            if st.checkbox("Sign up / Login",key="p"):
                s=False
                register()
        with col1:
            
            if st.session_state['loggedIn'] == False and s:
                    st.header("Login")
                    userName = st.text_input (label="", value="", placeholder="Enter your user name",key="new")
                    password = st.text_input (label="", value="",placeholder="Enter password", type="password",key="new1")
                    st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))

            

#Add a sidebar to switch between login and logout

with headerSection:
        #st.title("Streamlit Application")
        #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        st.session_state.name=None
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()  
        else:
            show_login_page()
