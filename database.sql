-- MySQL dump 10.13  Distrib 5.7.22, for osx10.13 (x86_64)
--
-- Host: 127.0.0.1    Database: IntelligentAnnotationSystem
-- ------------------------------------------------------
-- Server version	5.7.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `title` varchar(45) NOT NULL COMMENT '标题',
  `file_path` varchar(200) NOT NULL COMMENT '文件路径',
  `image_path` varchar(200) DEFAULT NULL COMMENT '封面路径',
  `state` int(11) NOT NULL COMMENT '状态 0=正常 1=清除',
  `author` varchar(45) NOT NULL COMMENT '作者',
  `uploader` int(11) NOT NULL COMMENT '上传人',
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '上传日期',
  PRIMARY KEY (`id`),
  KEY `fk_article_user_idx` (`uploader`),
  CONSTRAINT `fk_article_user` FOREIGN KEY (`uploader`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_comment`
--

DROP TABLE IF EXISTS `article_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `content` varchar(200) NOT NULL COMMENT '内容',
  `state` int(11) NOT NULL COMMENT '状态 0=正常 1=清除',
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '评论日期',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `article_id` int(11) NOT NULL COMMENT '文章id',
  `previous` int(11) DEFAULT NULL COMMENT '上一级评论',
  PRIMARY KEY (`id`),
  KEY `fk_postil_comment_user1_idx` (`user_id`),
  KEY `fk_article_comment_article1_idx` (`article_id`),
  KEY `fk_article_comment_article_comment1_idx` (`previous`),
  CONSTRAINT `fk_article_comment_article1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_article_comment_article_comment1` FOREIGN KEY (`previous`) REFERENCES `article_comment` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_postil_comment_user10` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_comment`
--

LOCK TABLES `article_comment` WRITE;
/*!40000 ALTER TABLE `article_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `article_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_tag`
--

DROP TABLE IF EXISTS `article_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(45) NOT NULL COMMENT 'tag名字',
  `weight` varchar(45) NOT NULL COMMENT '权重',
  `article_id` int(11) NOT NULL COMMENT '文章id',
  PRIMARY KEY (`id`),
  KEY `fk_article_tag_article1_idx` (`article_id`),
  CONSTRAINT `fk_article_tag_article1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_tag`
--

LOCK TABLES `article_tag` WRITE;
/*!40000 ALTER TABLE `article_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `article_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postil`
--

DROP TABLE IF EXISTS `postil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postil` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `content` varchar(400) NOT NULL COMMENT '内容',
  `start` int(11) NOT NULL COMMENT '开始处',
  `end` int(11) NOT NULL COMMENT '结束处',
  `type` int(11) NOT NULL COMMENT '种类',
  `article_id` int(11) NOT NULL COMMENT '文章id',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `state` int(11) NOT NULL COMMENT '状态 0=正常 1=删除',
  PRIMARY KEY (`id`),
  KEY `fk_postil_article1_idx` (`article_id`),
  KEY `fk_postil_user1_idx` (`user_id`),
  CONSTRAINT `fk_postil_article1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_postil_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postil`
--

LOCK TABLES `postil` WRITE;
/*!40000 ALTER TABLE `postil` DISABLE KEYS */;
/*!40000 ALTER TABLE `postil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postil_comment`
--

DROP TABLE IF EXISTS `postil_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postil_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `content` varchar(200) NOT NULL COMMENT '内容',
  `state` int(11) NOT NULL COMMENT '状态 0=正常 1=删除',
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '评论日期',
  `postil_id` int(11) NOT NULL COMMENT '批注id',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `previous` int(11) DEFAULT NULL COMMENT '上一级评论',
  PRIMARY KEY (`id`),
  KEY `fk_postil_comment_postil1_idx` (`postil_id`),
  KEY `fk_postil_comment_user1_idx` (`user_id`),
  KEY `fk_postil_comment_postil_comment1_idx` (`previous`),
  CONSTRAINT `fk_postil_comment_postil1` FOREIGN KEY (`postil_id`) REFERENCES `postil` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_postil_comment_postil_comment1` FOREIGN KEY (`previous`) REFERENCES `postil_comment` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_postil_comment_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postil_comment`
--

LOCK TABLES `postil_comment` WRITE;
/*!40000 ALTER TABLE `postil_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `postil_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `username` varchar(45) NOT NULL COMMENT '用户名',
  `password` varchar(200) NOT NULL COMMENT '密码',
  `email` varchar(45) NOT NULL COMMENT '邮箱',
  `phone` varchar(45) NOT NULL COMMENT '手机',
  `group` int(11) NOT NULL COMMENT '用户组',
  `is_del` int(11) NOT NULL COMMENT '状态',
  `nickname` varchar(45) NOT NULL COMMENT '昵称',
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '注册日期',
  `personas` varchar(45) NOT NULL COMMENT '用户画像',
  `token` varchar(45) NOT NULL COMMENT 'token',
  `intro` text COMMENT '用户简介',
  `avatar_path` varchar(200) DEFAULT NULL COMMENT '用户头像路径',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户信息存储表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','593421b87fabdaa514f3943ab2a037ff5ac3063f63c278e0d6b4a0dc3ee15361','0','0',1,0,'admin','2018-10-03 08:52:30','','',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_history`
--

DROP TABLE IF EXISTS `user_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` tinyint(2) NOT NULL,
  `comment` varchar(45) NOT NULL,
  `target` varchar(45) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_history_user1_idx` (`user_id`),
  CONSTRAINT `fk_user_history_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_history`
--

LOCK TABLES `user_history` WRITE;
/*!40000 ALTER TABLE `user_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_personas`
--

DROP TABLE IF EXISTS `user_personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_personas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL COMMENT '文章id',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `weight` float NOT NULL COMMENT '权重',
  PRIMARY KEY (`id`),
  KEY `user_personas_article_id_fk` (`article_id`),
  KEY `user_personas_user_id_fk_2` (`user_id`),
  CONSTRAINT `user_personas_article_id_fk` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_personas_user_id_fk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户画像表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_personas`
--

LOCK TABLES `user_personas` WRITE;
/*!40000 ALTER TABLE `user_personas` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_personas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-15 12:47:06
