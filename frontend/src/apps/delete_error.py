from ctypes import sizeof
import streamlit as st
import requests

def app(data):
    header = st.container()
    remove_error_form = st.form("remove_error_by_name")

    #session = requests.Session()

    with header:
        st.title('Errors Management System')

    with remove_error_form:
        error_name = st.text_input('Error name:')
        submitted = st.form_submit_button("Submit")
        directed_url = f"http://backend:8000/api/v1/errors/{error_name}"

        if submitted:
            response = requests.delete(directed_url)
            #st.write(data['name'])
            if error_name == '':
                st.warning("Plese fill the error name field first")
            else:
                if(response.status_code == 404):
                    st.warning(f"{error_name} doesn't exist already")
                else:
                    st.success(error_name + " - removed!")
