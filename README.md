# 🪐 Horizon — Exoplanet Searcher

A CBSE Class 12 Computer Science project using **Python + MySQL + mysql-connector-python + Flask + Jinja2**.

## Project overview

Horizon converts a cleaned snapshot of confirmed exoplanet data from the NASA Exoplanet Archive into a local MySQL database and presents it through a lightweight Flask website.

## Features

- Search by planet name
- Filter by discovery method
- Filter by discovery year range
- Sort results
- Summary statistics
- CREATE / READ / UPDATE / DELETE
- Parameterized SQL queries
- Safe dynamic sorting using an allow-list
- Input validation
- `try-except` database error handling
- Application logging

## Current project data

The project is designed for the cleaned file:

```text
data/exoplanets.csv
```

The current working dataset contains approximately 6,354 imported records.

The original NASA snapshot can be retained separately as:

```text
data/nasa_raw.csv
```

## Folder structure

```text
Horizon_Exoplanet_Searcher/
│
├── data/
│   ├── nasa_raw.csv
│   └── exoplanets.csv
│
├── docs/
│   ├── project_report.md
│   └── viva_notes.md
│
├── logs/
│   └── app.log
│
├── sql/
│   └── schema.sql
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
│
├── tests/
│   └── test_cases.md
│
├── app.py
├── clean_csv.py
├── config.py
├── db.py
├── exoplanets.py
├── import_csv.py
├── logger.py
├── requirements.txt
└── README.md
```

## Setup

### 1. Create the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL password

For this project, `config.py` reads database settings from environment variables.

In the VS Code terminal:

```bash
export HORIZON_DB_USER="root"
export HORIZON_DB_PASSWORD="YOUR_MYSQL_PASSWORD"
export HORIZON_DB_NAME="exoplanet_db"
export HORIZON_DB_HOST="localhost"
export HORIZON_DB_PORT="3306"
```

Do not put your real password into Git or public documentation.

These environment variables apply to the current terminal session.

## MySQL setup

Start MySQL:

```bash
brew services start mysql
```

Create the database/table:

```bash
mysql -u root -p < sql/schema.sql
```

Check:

```bash
mysql -u root -p
```

```sql
USE exoplanet_db;
DESCRIBE exoplanets;
SELECT COUNT(*) FROM exoplanets;
```

## CSV

The project keeps the raw NASA snapshot separately:

```text
data/nasa_raw.csv
```

Clean it:

```bash
python clean_csv.py
```

This generates:

```text
data/exoplanets.csv
```

Import it:

```bash
python import_csv.py
```

Then check:

```sql
SELECT COUNT(*) FROM exoplanets;
```

If all records are already imported, a later import may report duplicate entries. Do not repeatedly run the importer unless you intentionally rebuild/clear the table.

## Run Horizon

From the project root:

```bash
source .venv/bin/activate
python app.py
```

Open:

```text
http://127.0.0.1:5001
```

Port 5001 is used because macOS may already occupy port 5000.

## Testing

Syntax check:

```bash
python -m py_compile app.py
python -m py_compile exoplanets.py
python -m py_compile db.py
python -m py_compile logger.py
```

Run the application:

```bash
python app.py
```

Then test:

- Search
- Discovery-method filtering
- Discovery-year filtering
- Sorting
- Add
- Update
- Delete
- Statistics
- Invalid input
- Logging

Test cases are documented in:

```text
tests/test_cases.md
```

## Database safety

User-entered values use parameterized SQL:

```python
cursor.execute(query, values)
```

Dynamic sort columns use a predefined allow-list.

Do not replace parameterized queries with raw string concatenation.

## Logging

Log file:

```text
logs/app.log
```

View it with:

```bash
cat logs/app.log
```

## Backup

Create a database backup:

```bash
mysqldump -u root -p exoplanet_db > exoplanet_backup.sql
```

## Limitations

- Static NASA data snapshot
- Local deployment
- Maximum 100 displayed results
- No user authentication
- No advanced visualisations

## Future scope

- Pagination
- Charts and visualisations
- Automatic data updates
- Authentication
- Individual planet detail pages
- Public deployment

## Academic coverage

This project demonstrates:

```text
Python
MySQL
mysql-connector-python
Relational Database
SQL Queries
CRUD Operations
Parameterized Queries
Safe Dynamic SQL
Modular Python
try-except Error Handling
Logging
Flask
Jinja2
HTML/CSS
```
