import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('C:\\Users\\Denisa\\Desktop\\Diploma Project\\Diploma-Project\\Fourier_Medicine_App\\MIET\\keys\\imagenius-f0848-firebase-adminsdk-t93aw-dc327ff9c3.json')

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()