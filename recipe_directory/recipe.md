## 1. Extract nouns from the user stories or specification

```
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).
```

```
Nouns:

food, recipes, name, cooking_time (in mins), rating (1-5)
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                 |
| --------------------- | -------------------------- |
| recipe                | name, cooking_time, rating |

Name of the table (always plural): `recipes`

Column names: `name`, `cooking_time`, `rating`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).


Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
recipe_name: VARCHAR (255)
cooking_time: INT
rating: ENUM (1,2,3,4,5)
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.
CREATE TYPE one_to_five_scale AS ENUM (1,2,3,4,5);
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name VARCHAR (255),
  cooking_time INT,
  rating INT
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```