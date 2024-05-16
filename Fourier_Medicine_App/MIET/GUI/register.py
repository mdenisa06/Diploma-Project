import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate(
    'C:\\Users\\Denisa\\Desktop\\Diploma Project\\Diploma-Project\\Fourier_Medicine_App\\MIET\\keys\\imagenius-f0848-firebase-adminsdk-t93aw-dc327ff9c3.json')
firebase_admin.initialize_app(cred)


def register_account(doctor_id, password):
    try:
        user = auth.create_user(email=doctor_id+"@imagenius.com", password=password)
        return True
    except Exception as e:
        print("Error:", e)
        return False
