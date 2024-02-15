-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS ecipes_id_seq;
CREATE TABLE recipes (
id SERIAL PRIMARY KEY,
recipe_name VARCHAR (255),
cooking_time INT,
rating INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Puttanesca Pasta Sauce', 25, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Lentil Lasagna', 60, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Leek and Potato Soup', 20, 3);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Aubergine Parmagiana', 90, 5);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Spinach and Sweet Potato Enchilada Bake', 60, 2);