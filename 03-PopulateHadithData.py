#!/usr/bin/python

import sqlite3
from google.cloud import firestore

conn = sqlite3.connect("/home/alfi/Projects/hadeeth/hadeeth.db")

print("Opened database successfully")

cursor = conn.execute(
    """SELECT
		c.name collection_name,
		c.title collection_title,
		h.book_id,
		b.title book_name,
		c2.title chapter_name,
		CASE
			h.chapter_id - h.prev_chapter_id
		when 0 then 0
			else 1
		end is_first_hadith_of_chapter,
		h.display_number,
		h.order_in_book,
		h.narrator_prefix,
		h.content,
		h.narrator_postfix,
		h.narrator_prefix_diacless,
		h.content_diacless,
		h.narrator_postfix_diacless,
		h.comments,
		h.grades,
		h.narrators,
		h.related_hadiths
	from
		(
		SELECT
		h.urn,
			h.collection_id,
			h.book_id,
			h.chapter_id,
			LAG ( h.chapter_id,
			1,
			0 ) OVER (
		ORDER BY
			collection_id,
			book_id ,
			order_in_book  
		) prev_chapter_id,
			h.display_number,
			h.order_in_book,
			h.narrator_prefix,
			h.content,
			h.narrator_postfix,
			h.narrator_prefix_diacless,
			h.content_diacless,
			h.narrator_postfix_diacless,
			h.comments,
			h.grades,
			h.narrators,
			h.related_hadiths
		from
			hadith h
			) h
	inner  join collection c on
			c.id = h.collection_id
	left outer join book b on
			b.collection_id = h.collection_id
			and b.id = h.book_id
	left outer JOIN chapter c2 on
			c2.collection_id = h.collection_id
		and 
			c2.book_id = h.book_id
		and
			c2.id = h.chapter_id
	EXCEPT
		SELECT
		c.name collection_name,
		c.title collection_title,
		h.book_id,
		b.title book_name,
		c2.title chapter_name,
		CASE
			h.chapter_id - h.prev_chapter_id
		when 0 then 0
			else 1
		end is_first_hadith_of_chapter,
		h.display_number,
		h.order_in_book,
		h.narrator_prefix,
		h.content,
		h.narrator_postfix,
		h.narrator_prefix_diacless,
		h.content_diacless,
		h.narrator_postfix_diacless,
		h.comments,
		h.grades,
		h.narrators,
		h.related_hadiths
	from
		(
		SELECT
		h.urn,
			h.collection_id,
			h.book_id,
			h.chapter_id,
			LAG ( h.chapter_id,
			1,
			0 ) OVER (
		ORDER BY
			collection_id,
			book_id ,
			order_in_book  
		) prev_chapter_id,
			h.display_number,
			h.order_in_book,
			h.narrator_prefix,
			h.content,
			h.narrator_postfix,
			h.narrator_prefix_diacless,
			h.content_diacless,
			h.narrator_postfix_diacless,
			h.comments,
			h.grades,
			h.narrators,
			h.related_hadiths
		from
			hadith h
			) h
	inner  join collection c on
			c.id = h.collection_id
	inner join book b on
			b.collection_id = h.collection_id
			and b.id = h.book_id
	inner JOIN chapter c2 on
			c2.collection_id = h.collection_id
		and 
			c2.book_id = h.book_id
		and
			c2.id = h.chapter_id	"""
)
db = firestore.Client(project="hadeeth")
for row in cursor:
    # if collectionName != row[0]:
    infoDoc = db.collection(row[0]).document(str(row[6]).replace("/", ", "))
    # print('{0} {1}\n\n'.format(collectionName, data))
    infoDoc.set({
        "collection_name": row[0],
        "collection_title": row[1],
        "book_id": row[2],
        "book_name": row[3],
        "chapter_name": row[4],
        "is_first_hadith_of_chapter": row[5],
        "display_number": row[6],
        "order_in_book": row[7],
        "narrator_prefix": row[8],
        "content": row[9],
        "narrator_postfix": row[10],
        "narrator_prefix_diacless": row[11],
        "content_diacless": row[12],
        "narrator_postfix_diacless": row[13],
        "comments": row[14],
        "grades": row[15],
        "narrators": row[16],
        "related_hadiths": row[17],
    })
    print("collection_name :", row[0])
    print("book_id :", row[2])
    print("display_number :", row[6])
    



# infoDoc = db.collection("INFO").document("INFO")

# infoDoc.set({'Collections':data})

# print("Operation done successfully")

conn.close()

# collection_name : ibnmajah
# book_id : 5
# display_number : 1397