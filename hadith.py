#!/usr/bin/python

from google.cloud import firestore
import sqlite3

db = firestore.Client(project='hadeeth')

db.collection()

doc_ref = db.collection('صحيح البخاري').document(' {"BookId":1,"Name":" كتاب الطهارة","NameEn":"Purification (Kitab Al-Taharah)"}')


doc_ref.set({
    'first': 'Ada1',
    'last': 'Lovelace',
    'born': 1815
})