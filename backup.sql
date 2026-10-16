-- MySQL dump 10.13  Distrib 26.7.0, for macos26.6 (arm64)
USE defaultdb;
--
-- Host: localhost    Database: exoplanet_db
-- ------------------------------------------------------
-- Server version	26.7.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
-- SET @@SESSION.SQL_LOG_BIN= 0;

-- --
-- -- GTID state at the beginning of the backup 
-- --

-- SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '27b74356-a530-11f1-841d-2a42cb339f86:1-17';

--
-- Table structure for table `exoplanets`
--

DROP TABLE IF EXISTS `exoplanets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exoplanets` (
  `planet_id` int NOT NULL AUTO_INCREMENT,
  `planet_name` varchar(100) NOT NULL,
  `host_star` varchar(100) DEFAULT NULL,
  `discovery_year` int DEFAULT NULL,
  `discovery_method` varchar(100) DEFAULT NULL,
  `orbital_period_days` decimal(15,6) DEFAULT NULL,
  `radius_earth` decimal(12,6) DEFAULT NULL,
  `mass_earth` decimal(15,6) DEFAULT NULL,
  `distance_pc` decimal(12,6) DEFAULT NULL,
  `equilibrium_temp_k` decimal(12,3) DEFAULT NULL,
  PRIMARY KEY (`planet_id`),
  UNIQUE KEY `planet_name` (`planet_name`)
) ENGINE=InnoDB AUTO_INCREMENT=19070 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exoplanets`
--

LOCK TABLES `exoplanets` WRITE;
/*!40000 ALTER TABLE `exoplanets` DISABLE KEYS */;
/*!40000 ALTER TABLE `exoplanets` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-16  5:59:04
