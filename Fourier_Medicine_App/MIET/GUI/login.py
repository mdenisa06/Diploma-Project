from firebase_init import *
from firebase_admin import auth
import requests

API_KEY = 'AIzaSyA7tdgSDiAAYOgfxlU95RakOGGRdSc7nOU'


def login_account(email, password):
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}'
    payload = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return "Login successful"
    else:
        error_message = response.json().get('error', {}).get('message', '')
        if error_message == 'INVALID_LOGIN_CREDENTIALS':
            return "Wrong email/password or account not created. Please try again."
        else:
            print("Unexpected error message:", error_message)
            return "Login failed. An unexpected error occurred."
