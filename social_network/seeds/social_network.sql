
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR (50),
    email_address VARCHAR (255)
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title VARCHAR (255),
    post_contents text,
    post_views int,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (username, email_address) VALUES ('amy_brown', 'amys-fake-email@hotmail.com');
INSERT INTO users (username, email_address) VALUES ('best_username_ever', 'what-a-great-email@email.com');
INSERT INTO users (username, email_address) VALUES ('dr-evil', 'evil@evilcity.com');

INSERT INTO posts (user_id, post_title, post_contents, post_views) VALUES (1, 'What I did on my Holidays', 'It was great, I went to the beach', 10);
INSERT INTO posts (user_id, post_title, post_contents, post_views) VALUES (2, 'I am the best poster ever', 'Why yes read all about my excellent time in this post of brilliance', 1);
INSERT INTO posts (user_id, post_title, post_contents, post_views) VALUES (1, 'What I did when I got back from my Holidays', 'actually not a lot really, just went to the shops because we were out of milk :(', 300);
INSERT INTO posts (user_id, post_title, post_contents, post_views) VALUES (3, 'Mwahahhahahahah', 'noone can know about my evil plot, here is my 10 step plan of how I will rob all the banks in the WORLD!!!! ', 666);



