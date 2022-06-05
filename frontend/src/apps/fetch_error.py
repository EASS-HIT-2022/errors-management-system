from ctypes import sizeof
import streamlit as st
import requests

def app(data):
    header = st.container()
    fetch_errors_form = st.form("new_error")

    session = requests.Session()

    def fetch(session, url):
        try:
            result = session.get(url)
            return result.json()
        except Exception:
            return {}

    with header:
        st.title('Errors Management System')

    with fetch_errors_form:
        error_name = st.text_input('Error name (submitting without error name will show all the errors):')
        submitted = st.form_submit_button("Submit")
        if submitted:
            data = fetch(session, f"http://backend:8000/api/v1/errors/{error_name}")
            #st.write(data['name'])
            if error_name == '':
                if len(data) == 0:
                    st.error('The system is empty from errors')
                else:
                    st.success(f"Showing all the {len(data)} errors")

                    # print the complete data at once
                    #st.write(data)
                    
                    # print each param  
                    for error in data:
                        st.write("The error name: ", error['name'])
                        st.write("The priority is: ", error['priority'])
                        st.write("These are the involved when the error was raised: ", error['involved'])
                        st.write("What you should do next: ", error['next_step'])
                        st.write("The accepted date: ", error['accept_date'])
                        st.write("___________________________________________________")
                


            else:
                if('detail' in data):
                    st.warning(f'Have no error called {error_name}')
                else:
                    st.success(error_name + " - has been found")

                    # print the complete data at once
                    #st.write(data)
                    
                    # print each param 
                    st.write("The priority is: ", data['priority'])
                    st.write("These are the involved when the error was raised: ", data['involved'])
                    st.write("What you should do next: ", data['next_step'])
                    st.write("The accepted date: ", data['accept_date'])
