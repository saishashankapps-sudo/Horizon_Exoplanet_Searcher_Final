# Horizon — Exoplanet Searcher

## Abstract

Horizon is a CBSE Class 12 Computer Science project that transforms a cleaned snapshot of confirmed exoplanet data from the NASA Exoplanet Archive into a searchable local MySQL database and a Flask-based web application.

## Problem Statement

Large scientific datasets are difficult for non-specialist users to explore directly. Horizon provides a simple webpage for searching, filtering, sorting and exploring useful exoplanet information.

## Objectives

1. Obtain confirmed exoplanet data from NASA.
2. Clean the dataset to keep useful fields.
3. Store the data in a relational MySQL database.
4. Connect Python to MySQL using `mysql-connector-python`.
5. Build a Flask web interface using Jinja2.
6. Implement search, filtering and sorting.
7. Demonstrate CRUD operations.
8. Use parameterized SQL queries.
9. Handle errors and maintain logs.
10. Document and test the system.

## Technologies

- Python 3.x
- MySQL
- mysql-connector-python
- Flask
- Jinja2
- HTML5
- CSS3
- VS Code
- MySQL CLI
- NASA Exoplanet Archive

## Database

Database: `exoplanet_db`

Table: `exoplanets`

The table contains:

- `planet_id`
- `planet_name`
- `host_star`
- `discovery_year`
- `discovery_method`
- `orbital_period_days`
- `radius_earth`
- `mass_earth`
- `distance_pc`
- `equilibrium_temp_k`

## Features

- Planet-name search
- Discovery-method filtering
- Discovery-year filtering
- Sorting
- Summary statistics
- Add
- Update
- Delete
- Error handling
- Logging
- Parameterized SQL

## Limitations

- Static NASA dataset snapshot
- Local deployment
- Maximum 100 displayed results
- No authentication
- No advanced visualisations

## Conclusion

Horizon demonstrates how Python, SQL, MySQL and Flask can be integrated into one practical application. It provides a simple interface for exploring a structured scientific dataset while demonstrating database connectivity, CRUD operations, modular programming, parameterized SQL, exception handling and logging.
