ALTER TABLE collection ADD name text;

update collection set name = 'bukhari' where id = 1;
update collection set name = 'muslim' where id = 2;
update collection set name = 'nasai' where id = 3;
update collection set name = 'abudawud' where id = 10;
update collection set name = 'tirmidhi' where id = 30;
update collection set name = 'ibnmajah' where id = 38;
update collection set name = 'malik' where id = 40;
update collection set name = 'ahmad' where id = 50;
update collection set name = 'nawawi' where id = 101;
update collection set name = 'forty' where id = 102;
update collection set name = 'riyadussalihin' where id = 110;
update collection set name = 'mishkat' where id = 113;
update collection set name = 'adab' where id = 115;
update collection set name = 'shamail' where id = 130;
update collection set name = 'bulugh' where id = 200;
update collection set name = 'hisn' where id = 300;


--CollectionId = 30
--BookId = 37
--ChapterId = 60.0
--urn = 727072 display number 2521 is missing
update hadith set display_number = 2521 where urn = 727072;
update hadith set display_number = 512 where urn = 1105131;
update hadith set display_number = 570 where urn = 1105722;
update hadith set display_number = '160 a' where urn = 5601605;


	select * from hadith where urn not in (
	SELECT
	h.urn
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
	inner join collection c on
			c.id = h.collection_id
	inner join book b on
			b.collection_id = h.collection_id
			and b.id = h.book_id
	INNER JOIN chapter c2 on
			c2.collection_id = h.collection_id
		and 
			c2.book_id = h.book_id
		and
			c2.id = h.chapter_id
	ORDER BY h.urn
)
	;