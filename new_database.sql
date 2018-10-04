/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : intelligentannotationsystem

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-10-03 16:52:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `article`
-- ----------------------------
DROP TABLE IF EXISTS `article`;
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

-- ----------------------------
-- Records of article
-- ----------------------------

-- ----------------------------
-- Table structure for `article_comment`
-- ----------------------------
DROP TABLE IF EXISTS `article_comment`;
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

-- ----------------------------
-- Records of article_comment
-- ----------------------------

-- ----------------------------
-- Table structure for `article_tag`
-- ----------------------------
DROP TABLE IF EXISTS `article_tag`;
CREATE TABLE `article_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(45) NOT NULL COMMENT 'tag名字',
  `weight` varchar(45) NOT NULL COMMENT '权重',
  `article_id` int(11) NOT NULL COMMENT '文章id',
  PRIMARY KEY (`id`),
  KEY `fk_article_tag_article1_idx` (`article_id`),
  CONSTRAINT `fk_article_tag_article1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_tag
-- ----------------------------

-- ----------------------------
-- Table structure for `postil`
-- ----------------------------
DROP TABLE IF EXISTS `postil`;
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

-- ----------------------------
-- Records of postil
-- ----------------------------

-- ----------------------------
-- Table structure for `postil_comment`
-- ----------------------------
DROP TABLE IF EXISTS `postil_comment`;
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

-- ----------------------------
-- Records of postil_comment
-- ----------------------------

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户信息存储表';

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', '593421b87fabdaa514f3943ab2a037ff5ac3063f63c278e0d6b4a0dc3ee15361', '0', '0', '1', '0', 'admin', '2018-10-03 16:52:30', '', '');

-- ----------------------------
-- Table structure for `user_history`
-- ----------------------------
DROP TABLE IF EXISTS `user_history`;
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

-- ----------------------------
-- Records of user_history
-- ----------------------------
