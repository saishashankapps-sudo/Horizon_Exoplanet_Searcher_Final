from mysql.connector import Error

from db import create_connection
from logger import log_error


SELECT_FIELDS = """
    planet_id,
    planet_name,
    host_star,
    discovery_year,
    discovery_method,
    orbital_period_days,
    radius_earth,
    mass_earth,
    distance_pc,
    equilibrium_temp_k
"""


def get_all_exoplanets():
    """Return up to 100 exoplanets ordered by name."""
    connection = create_connection()
    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = f"""
            SELECT {SELECT_FIELDS}
            FROM exoplanets
            ORDER BY planet_name
            LIMIT 100
        """

        cursor.execute(query)
        return cursor.fetchall()

    except Error as error:
        log_error(f"get_all_exoplanets error: {error}")
        print(f"Error getting exoplanets: {error}")
        return []

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def search_exoplanets(
    name="",
    method="",
    start_year=None,
    end_year=None,
    sort_by="planet_name",
):
    """Search/filter exoplanets using parameterized values."""
    connection = create_connection()
    if connection is None:
        return []

    cursor = None

    allowed_sort_columns = {
        "planet_name": "planet_name",
        "discovery_year": "discovery_year",
        "distance_pc": "distance_pc",
        "radius_earth": "radius_earth",
        "mass_earth": "mass_earth",
        "orbital_period_days": "orbital_period_days",
    }

    sort_column = allowed_sort_columns.get(sort_by, "planet_name")

    query = f"""
        SELECT {SELECT_FIELDS}
        FROM exoplanets
        WHERE 1 = 1
    """

    parameters = []

    if name:
        query += " AND planet_name LIKE %s"
        parameters.append(f"%{name}%")

    if method:
        query += " AND discovery_method = %s"
        parameters.append(method)

    if start_year is not None:
        query += " AND discovery_year >= %s"
        parameters.append(start_year)

    if end_year is not None:
        query += " AND discovery_year <= %s"
        parameters.append(end_year)

    query += f" ORDER BY {sort_column}"
    query += " LIMIT 100"

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, tuple(parameters))
        return cursor.fetchall()

    except Error as error:
        log_error(f"search_exoplanets error: {error}")
        print(f"Error searching exoplanets: {error}")
        return []

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def get_discovery_methods():
    """Return all distinct discovery methods."""
    connection = create_connection()
    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT discovery_method
            FROM exoplanets
            WHERE discovery_method IS NOT NULL
              AND discovery_method <> ''
            ORDER BY discovery_method
        """)

        return [row[0] for row in cursor.fetchall()]

    except Error as error:
        log_error(f"get_discovery_methods error: {error}")
        return []

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def get_exoplanet_by_id(planet_id):
    """Return one exoplanet by ID."""
    connection = create_connection()
    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = f"""
            SELECT {SELECT_FIELDS}
            FROM exoplanets
            WHERE planet_id = %s
        """

        cursor.execute(query, (planet_id,))
        return cursor.fetchone()

    except Error as error:
        log_error(f"get_exoplanet_by_id error: {error}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def add_exoplanet(
    planet_name,
    host_star,
    discovery_year,
    discovery_method,
    orbital_period_days,
    radius_earth,
    mass_earth,
    distance_pc,
    equilibrium_temp_k,
):
    """Insert one exoplanet record."""
    connection = create_connection()
    if connection is None:
        return False

    cursor = None

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

    values = (
        planet_name,
        host_star,
        discovery_year,
        discovery_method,
        orbital_period_days,
        radius_earth,
        mass_earth,
        distance_pc,
        equilibrium_temp_k,
    )

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        return True

    except Error as error:
        log_error(f"add_exoplanet error: {error}")
        connection.rollback()
        return False

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def update_exoplanet(
    planet_id,
    planet_name,
    host_star,
    discovery_year,
    discovery_method,
    orbital_period_days,
    radius_earth,
    mass_earth,
    distance_pc,
    equilibrium_temp_k,
):
    """Update an existing exoplanet record."""
    connection = create_connection()
    if connection is None:
        return False

    cursor = None

    query = """
        UPDATE exoplanets
        SET
            planet_name = %s,
            host_star = %s,
            discovery_year = %s,
            discovery_method = %s,
            orbital_period_days = %s,
            radius_earth = %s,
            mass_earth = %s,
            distance_pc = %s,
            equilibrium_temp_k = %s
        WHERE planet_id = %s
    """

    values = (
        planet_name,
        host_star,
        discovery_year,
        discovery_method,
        orbital_period_days,
        radius_earth,
        mass_earth,
        distance_pc,
        equilibrium_temp_k,
        planet_id,
    )

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        return cursor.rowcount > 0

    except Error as error:
        log_error(f"update_exoplanet error: {error}")
        connection.rollback()
        return False

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def delete_exoplanet(planet_id):
    """Delete an exoplanet record by ID."""
    connection = create_connection()
    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM exoplanets
            WHERE planet_id = %s
        """

        cursor.execute(query, (planet_id,))
        connection.commit()
        return cursor.rowcount > 0

    except Error as error:
        log_error(f"delete_exoplanet error: {error}")
        connection.rollback()
        return False

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def get_statistics():
    """Return dashboard summary statistics."""
    connection = create_connection()
    if connection is None:
        return {}

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                COUNT(*) AS total_planets,
                MIN(discovery_year) AS earliest_discovery,
                MAX(discovery_year) AS latest_discovery,
                AVG(distance_pc) AS average_distance
            FROM exoplanets
        """)

        return cursor.fetchone() or {}

    except Error as error:
        log_error(f"get_statistics error: {error}")
        return {}

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def get_most_common_method():
    """Return the most common discovery method."""
    connection = create_connection()
    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                discovery_method,
                COUNT(*) AS total
            FROM exoplanets
            WHERE discovery_method IS NOT NULL
              AND discovery_method <> ''
            GROUP BY discovery_method
            ORDER BY total DESC
            LIMIT 1
        """)

        return cursor.fetchone()

    except Error as error:
        log_error(f"get_most_common_method error: {error}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()
