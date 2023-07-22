CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    passwd_hash TEXT NOT NULL,
    created_ts INTEGER NOT NULL
);

CREATE TABLE questions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    content_md TEXT NOT NULL,
    content_html TEXT NOT NULL,
    subject_id INTEGER,
    grade_id INTEGER,
    created_ts INTEGER NOT NULL,
    img_path TEXT
);

CREATE TABLE replies (
    id INTEGER PRIMARY KEY,
    question_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    content_md TEXT NOT NULL,
    content_html TEXT NOT NULL,
    created_ts INTEGER NOT NULL
);
