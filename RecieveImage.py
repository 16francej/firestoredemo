import google
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import base64

keyPath = '../firestoreKEY.json'


def initializeDb(path):
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def stringToImage(string, imagePath):
    fh = open(imagePath, "wb")
    fh.write(string.decode('base64'))
    fh.close()


def getFieldFromDB(database, collectionName, docName, fieldName):
    dbRef = database.collection(collectionName).document(docName)
    try:
        doc = dbRef.get()
        str = doc.to_dict()[fieldName]
    except google.cloud.exception.NotFound:
        str = 'NO SUCH DOCUMENT'

    return str

def main():
    database = initializeDb(keyPath)
    str = getFieldFromDB(database, u'users', u'alovelace', u'born')
    stringToImage(str, 'images/trollfaceDECODED.jpg')


if __name__ == '__main__':
    main()
