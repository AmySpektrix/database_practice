# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in their comment.
```

```
Nouns:

posts, post_title, post_content, comments, comment_content, comment_author
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                                   |
| --------------------- | ---------------------------------------------|
| posts                 | id, post_content, post_title                 |
| comments              | id, comment_content, comment_author, post_id |

1. Name of the first table (always plural): `posts` 

    Column names: `id`, `post_content`, `post_title`

2. Name of the second table (always plural): `comments` 

    Column names: `id`, `comment_content`, `comment_author`, `post_id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```

Table: posts
id: SERIAL
post_title: text
post_comment: text

Table: comments
id: SERIAL
comment_content: text
comment_author: text
post_id: int
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one post have many comments? YES
2. Can one comment have many posts? NO

-> Therefore,
-> An post HAS MANY comments
-> A comment BELONGS TO a post

-> Therefore, the foreign key is on the comments table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  post_name VARCHAR(255),
  post_content TEXT
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  comment_author VARCHAR(255),
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```