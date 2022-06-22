#from distutils.log import error
import streamlit as st 
import requests

import json
import time

def app(data):
    header = st.container()
    user_detail = st.container()
    new_error_form = st.form("new_error")

    with header:
        st.title('Errors Management System')

    with user_detail:
        st.subheader('Hello User')
        #st.write('if you want to live check out the [David home page](https://www.google.com)')

    with new_error_form:
        error_name = st.text_input('Error name:')
        priority= st.radio("Priority:",('Low','Medium','High','Blocker'))
        involved = st.multiselect("Involved:",("David Rimon","Daniel","Eden","Amit Kazir","Chen Ben Ezra","Bader","Ronit Golan","Laila Zoabi","Guy","Moshe Mharaban","Idan"))
        next_step = st.text_area("Next step:", placeholder="list of missions to do")
        accepted_date = st.date_input('accepted date')
        submitted = st.form_submit_button("Submit")

        if submitted:
            if error_name == '' or involved == "" or next_step == "":
                st.warning('You have to fill all the fields')
            else:
                input_error = {
                    "name": error_name,
                    "priority": priority,
                    "involved": involved,
                    "next_step": next_step,
                    "accept_date": accepted_date.strftime("%Y-%m-%dT%H:%M:%S")
                    #"accept_date": accepted_date.isoformat()
                }

                API_URL = "http://backend:8000/api/v1/errors"

                result_for_insert = requests.post(API_URL,json=input_error) 
                response_data = result_for_insert.json()
                
                if(result_for_insert.status_code == 200):
                    st.success(error_name + " - created successfully!")
                    st.write("The priority is: ", priority)
                    st.write("These are the involved when the error was raised: ", involved)
                    st.write("What you should do next: ", next_step)
                    st.write("The accepted date: ", accepted_date)
                else:
                    st.warning(response_data['detail'])
                







