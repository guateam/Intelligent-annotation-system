/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : intelligentannotationsystem

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-10-15 18:50:51
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
  `intro` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_article_user_idx` (`uploader`),
  CONSTRAINT `fk_article_user` FOREIGN KEY (`uploader`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('1', 'Title1', 'static/upload/9237584826.575634新建文本文档.txt', 'static/upload/9237584826.587624timg (1).jpg', '0', 'Author1', '1', '2018-10-15 17:57:51', '这是title1');
INSERT INTO `article` VALUES ('2', 'Title2', 'static/upload/9237584868.975224新建文本文档.txt', 'static/upload/9237584868.987217timg (1).jpg', '0', 'Author2', '1', '2018-10-15 17:57:58', '这是title2');
INSERT INTO `article` VALUES ('3', 'Title3', 'static/upload/9237584914.159182新建文本文档.txt', 'static/upload/9237584914.17117timg (1).jpg', '0', 'Author3', '1', '2018-10-15 17:58:05', '这是title3');
INSERT INTO `article` VALUES ('4', 'Title4', 'static/upload/9237584952.336943新建文本文档.txt', 'static/upload/9237584952.342937timg (1).jpg', '0', 'Author4', '1', '2018-10-15 17:58:12', '这是title4');
INSERT INTO `article` VALUES ('5', 'Title5', 'static/upload/9237584976.808872新建文本文档.txt', 'static/upload/9237584976.814867timg (1).jpg', '0', 'Author5', '1', '2018-10-15 17:58:16', '这是title5');
INSERT INTO `article` VALUES ('6', 'Title6', 'static/upload/9237585003.439526新建文本文档.txt', 'static/upload/9237585003.451508timg (1).jpg', '0', 'Author6', '1', '2018-10-15 17:58:20', '这是title6');
INSERT INTO `article` VALUES ('7', 'Title7', 'static/upload/9237585040.229856新建文本文档.txt', 'static/upload/9237585040.241844timg (1).jpg', '0', 'Author7', '1', '2018-10-15 17:58:26', '这是title7');
INSERT INTO `article` VALUES ('8', 'Title8', 'static/upload/9237585067.011114新建文本文档.txt', 'static/upload/9237585067.017101timg (1).jpg', '0', 'Author8', '1', '2018-10-15 17:58:31', '这是title8');
INSERT INTO `article` VALUES ('9', 'Title9', 'static/upload/9237585110.546227新建文本文档.txt', 'static/upload/9237585110.55822timg (1).jpg', '0', 'Author9', '1', '2018-10-15 17:58:38', '这是title9');

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
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_tag
-- ----------------------------
INSERT INTO `article_tag` VALUES ('1', '体育', '-6.71384620666504', '1');
INSERT INTO `article_tag` VALUES ('2', '财经', '-3.66171741485596', '1');
INSERT INTO `article_tag` VALUES ('3', '房产', '-1.62546157836914', '1');
INSERT INTO `article_tag` VALUES ('4', '家居', '7.51650905609131', '1');
INSERT INTO `article_tag` VALUES ('5', '教育', '-1.61119031906128', '1');
INSERT INTO `article_tag` VALUES ('6', '科技', '-3.55373311042786', '1');
INSERT INTO `article_tag` VALUES ('7', '时尚', '2.83562159538269', '1');
INSERT INTO `article_tag` VALUES ('8', '时政', '-3.26987838745117', '1');
INSERT INTO `article_tag` VALUES ('9', '游戏', '-1.1672694683075', '1');
INSERT INTO `article_tag` VALUES ('10', '娱乐', '-2.64986538887024', '1');
INSERT INTO `article_tag` VALUES ('11', '体育', '-6.71384620666504', '2');
INSERT INTO `article_tag` VALUES ('12', '财经', '-3.66171741485596', '2');
INSERT INTO `article_tag` VALUES ('13', '房产', '-1.62546157836914', '2');
INSERT INTO `article_tag` VALUES ('14', '家居', '7.51650905609131', '2');
INSERT INTO `article_tag` VALUES ('15', '教育', '-1.61119031906128', '2');
INSERT INTO `article_tag` VALUES ('16', '科技', '-3.55373311042786', '2');
INSERT INTO `article_tag` VALUES ('17', '时尚', '2.83562159538269', '2');
INSERT INTO `article_tag` VALUES ('18', '时政', '-3.26987838745117', '2');
INSERT INTO `article_tag` VALUES ('19', '游戏', '-1.1672694683075', '2');
INSERT INTO `article_tag` VALUES ('20', '娱乐', '-2.64986538887024', '2');
INSERT INTO `article_tag` VALUES ('21', '体育', '-6.71384620666504', '3');
INSERT INTO `article_tag` VALUES ('22', '财经', '-3.66171741485596', '3');
INSERT INTO `article_tag` VALUES ('23', '房产', '-1.62546157836914', '3');
INSERT INTO `article_tag` VALUES ('24', '家居', '7.51650905609131', '3');
INSERT INTO `article_tag` VALUES ('25', '教育', '-1.61119031906128', '3');
INSERT INTO `article_tag` VALUES ('26', '科技', '-3.55373311042786', '3');
INSERT INTO `article_tag` VALUES ('27', '时尚', '2.83562159538269', '3');
INSERT INTO `article_tag` VALUES ('28', '时政', '-3.26987838745117', '3');
INSERT INTO `article_tag` VALUES ('29', '游戏', '-1.1672694683075', '3');
INSERT INTO `article_tag` VALUES ('30', '娱乐', '-2.64986538887024', '3');
INSERT INTO `article_tag` VALUES ('31', '体育', '-6.71384620666504', '4');
INSERT INTO `article_tag` VALUES ('32', '财经', '-3.66171741485596', '4');
INSERT INTO `article_tag` VALUES ('33', '房产', '-1.62546157836914', '4');
INSERT INTO `article_tag` VALUES ('34', '家居', '7.51650905609131', '4');
INSERT INTO `article_tag` VALUES ('35', '教育', '-1.61119031906128', '4');
INSERT INTO `article_tag` VALUES ('36', '科技', '-3.55373311042786', '4');
INSERT INTO `article_tag` VALUES ('37', '时尚', '2.83562159538269', '4');
INSERT INTO `article_tag` VALUES ('38', '时政', '-3.26987838745117', '4');
INSERT INTO `article_tag` VALUES ('39', '游戏', '-1.1672694683075', '4');
INSERT INTO `article_tag` VALUES ('40', '娱乐', '-2.64986538887024', '4');
INSERT INTO `article_tag` VALUES ('41', '体育', '-6.71384620666504', '5');
INSERT INTO `article_tag` VALUES ('42', '财经', '-3.66171741485596', '5');
INSERT INTO `article_tag` VALUES ('43', '房产', '-1.62546157836914', '5');
INSERT INTO `article_tag` VALUES ('44', '家居', '7.51650905609131', '5');
INSERT INTO `article_tag` VALUES ('45', '教育', '-1.61119031906128', '5');
INSERT INTO `article_tag` VALUES ('46', '科技', '-3.55373311042786', '5');
INSERT INTO `article_tag` VALUES ('47', '时尚', '2.83562159538269', '5');
INSERT INTO `article_tag` VALUES ('48', '时政', '-3.26987838745117', '5');
INSERT INTO `article_tag` VALUES ('49', '游戏', '-1.1672694683075', '5');
INSERT INTO `article_tag` VALUES ('50', '娱乐', '-2.64986538887024', '5');
INSERT INTO `article_tag` VALUES ('51', '体育', '-6.71384620666504', '6');
INSERT INTO `article_tag` VALUES ('52', '财经', '-3.66171741485596', '6');
INSERT INTO `article_tag` VALUES ('53', '房产', '-1.62546157836914', '6');
INSERT INTO `article_tag` VALUES ('54', '家居', '7.51650905609131', '6');
INSERT INTO `article_tag` VALUES ('55', '教育', '-1.61119031906128', '6');
INSERT INTO `article_tag` VALUES ('56', '科技', '-3.55373311042786', '6');
INSERT INTO `article_tag` VALUES ('57', '时尚', '2.83562159538269', '6');
INSERT INTO `article_tag` VALUES ('58', '时政', '-3.26987838745117', '6');
INSERT INTO `article_tag` VALUES ('59', '游戏', '-1.1672694683075', '6');
INSERT INTO `article_tag` VALUES ('60', '娱乐', '-2.64986538887024', '6');
INSERT INTO `article_tag` VALUES ('61', '体育', '-6.71384620666504', '7');
INSERT INTO `article_tag` VALUES ('62', '财经', '-3.66171741485596', '7');
INSERT INTO `article_tag` VALUES ('63', '房产', '-1.62546157836914', '7');
INSERT INTO `article_tag` VALUES ('64', '家居', '7.51650905609131', '7');
INSERT INTO `article_tag` VALUES ('65', '教育', '-1.61119031906128', '7');
INSERT INTO `article_tag` VALUES ('66', '科技', '-3.55373311042786', '7');
INSERT INTO `article_tag` VALUES ('67', '时尚', '2.83562159538269', '7');
INSERT INTO `article_tag` VALUES ('68', '时政', '-3.26987838745117', '7');
INSERT INTO `article_tag` VALUES ('69', '游戏', '-1.1672694683075', '7');
INSERT INTO `article_tag` VALUES ('70', '娱乐', '-2.64986538887024', '7');
INSERT INTO `article_tag` VALUES ('71', '体育', '-6.71384620666504', '8');
INSERT INTO `article_tag` VALUES ('72', '财经', '-3.66171741485596', '8');
INSERT INTO `article_tag` VALUES ('73', '房产', '-1.62546157836914', '8');
INSERT INTO `article_tag` VALUES ('74', '家居', '7.51650905609131', '8');
INSERT INTO `article_tag` VALUES ('75', '教育', '-1.61119031906128', '8');
INSERT INTO `article_tag` VALUES ('76', '科技', '-3.55373311042786', '8');
INSERT INTO `article_tag` VALUES ('77', '时尚', '2.83562159538269', '8');
INSERT INTO `article_tag` VALUES ('78', '时政', '-3.26987838745117', '8');
INSERT INTO `article_tag` VALUES ('79', '游戏', '-1.1672694683075', '8');
INSERT INTO `article_tag` VALUES ('80', '娱乐', '-2.64986538887024', '8');
INSERT INTO `article_tag` VALUES ('81', '体育', '-6.71384620666504', '9');
INSERT INTO `article_tag` VALUES ('82', '财经', '-3.66171741485596', '9');
INSERT INTO `article_tag` VALUES ('83', '房产', '-1.62546157836914', '9');
INSERT INTO `article_tag` VALUES ('84', '家居', '7.51650905609131', '9');
INSERT INTO `article_tag` VALUES ('85', '教育', '-1.61119031906128', '9');
INSERT INTO `article_tag` VALUES ('86', '科技', '-3.55373311042786', '9');
INSERT INTO `article_tag` VALUES ('87', '时尚', '2.83562159538269', '9');
INSERT INTO `article_tag` VALUES ('88', '时政', '-3.26987838745117', '9');
INSERT INTO `article_tag` VALUES ('89', '游戏', '-1.1672694683075', '9');
INSERT INTO `article_tag` VALUES ('90', '娱乐', '-2.64986538887024', '9');

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
  `intro` text COMMENT '用户简介',
  `avatar_path` varchar(200) DEFAULT NULL COMMENT '用户头像路径',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户信息存储表';

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', '593421b87fabdaa514f3943ab2a037ff5ac3063f63c278e0d6b4a0dc3ee15361', '0', '0', '1', '0', 'admin', '2018-10-03 16:52:30', '', 'GXNBIHe5QJtZ4ounWr72gi81h', '这是一个人~', null);

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_history
-- ----------------------------
INSERT INTO `user_history` VALUES ('1', '3', '', '1', '1', '2018-10-15 18:18:22');

-- ----------------------------
-- Table structure for `user_personas`
-- ----------------------------
DROP TABLE IF EXISTS `user_personas`;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='用户画像表';

-- ----------------------------
-- Records of user_personas
-- ----------------------------
INSERT INTO `user_personas` VALUES ('1', '1', '1', '0.79');
INSERT INTO `user_personas` VALUES ('2', '3', '1', '0.98');
INSERT INTO `user_personas` VALUES ('3', '4', '1', '0.01');

-- ----------------------------
-- Table structure for `user_personas_postil`
-- ----------------------------
DROP TABLE IF EXISTS `user_personas_postil`;
CREATE TABLE `user_personas_postil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `postil_id` int(11) NOT NULL COMMENT '文章id',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `weight` float NOT NULL COMMENT '权重',
  PRIMARY KEY (`id`),
  KEY `user_personas_article_id_fk` (`postil_id`),
  KEY `user_personas_user_id_fk_2` (`user_id`),
  CONSTRAINT `user_personas_postil_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_personas_postil_ibfk_3` FOREIGN KEY (`postil_id`) REFERENCES `postil` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户画像表';

-- ----------------------------
-- Records of user_personas_postil
-- ----------------------------
