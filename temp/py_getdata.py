#!/usr/bin/python
import string
strHead="""-- phpMyAdmin SQL Dump
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
"""
strPreSql = """INSERT INTO `investor` (`id`, `key`, `total_income`, `total_outcome`, `total_left`, `account`, `description`) VALUES"""

stream = open("data.sql", "w")
stream.write(strHead)
for i in range(1, 10):
    key     = 1000 + i
    income  = i * 100
    outcome = (i - 1) * 100
    left    = income - outcome

    strLastSql = "({0}, {1}, {2}, {3}, {4}, '{5}', '{6}');".format(\
                   i, key, income, outcome, left, '15503419910222{0}X'.format(i), 'i lost my money')
    stream.write(strPreSql)
    stream.write(strLastSql + "\n")
