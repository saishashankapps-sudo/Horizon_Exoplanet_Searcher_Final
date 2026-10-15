import os


DB_CONFIG = {
    "host": os.getenv("HORIZON_DB_HOST", "localhost"),
    "port": int(os.getenv("HORIZON_DB_PORT", "3306")),
    "user": os.getenv("HORIZON_DB_USER", "root"),
    "password": os.getenv("HORIZON_DB_PASSWORD", ""),
    "database": os.getenv("HORIZON_DB_NAME", "exoplanet_db"),
}
