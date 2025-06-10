-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: logsdb
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Position to start replication or point-in-time recovery from
--

-- CHANGE MASTER TO MASTER_LOG_FILE='KKRLP-3-bin.000027', MASTER_LOG_POS=157;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
REPLACE  IGNORE INTO `admins` (`id`, `name`, `email`) VALUES (1,'geert2.0','geert2@gmail.com'),(7,'geert','geert@gmail.com'),(36,'Alfred','alfredmiddel@outlook.com'),(37,'Adriaan','adriaan@gmail.com'),(38,'Simon','simwolsman@gmail.com'),(39,'Aard','adminkol@gmail.com'),(40,'Harm','smitharm1970@outlook.com');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_admin_insert` AFTER INSERT ON `admins` FOR EACH ROW BEGIN
    INSERT INTO user_log (user_id, action_type, new_name, new_email, changed_by)
    VALUES (NEW.id, 'INSERT', NEW.name, NEW.email, current_user());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_admin_update` AFTER UPDATE ON `admins` FOR EACH ROW BEGIN
    INSERT INTO user_log (
        user_id, action_type,
        old_name, old_email,
        new_name, new_email,
        changed_by
    )
    VALUES (
        OLD.id, 'UPDATE',
        OLD.name, OLD.email,
        NEW.name, NEW.email,
        CURRENT_USER()
    );
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_admin_delete` AFTER DELETE ON `admins` FOR EACH ROW BEGIN
    INSERT INTO user_log (
        user_id, action_type, 
        old_name, old_email, 
        changed_by
    )
    VALUES (
        OLD.id, 'DELETE', 
        OLD.name, OLD.email, 
        CURRENT_USER()
    );
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `user_log`
--

DROP TABLE IF EXISTS `user_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_log` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `action_type` varchar(100) DEFAULT NULL,
  `old_name` varchar(100) DEFAULT NULL,
  `old_email` varchar(100) DEFAULT NULL,
  `new_name` varchar(100) DEFAULT NULL,
  `new_email` varchar(200) DEFAULT NULL,
  `action_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `changed_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_log`
--

LOCK TABLES `user_log` WRITE;
/*!40000 ALTER TABLE `user_log` DISABLE KEYS */;
REPLACE  IGNORE INTO `user_log` (`log_id`, `user_id`, `action_type`, `old_name`, `old_email`, `new_name`, `new_email`, `action_time`, `changed_by`) VALUES (1,11,'INSERT',NULL,NULL,'geert','geert@gmail.com','2025-06-05 07:04:44','root@localhost'),(2,1,'UPDATE','geert','willem','geertje','geert05@gmail.com','2025-06-05 07:05:25','root@localhost'),(3,12,'INSERT',NULL,NULL,'willem','willem@gmail.com','2025-06-05 07:46:31','root@localhost'),(4,5,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-05 07:51:38','root@localhost'),(5,7,'INSERT',NULL,NULL,'geert','geert@gmail.com','2025-06-05 07:58:24','root@localhost'),(6,8,'INSERT',NULL,NULL,'wilders','wilderd@gmail.com','2025-06-06 08:03:51','root@localhost'),(7,8,'UPDATE','wilders','wilderd@gmail.com','wilders','wilders@gmail.com','2025-06-06 08:05:47','root@localhost'),(8,8,'DELETE','wilders','wilders@gmail.com',NULL,NULL,'2025-06-06 08:06:25','root@localhost'),(9,13,'INSERT',NULL,NULL,'wilders','wilders@gmail.com','2025-06-06 08:07:22','root@localhost'),(10,13,'UPDATE','wilders','wilders@gmail.com','willie','willie@gmail.com','2025-06-06 08:08:02','root@localhost'),(11,13,'DELETE','willie','willie@gmail.com',NULL,NULL,'2025-06-06 08:08:32','root@localhost'),(12,14,'INSERT',NULL,NULL,'erik','erik@gmail.com','2025-06-06 09:01:12','root@localhost'),(13,14,'UPDATE','erik','erik@gmail.com','erik','erikuters@gmail.com','2025-06-06 09:01:35','root@localhost'),(14,9,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:03:57','root@localhost'),(15,10,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:03:59','root@localhost'),(16,11,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:03:59','root@localhost'),(17,12,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:01','root@localhost'),(18,13,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:01','root@localhost'),(19,14,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:01','root@localhost'),(20,15,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:01','root@localhost'),(21,16,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:01','root@localhost'),(22,17,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:01','root@localhost'),(23,18,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:02','root@localhost'),(24,19,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:02','root@localhost'),(25,20,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:02','root@localhost'),(26,21,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:02','root@localhost'),(27,22,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:02','root@localhost'),(28,23,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:02','root@localhost'),(29,24,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:03','root@localhost'),(30,25,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:03','root@localhost'),(31,26,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:03','root@localhost'),(32,27,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:03','root@localhost'),(33,28,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:03','root@localhost'),(34,29,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:03','root@localhost'),(35,30,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:04','root@localhost'),(36,31,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:04:04','root@localhost'),(37,5,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(38,9,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(39,10,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(40,11,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(41,12,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(42,13,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(43,14,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(44,15,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(45,16,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(46,17,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(47,18,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(48,19,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(49,20,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(50,21,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(51,22,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(52,23,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(53,24,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(54,25,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(55,26,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(56,27,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(57,28,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(58,29,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(59,30,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(60,31,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:07:43','root@localhost'),(61,32,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:08:08','root@localhost'),(62,33,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:08:08','root@localhost'),(63,34,'INSERT',NULL,NULL,'Pim','karel@gmail.com','2025-06-06 09:08:09','root@localhost'),(64,32,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:08:47','root@localhost'),(65,33,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:08:47','root@localhost'),(66,34,'DELETE','Pim','karel@gmail.com',NULL,NULL,'2025-06-06 09:08:47','root@localhost'),(67,35,'INSERT',NULL,NULL,'willem','willem@gmail.com','2025-06-06 09:11:31','root@localhost'),(68,35,'DELETE','willem','willem@gmail.com',NULL,NULL,'2025-06-06 09:12:13','root@localhost'),(69,36,'INSERT',NULL,NULL,'Alfred','alfredmiddel@outlook.com','2025-06-06 09:24:21','root@localhost'),(70,37,'INSERT',NULL,NULL,'Adriaan','adriaan@gmail.com','2025-06-06 09:24:47','root@localhost'),(71,38,'INSERT',NULL,NULL,'Simon','simwolsman@gmail.com','2025-06-06 09:25:10','root@localhost'),(72,39,'INSERT',NULL,NULL,'Aard','adminkol@gmail.com','2025-06-06 09:25:48','root@localhost'),(73,15,'INSERT',NULL,NULL,'marc','marc@outlook.com','2025-06-06 09:26:13','root@localhost'),(74,16,'INSERT',NULL,NULL,'merijn','ruitermerijn06@gmail.com','2025-06-06 09:26:45','root@localhost'),(75,40,'INSERT',NULL,NULL,'Harm','smitharm1970@outlook.com','2025-06-06 09:27:46','root@localhost'),(76,17,'INSERT',NULL,NULL,'Sam','fsam@example.com','2025-06-10 07:00:48','root@localhost');
/*!40000 ALTER TABLE `user_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
REPLACE  IGNORE INTO `users` (`id`, `name`, `email`) VALUES (1,'geertje','geert05@gmail.com'),(2,'willem','geert@wneknkn.com'),(5,'Test','test@example.nl'),(8,'Wassim','wassim@gmail.com'),(11,'geert','geert@gmail.com'),(12,'willem','willem@gmail.com'),(14,'erik','erikuters@gmail.com'),(15,'marc','marc@outlook.com'),(16,'merijn','ruitermerijn06@gmail.com'),(17,'Sam','fsam@example.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_user_insert` AFTER INSERT ON `users` FOR EACH ROW BEGIN
    INSERT INTO user_log (user_id, action_type, new_name, new_email, changed_by)
    VALUES (NEW.id, 'INSERT', NEW.name, NEW.email, current_user());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_user_update` AFTER UPDATE ON `users` FOR EACH ROW BEGIN
    INSERT INTO user_log (
        user_id, action_type,
        old_name, old_email,
        new_name, new_email,
        changed_by
    )
    VALUES (
        OLD.id, 'UPDATE',
        OLD.name, OLD.email,
        NEW.name, NEW.email,
        CURRENT_USER()
    );
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `after_user_delete` AFTER DELETE ON `users` FOR EACH ROW BEGIN
    INSERT INTO user_log (user_id, action_type, old_name, old_email, changed_by)
    VALUES (OLD.id, 'DELETE', OLD.name, OLD.email, current_user());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-10  9:08:01
