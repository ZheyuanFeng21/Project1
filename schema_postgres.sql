CREATE TABLE word (
 word_id int NOT NULL,
 word varchar(64) NOT NULL,
 CONSTRAINT word_pk PRIMARY KEY (word_id)
);

CREATE TABLE word_count (
 word_id int NOT NULL,
 time timestamp NOT NULL,
 countnum int NOT NULL,
 PRIMARY KEY (word_id, time),
 FOREIGN KEY (word_id) REFERENCES word(word_id)
);
