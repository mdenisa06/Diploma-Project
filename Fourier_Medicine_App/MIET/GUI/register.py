from firebase_init import *
from firebase_admin import auth


def register_account(name, last_name, doctor_id, password):
    try:
        user = auth.create_user(email=doctor_id+"@imagenius.com", password=password)
        user_info = {
            "name": name,
            "last_name": last_name,
            "doctor_id": doctor_id
        }

        db.collection('users').document(user.uid).set(user_info)

        return True
    except auth.EmailAlreadyExistsError:
        print("Error: The email already exists.")
        return False
    except Exception as e:
        print("Error:", e)
        return False
