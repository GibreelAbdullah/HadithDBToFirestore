#!/usr/bin/python

import sqlite3
from google.cloud import firestore

conn = sqlite3.connect("/home/alfi/Projects/hadeeth/hadeeth.db")

print("Opened database successfully")

cursor = conn.execute(
    "select id, name, type , title, title_en, short_description_en , numbering_source_en , has_volumes , has_books , has_chapters, status  from collection c"
)

data = []
for row in cursor:
    dict = {}
    
    dict['id'] = row[0]
    dict["name"] = row[1]
    dict["type"] = row[2]
    dict["title"] = row[3]
    dict["title_en"] = row[4]
    dict["short_description_en"] = row[5]
    dict["numbering_source_en"] = row[6]
    dict["has_volumes"] = row[7]
    dict["has_books"] = row[8]
    dict["has_chapters"] = row[9]
    dict["status"] = row[10]
    data.append(dict)

print(data)

db = firestore.Client(project="hadeeth")

infoDoc = db.collection("INFO").document("INFO")

infoDoc.set({'Collections':data})

print("Operation done successfully")

conn.close()
