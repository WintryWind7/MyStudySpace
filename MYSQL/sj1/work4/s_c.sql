-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: studentsdb
-- ------------------------------------------------------
-- Server version	8.0.44

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

--
-- Table structure for table `curriculum`
--

DROP TABLE IF EXISTS `curriculum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curriculum` (
  `KCH` char(4) NOT NULL COMMENT '课程编号',
  `KCMC` varchar(50) DEFAULT NULL,
  `CREDIT` int DEFAULT NULL COMMENT '学分',
  UNIQUE KEY `cno_idx` (`KCH`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curriculum`
--

LOCK TABLES `curriculum` WRITE;
/*!40000 ALTER TABLE `curriculum` DISABLE KEYS */;
INSERT INTO `curriculum` VALUES ('0001','计算机应用基础',2),('0002','C语言程序设计',2),('0003','数据库原理及应用',2),('0004','英语',4),('0005','高等数学',4);
/*!40000 ALTER TABLE `curriculum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grade`
--

DROP TABLE IF EXISTS `grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grade` (
  `SNO` char(4) NOT NULL COMMENT '学号',
  `KCH` char(4) NOT NULL COMMENT '课程编号',
  `SCORE` decimal(5,2) DEFAULT NULL,
  UNIQUE KEY `grade_sid_cid_idx` (`SNO`,`KCH`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade`
--

LOCK TABLES `grade` WRITE;
/*!40000 ALTER TABLE `grade` DISABLE KEYS */;
INSERT INTO `grade` VALUES ('0001','0002',91.00),('0001','0003',0.00),('0001','0004',85.00),('0001','0005',87.00),('0002','0002',68.00),('0002','0003',0.00),('0002','0004',79.00),('0002','0005',73.00),('0003','0002',92.00),('0003','0003',0.00),('0003','0004',82.00),('0003','0005',75.00),('0004','0006',76.00);
/*!40000 ALTER TABLE `grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_info` (
  `SNO` char(4) NOT NULL COMMENT '学号',
  `SNAME` char(8) NOT NULL COMMENT '姓名',
  `SEX` char(2) DEFAULT NULL COMMENT '性别',
  `BIRTH` date DEFAULT NULL COMMENT '出生日期',
  `ADDRESS` varchar(50) DEFAULT NULL COMMENT '家庭住址',
  `Remark` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES ('0001','张青平','男','2000-10-01','衡阳市东风路77号',NULL),('0002','刘东阳','男','1998-12-09','滨江市新建路196号',NULL),('0003','马晓夏','女','1995-05-12','长岭市五一路763号',NULL),('0004','钱忠理','男','1994-09-23','滨海市洞庭大道279号',NULL),('0005','孙海洋','男','1995-04-03','长岛市解放路27号',NULL),('0006','郭小斌','男','1997-11-10','南山市红旗路113号',NULL),('0007','肖月玲','女','1996-12-07','东方市南京路11号',NULL);
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-23 15:19:21
