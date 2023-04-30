# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:45:55 2023

@author: RITHVIK
"""
from deta import Deta
import bcrypt
import streamlit as st

# Initialize with a project key
deta = Deta(st.secrets["DETA_KEY"]) 
# This is how to create/connect a database
db = deta.Base("heart_result")

def insert_data(val,username):
    result = db.get(username)
    result['Result'].append(val)
    db.put(result)

d=deta.Base("heart_users")
def insert_user(username,password):
     d.put({"key":username,"password":password});
     db.put({"key":username,"Result":[]})
     return
def get_user(username):
    result = d.get(username)
    if result and result["key"] == username:
        return True
    return False
def compare(username, password):
    result = d.get(username)
    if result and bcrypt.checkpw(password.encode('utf-8'), result["password"].encode('utf-8')):
        return True
    return False
    
