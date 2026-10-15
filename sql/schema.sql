CREATE DATABASE IF NOT EXISTS exoplanet_db;

USE exoplanet_db;

CREATE TABLE IF NOT EXISTS exoplanets (
    planet_id INT PRIMARY KEY AUTO_INCREMENT,
    planet_name VARCHAR(100) NOT NULL UNIQUE,
    host_star VARCHAR(100),
    discovery_year INT,
    discovery_method VARCHAR(100),
    orbital_period_days DECIMAL(15,6),
    radius_earth DECIMAL(12,6),
    mass_earth DECIMAL(15,6),
    distance_pc DECIMAL(12,6),
    equilibrium_temp_k DECIMAL(12,3)
);
