from firebase_init import *
from firebase_admin import auth
import requests

API_KEY = 'AIzaSyA7tdgSDiAAYOgfxlU95RakOGGRdSc7nOU'


def login_account(email, password):
    try:
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}'
        payload = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            user_info = response.json()
            uid = user_info.get('localId')
            return "Login successful", uid
        else:
            error_message = response.json().get('error', {}).get('message', '')
            raise ValueError(error_message)

    except ValueError as e:
        error_message = str(e)
        if error_message == 'USER_NOT_FOUND':
            return "The email does not exist.", None
        elif error_message == 'INVALID_PASSWORD':
            return "The password is invalid.", None
        elif error_message == 'INVALID_LOGIN_CREDENTIALS':
            return "Incorrect username or password. Try again. If you don't have an account, sign in by filling the Register Form.", None
        elif error_message == 'INVALID_EMAIL':
            return "The email address is badly formatted. Please check and try again.", None
        else:
            print("Unexpected error message:", error_message)
            return "Login failed. An unexpected error occurred.", None
    except Exception as e:
        print("Unexpected error message:", e)
        return "Login failed. An unexpected error occurred.", None
