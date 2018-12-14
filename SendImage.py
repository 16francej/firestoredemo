import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import base64

# Use the application default credentials
from RecieveImage import keyPath


def initializeDb(path):
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def imageToString(path):
    serialImage = u'NOT FOUND'
    with open(path) as imageFile:
        serialImage = base64.b64encode(imageFile.read())
        return serialImage


def addToDB(database, collectionName, documentName, json):
    doc_ref = database.collection(collectionName).document(documentName)
    doc_ref.set(json)


def main():
    # Use a service account
    db = initializeDb(keyPath)

    serialImage = imageToString('images/trollface.jpg')

    addToDB(db, u'users', u'alovelace', {
        u'first': u'Adam',
        u'last': u'Lovelaced',
        u'born': serialImage
    })


if __name__ == '__main__':
    main()
