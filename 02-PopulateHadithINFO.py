#!/usr/bin/python

import sqlite3
from google.cloud import firestore

conn = sqlite3.connect("/home/alfi/Projects/hadeeth/hadeeth.db")

print("Opened database successfully")

cursor = conn.execute(
    '''SELECT
	b.collection_id ,
	c.name,
	b.id,
	b.title,
	b.display_number,
	b.order_in_collection,
	b.intro,
	b.hadith_start,
	b.hadith_end,
	b.hadith_count,
	b.title_en,
	b.intro_en
from
	collection c
inner join book b on
	c.id = b.collection_id 
order by
	b.collection_id, b.order_in_collection'''
)
db = firestore.Client(project="hadeeth")
collectionName = 'bukhari'
data = []
for row in cursor:
    dict = {}
    if collectionName != row[1]:
        infoDoc = db.collection(collectionName).document("INFO")
        infoDoc.set({'Books':data})
        # print('{0} {1}\n\n'.format(collectionName, data))
        data = []
        collectionName = row[1]
    dict["id"] = row[2]
    dict["title"] = row[3]
    dict["display_number"] = row[4]
    dict["order_in_collection"] = row[5]
    dict["intro"] = row[6]
    dict["hadith_start"] = row[7]
    dict["hadith_end"] = row[8]
    dict["hadith_count"] = row[9]
    dict["title_en"] = row[10]
    dict["intro_en"] = row[11]
    data.append(dict)

print(data)


# infoDoc = db.collection("INFO").document("INFO")

# infoDoc.set({'Collections':data})

# print("Operation done successfully")

conn.close()
