#from distutils.log import error
from datetime import datetime
from datetime import date
from distutils.log import error
from sqlite3 import Date
import streamlit as st 
import requests

import json
import time

def app(data):
    header = st.container()
    user_detail = st.container()
    list_update_error_form = st.form("list_of_error_changes")
    update_error_form = st.form("update_error")


    with header:
        st.title('Errors Management System')

    with user_detail:
        st.subheader('Hello David Rimon')
        st.write('if you want to live check out the [David home page](https://www.google.com)')

    with update_error_form:
        input_error = {}

        error_name = st.text_input('error name for update:')

        '''error_name = st.text_input("New error name")
        if error_name != "":
            input_error['name'] = error_name'''

        priority= st.radio("Priority:",('Low','Medium','High','Blocker'))
        if priority != "":
            input_error['priority'] = priority

        next_step = st.text_area("Next step:", placeholder="list of missions to do") 
        if next_step != "":
            input_error['next_step'] = next_step

        submitted = st.form_submit_button("Submit")        
        updated_date = date.today()
        d1 = updated_date.strftime("%Y-%m-%d")
        input_error['update_date'] = d1

        if submitted:
            if error_name == '':
                st.warning('You have to fill the error name that you want to change')
            else:
                API_URL = f"http://localhost:8000/api/v1/errors/${error_name}"
                result_for_insert = requests.put(API_URL,data=input_error) 
                #result_for_insert.json
                if(result_for_insert.status_code == 200):
                    st.success(error_name + " - updated successfully!")
                    st.write("The priority is: ", priority)
                    #st.write("These are the involved when the error was raised: ", involved)
                    st.write("What you should do next: ", next_step)
                    #st.write("The accepted date: ", accepted_date)
                else:
                    st.write(result_for_insert)
                    st.write(input_error)

            
                