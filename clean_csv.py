import csv


INPUT_FILE = "data/nasa_raw.csv"
OUTPUT_FILE = "data/exoplanets.csv"


def clean_value(value):
    """Convert blank values to None; strip surrounding whitespace."""
    if value is None:
        return None

    value = value.strip()
    return value if value else None


def find_header(input_file):
    """Find the real CSV header after NASA metadata lines."""
    while True:
        line = input_file.readline()

        if not line:
            raise ValueError("Could not find the CSV header.")

        if line.startswith("pl_name"):
            return line.strip().split(",")


def clean_csv():
    """Create a smaller project CSV from the NASA raw CSV."""
    with open(
        INPUT_FILE,
        "r",
        newline="",
        encoding="utf-8",
    ) as input_file:

        header = find_header(input_file)

        reader = csv.DictReader(
            input_file,
            fieldnames=header,
        )

        fieldnames = [
            "planet_name",
            "host_star",
            "discovery_year",
            "discovery_method",
            "orbital_period_days",
            "radius_earth",
            "mass_earth",
            "distance_pc",
            "equilibrium_temp_k",
        ]

        seen_planets = set()

        with open(
            OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8",
        ) as output_file:

            writer = csv.DictWriter(
                output_file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for row in reader:
                planet_name = clean_value(row.get("pl_name"))

                if not planet_name:
                    continue

                if planet_name in seen_planets:
                    continue

                seen_planets.add(planet_name)

                writer.writerow({
                    "planet_name": planet_name,
                    "host_star": clean_value(row.get("hostname")),
                    "discovery_year": clean_value(row.get("disc_year")),
                    "discovery_method": clean_value(
                        row.get("discoverymethod")
                    ),
                    "orbital_period_days": clean_value(
                        row.get("pl_orbper")
                    ),
                    "radius_earth": clean_value(
                        row.get("pl_rade")
                    ),
                    "mass_earth": clean_value(
                        row.get("pl_bmasse")
                    ),
                    "distance_pc": clean_value(
                        row.get("sy_dist")
                    ),
                    "equilibrium_temp_k": clean_value(
                        row.get("pl_eqt")
                    ),
                })


if __name__ == "__main__":
    clean_csv()
    print("CSV cleaning complete.")
