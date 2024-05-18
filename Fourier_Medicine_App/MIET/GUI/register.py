from firebase_init import *
from firebase_admin import auth


def register_account(doctor_id, password):
    try:
        user = auth.create_user(email=doctor_id+"@imagenius.com", password=password)
        return True
    except auth.EmailAlreadyExistsError:
        print("Error: The email already exists.")
        return False
    except Exception as e:
        print("Error:", e)
        return False
