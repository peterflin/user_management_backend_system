-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: user_management
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UNIQUE` (`name`),
  KEY `INDEX` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'peterflin','peterflin123@gmail.com','$2b$12$kw76jem8Ri8bzygOoB3/Ce2xva5OCeM7Gw1XywRwvKOj8aFIENTee'),(4,'peterflin4','peterflin@gmail.com','$2b$12$.PGfwOJJ2lPmZwGhI12iQ.yGIHwPTE6.aIU6cggEr4HNXDgUCKyx2'),(5,'peterflin5','peterflin4@gmail.com','$2b$12$/nzAWdOBXAddnpk9aooDYO2gaBcYuXNRADSPkn58SFPvVclxrtX.a'),(6,'peterflin6','peterflin4@gmail.com','$2b$12$CQi2dAUTJMkiQfqjtnUFH.x/tRf5AOSCrYkTyHcn2CK.ybZmctrIq'),(7,'peterflin123','test@gmail.com','$2b$12$jZvliRh9pYsIkMQ4VhATROYOWj/VRl8Qukwa9.2NmlHeQmLrE2.Iy'),(8,'peterflin145677','test@gmail.com','$2b$12$Cl5lTF3.H1KCu.ZwaPakSOMtSoRtn6F5U/5C3ICDnCje6hbr7ZM1y'),(9,'peterflin7223','peterflin4@gmail.com','$2b$12$29TeC06rT72qaREFv291g.u4TpFTvqtvmFQGnTVRe8sS/czPp.jFW'),(10,'peterflin1457','peterflin4@gmail.com','$2b$12$0T6.EvH89vrGeZjvn3nKmuJP7nAb3M698Y58Zjn4/RypnOP7ZpMcG'),(11,'peterflin5212','peterflin4@gmail.com','$2b$12$jiU/Ee9kOjXLdNya2rSFgO9v0Qwcu0V2aVabJMAXNkxWOykp74Z5u'),(12,'peterflin1877','peterflin4@gmail.com','$2b$12$cmCu1qskAfvR7VH7gc8LtOCm2g0uvrWAuLtTA9B4DgT76u8LyZldu'),(13,'peterflin2913','peterflin4@gmail.com','$2b$12$tAgEBlTxNjQd9tSIdCi43eqAt8Q18TvcOT3ko49p1SDg/t8vLyRUG'),(14,'peterflin5703','peterflin4@gmail.com','$2b$12$nlCbsDrQ1.qBGdTKQ1mWfu197a0bulptTG69bDlHkbhGTAtpZG8F.'),(15,'peterflin3024','peterflin4@gmail.com','$2b$12$uw1X9dTAX8MD5P885GO.JOjmBCd7WSasQ9CKBL6lHJElHZjiKGSI2'),(16,'peterflin3166','peterflin4@gmail.com','$2b$12$EnD5VuloIgQQ2929H.i5y.9EQSxJZi30QjZEd///49rnh2Nelvi22'),(17,'peterflin4521','peterflin4@gmail.com','$2b$12$UTRfouvpxHY3.rLykY9Ej.KkcWsvdadR4g08IANSO8Rrn1YC0oCPu'),(18,'peterflin6799','peterflin4@gmail.com','$2b$12$r93pfN3RDrUA2ilOEOTaNOKHDhAKi15CVNhIQhFPcJ2o9b39Hw2sS'),(19,'peterflin9860','peterflin4@gmail.com','$2b$12$Jfhx63wkZapQzTszzge0NuCp.8Gr1Wkm0aePQmgCTQ6R6RQpO.F1e'),(20,'peterflin4407','peterflin4@gmail.com','$2b$12$ABnShCkczxJWEmUMvZyL.emYELh7a8NG9TSNiL4XdlpIWqbA1K2H2'),(21,'peterflin8762','peterflin4@gmail.com','$2b$12$0gCfWlH8UjtyhG30x7/BRuQTWl8bCPpMaDC.325FCP25YRWHzS4Y2'),(22,'peterflin8442','peterflin4@gmail.com','$2b$12$CkiAaPmqxl4TpU.QTf1x0OOKf4mWb/IcQyDdxGEnJ38By4Exedm8a'),(23,'peterflin3146','peterflin4@gmail.com','$2b$12$uzLwFB6UUOsygxXSVs/f1OAPdd/7.v2xRQpzNsOevXDqYdp8yg3cC'),(24,'peterflin2318','peterflin4@gmail.com','$2b$12$cuFHi6PW81IIHS6FP1rrwe39oGcmygeczUSmjQCtDLy2CGqHTl3jK'),(25,'peterflin4479','peterflin4@gmail.com','$2b$12$iaz2G6jZhU6R9r8vV0cW6eQ6cTrqmVYtyixff3VxcMP3EmZAGdhle'),(26,'peterflin9283','peterflin4@gmail.com','$2b$12$uDtpV43oyEPgpW8q0Qp/xu6EEcNlFQVo.VA9WOkRqjIyUXj83P.2.'),(27,'peterflin8797','peterflin4@gmail.com','$2b$12$CqrMHsL6xNP1jY4X83LsXeoCpDmoiUcXjBNKio5.43E7nhiAbIwZS'),(28,'peterflin5805','peterflin4@gmail.com','$2b$12$vBXhSlx3z4MtvwULNN8e1eE8J6cMo53FsgtZlg6qdbKMI6oiOPCVW'),(29,'peterflin3965','peterflin4@gmail.com','$2b$12$5V346kOkthao5bc47reqj.J6hqUa7qN0wKAn8bGabTSj4eT3ifPnC'),(30,'peterflin8590','peterflin4@gmail.com','$2b$12$YArKIh9skjlw5RmR50NbBuUcwTu8X6m5uLiX2qZjO6w/EwsxHqf6S'),(31,'peterflin8056','peterflin4@gmail.com','$2b$12$GmNKpDHEbR6zdtNtR5apYuvYzXhYvb.NMWjfUfJBr4gl6f46PdmyW'),(32,'peterflin4912','peterflin4@gmail.com','$2b$12$ktwQOGyL/EvLyYQCiMhb3O9nIrmL./ciVCYfMo.M8krWQy0gw.7FC'),(33,'peterflin5346','peterflin4@gmail.com','$2b$12$SNuHMAPJKQOVofA5F7/RFenWgj1HiS3eevuCOxQIYpmtBcR8eWn1y'),(34,'peterflin7531','peterflin4@gmail.com','$2b$12$2aijZn2NgfiYlKvL6hv4q.sbGABCAjO5zUraW5mNSu6MiQzyqy.BC'),(35,'peterflin3060','peterflin4@gmail.com','$2b$12$GzHhXXsTTrHZkwvkWGRrluqg9tSRnVf7CzTxxxzFLfwz03NYiYrNe'),(37,'peterflin3695','peterflin4@gmail.com','$2b$12$t7E5SM8ktc2g7JJnWbXrA.IuXRVl/BdEFL6BWHU.00vN5PM1vng8m');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-01 20:40:30
