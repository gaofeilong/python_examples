-- phpMyAdmin SQL Dump
-- version 3.0.1.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2013 at 11:17 AM
-- Server version: 5.1.47
-- PHP Version: 5.3.2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


-- --------------------------------------------------------


--
-- Database: `test`
--

DROP DATABASE IF EXISTS `test`;
CREATE DATABASE IF NOT EXISTS `test` CHARACTER SET utf8;
USE `test`;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '' WITH GRANT OPTION;
flush privileges;


-- --------------------------------------------------------

--
-- Table structure for table `investor`
--

CREATE TABLE IF NOT EXISTS `investor` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `key` int(10) unsigned NOT NULL,
  `total_income` int(10) unsigned NOT NULL,
  `total_outcome` int(10) unsigned NOT NULL,
  `total_left` int(10) unsigned NOT NULL,
  `account` text NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

--
-- Dumping data for table `investor`
--
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(1, 1001, 100, 0, 100, '155034199102221X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(2, 1002, 200, 100, 100, '155034199102222X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(3, 1003, 300, 200, 100, '155034199102223X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(4, 1004, 400, 300, 100, '155034199102224X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(5, 1005, 500, 400, 100, '155034199102225X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(6, 1006, 600, 500, 100, '155034199102226X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(7, 1007, 700, 600, 100, '155034199102227X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(8, 1008, 800, 700, 100, '155034199102228X', 'i lost my money');
INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES(9, 1009, 900, 800, 100, '155034199102229X', 'i lost my money');
