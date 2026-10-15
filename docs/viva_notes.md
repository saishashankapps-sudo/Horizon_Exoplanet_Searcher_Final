# Horizon — Viva Preparation Notes

## Project

**What is Horizon?**

Horizon is a Flask-based exoplanet search application that stores a cleaned NASA exoplanet dataset in a MySQL database and allows users to search, filter, sort and manage records.

## Data

**Which dataset is used?**

A snapshot of the NASA Exoplanet Archive PSCompPars data is used.

**Why clean the CSV?**

The NASA raw dataset contains many fields. The project keeps only the fields needed for meaningful display, search, filtering and database operations.

## Database

**What is the primary key?**

`planet_id` is the primary key. It uniquely identifies each row.

**Why is `planet_name` UNIQUE?**

It prevents duplicate planet names from being inserted into the table.

**What is a relational database?**

A relational database stores related data in tables consisting of rows and columns.

## Python-MySQL Integration

**What does `mysql-connector-python` do?**

It allows Python to connect to MySQL, execute SQL statements and retrieve results.

**What is a cursor?**

A cursor is used to execute SQL statements and fetch query results.

**Why is `commit()` used?**

`commit()` permanently applies successful INSERT, UPDATE or DELETE operations.

**Why is `rollback()` used?**

`rollback()` cancels an unsuccessful transaction so that a failed change is not partially applied.

## CRUD

- CREATE — Add a new exoplanet
- READ — View/search exoplanets
- UPDATE — Edit an existing record
- DELETE — Remove a record

## SQL Safety

**What is SQL injection?**

SQL injection is an attack where untrusted input is made to alter the meaning of an SQL statement.

**How is it prevented?**

User-supplied values are passed as parameters using `%s` placeholders and `cursor.execute(query, values)`.

**How is dynamic sorting handled safely?**

Sort choices are selected from a predefined allow-list of permitted database column names.

## Flask

**What does Flask do?**

Flask handles HTTP requests, routes URLs to Python functions, and renders Jinja2 HTML templates.

**Why is Jinja2 used?**

Jinja2 allows database results and other Python values to be inserted into HTML templates dynamically.

## Error Handling

The project uses `try-except-finally` blocks for database operations and input conversion.

## Logging

Application activity and database errors are recorded in:

`logs/app.log`

## Limitations

The application uses a static data snapshot, is designed for local deployment, displays a maximum of 100 results at once, and does not include authentication or advanced visualisations.

## Future Scope

Possible improvements include pagination, charts, automatic data updates, authentication and public deployment.
