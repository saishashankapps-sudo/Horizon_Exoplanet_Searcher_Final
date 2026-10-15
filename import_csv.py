import csv

from mysql.connector import Error

from db import create_connection
from logger import log_error, log_info


CSV_FILE = "data/exoplanets.csv"


def convert_value(value):
    """Convert blank CSV values into None for MySQL NULL."""
    value = value.strip()
    return value if value else None


def import_csv():
    """Import the cleaned CSV into MySQL."""
    connection = create_connection()

    if connection is None:
        print("Could not connect to MySQL.")
        return

    cursor = None
    inserted = 0
    skipped = 0

    query = """
        INSERT INTO exoplanets (
            planet_name,
            host_star,
            discovery_year,
            discovery_method,
            orbital_period_days,
            radius_earth,
            mass_earth,
            distance_pc,
            equilibrium_temp_k
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cursor = connection.cursor()

        with open(
            CSV_FILE,
            "r",
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                planet_name = convert_value(row["planet_name"])

                if planet_name is None:
                    skipped += 1
                    continue

                values = (
                    planet_name,
                    convert_value(row["host_star"]),
                    convert_value(row["discovery_year"]),
                    convert_value(row["discovery_method"]),
                    convert_value(row["orbital_period_days"]),
                    convert_value(row["radius_earth"]),
                    convert_value(row["mass_earth"]),
                    convert_value(row["distance_pc"]),
                    convert_value(row["equilibrium_temp_k"]),
                )

                try:
                    cursor.execute(query, values)
                    inserted += 1

                except Error as error:
                    # Duplicate names are skipped safely.
                    skipped += 1
                    print(f"Skipping {planet_name}: {error}")

        connection.commit()

        log_info(
            f"CSV import complete. inserted={inserted}, skipped={skipped}"
        )

        print()
        print("CSV import complete.")
        print(f"Inserted records: {inserted}")
        print(f"Skipped records: {skipped}")

    except FileNotFoundError:
        log_error(f"CSV file not found: {CSV_FILE}")
        print(f"CSV file not found: {CSV_FILE}")

    except Error as error:
        connection.rollback()
        log_error(f"CSV import database error: {error}")
        print(f"Database error: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


if __name__ == "__main__":
    import_csv()
