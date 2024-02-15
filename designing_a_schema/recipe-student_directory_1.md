## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

student, student names, student cohorts
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| student               | student_name, cohort        |

Name of the table (always plural): `students`

Column names: `name`, `cohort`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

```
# EXAMPLE:

id: SERIAL
student_name: text
cohort: text
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: students_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort text,
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 student_directory_1 < /Users/amybrown/Documents/Modern_Software_Engineering_Foundations-Learning/databases/database_practice/designing_a_schema/students_table.sql
```