import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

# Use the following code (in comments) in the Python terminal first to hash the password in the user.yaml and replace it
#  import streamlit_authenticator as stauth
#  hashed_passwords = stauth.Hasher(['admin', 'abc123','bonjovirocks']).generate()
#  print(hashed_passwords)


# function being called to Dashboard for user authentication
def user_auth_system():
    with open("utility/user.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    name, authentication_status, username = authenticator.login(
        "Welcome to the AnaeroDash App!", "main"
    )
    return name, authentication_status, username, authenticator
