import functions_framework
from google.cloud import firestore

@functions_framework.http
def hello_http(request):
    db = firestore.Client(project="hadeeth")
    args = str(request.path).split('/')
    doc = db.collection(args[1]).document(str(args[2])).get()

    if(doc.to_dict() == None):
        return {'Error':'Hadith not found!'}
    return doc.to_dict()