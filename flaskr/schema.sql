DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  lastname TEXT NOT NULL,
  firstname TEXT NOT NULL,

    email TEXT NOT NULL,
    profession INTEGER ,
    rang INTEGER,
    specialite INTEGER ,
    institut INTEGER ,
    specialitePrepa INTEGER ,
    bac INTEGER ,
    mentionBac INTEGER ,
    connaissance INTEGER ,
    emplacement  INTEGER ,
    influenceFamille BOOLEAN ,
    proche INTEGER ,
    facteur INTEGER ,
    jeuxColl INTEGER,
    sport INTEGER,
    arts INTEGER,
    voyage INTEGER,
    vieassociative INTEGER,
    technologie INTEGER,
    pc INTEGER,
    culture INTEGER,
    vision INTEGER ,
    residence INTEGER ,
    conditon INTEGER


);


create TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
