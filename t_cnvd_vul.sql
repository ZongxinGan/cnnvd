/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-04-09 20:44:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `t_cnvd_vul`
-- ----------------------------
DROP TABLE IF EXISTS `t_cnvd_vul`;
CREATE TABLE `t_cnvd_vul` (
  `cnvdid` varchar(255) NOT NULL COMMENT 'CNVD ID',
  `title` varchar(255) DEFAULT NULL COMMENT '漏洞名称',
  `publicdate` date DEFAULT NULL COMMENT '公开日期',
  `vullevel` varchar(255) DEFAULT NULL COMMENT '危害级别',
  `impactproducts` varchar(255) DEFAULT NULL COMMENT '影响产品',
  `cveid` varchar(255) DEFAULT NULL COMMENT 'CVE ID',
  `description` text COMMENT '漏洞描述',
  `reference` varchar(255) DEFAULT NULL COMMENT '参考链接',
  `solutions` varchar(255) DEFAULT NULL COMMENT '解决方案',
  `path` varchar(255) DEFAULT NULL COMMENT '厂商补丁',
  `verification` varchar(255) DEFAULT NULL COMMENT '验证信息',
  `classification` int(11) DEFAULT NULL COMMENT '1：web应用漏洞，2：安全产品漏洞，3：应用程序漏洞，4：操作系统漏洞，5：数据库漏洞，6：网络设备漏洞',
  PRIMARY KEY (`cnvdid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_cnvd_vul
-- ----------------------------
