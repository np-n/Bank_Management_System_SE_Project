-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 11, 2019 at 05:16 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `yvd_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `barak_obama_7500020_loan`
--

CREATE TABLE `barak_obama_7500020_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `barak_obama_7500020_loan`
--

INSERT INTO `barak_obama_7500020_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:56:21 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000200000);

-- --------------------------------------------------------

--
-- Table structure for table `bhuwan_207500004`
--

CREATE TABLE `bhuwan_207500004` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bhuwan_207500004`
--

INSERT INTO `bhuwan_207500004` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Mon Mar 11 12:45:45 2019', 'Acoount register', '0.0(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000040000),
('Fri Jul 19 20:38:08 2019', 'Receive amt', '1000', 'Mukti Prasad Dumre', 'Mukti Prasad Dumre(207500012)', 'Pokhara', '--------', 2075000040001);

-- --------------------------------------------------------

--
-- Table structure for table `binayak_207500022`
--

CREATE TABLE `binayak_207500022` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer_data`
--

CREATE TABLE `customer_data` (
  `ac_holder_name` varchar(50) DEFAULT NULL,
  `f_name` varchar(50) DEFAULT NULL,
  `m_name` varchar(50) DEFAULT NULL,
  `sex` varchar(50) NOT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `interest_date` date NOT NULL,
  `mobile_no` varchar(25) DEFAULT NULL,
  `account_type` varchar(55) DEFAULT NULL,
  `id_number` varchar(55) DEFAULT NULL,
  `id_type` varchar(55) DEFAULT NULL,
  `occupation` varchar(20) DEFAULT NULL,
  `per_address` varchar(55) DEFAULT NULL,
  `tem_address` varchar(55) DEFAULT NULL,
  `current_amount` double DEFAULT NULL,
  `image_directory` varchar(200) NOT NULL,
  `account_num` bigint(20) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `date_account_open` varchar(50) DEFAULT NULL,
  `branch` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_data`
--

INSERT INTO `customer_data` (`ac_holder_name`, `f_name`, `m_name`, `sex`, `dob`, `interest_date`, `mobile_no`, `account_type`, `id_number`, `id_type`, `occupation`, `per_address`, `tem_address`, `current_amount`, `image_directory`, `account_num`, `created_by`, `date_account_open`, `branch`) VALUES
('Netra Prasad Neupane', 'Peu Narayan Neupane', 'Tika Neupane', 'male', '2055-01-30', '2019-07-19', '9846626929', 'Saving', '422045/740', 'Citizenship', 'Student', 'Walling-12 Syangja', 'Lamachaur Pokhara', 6637, '', 207500001, 'Netra Prasad Neupane', '2075-09-04', 'kathmandu'),
('Bikash Panday', 'Pharsuram Panday', 'Manju Pnaday', 'male', '2054-05-9', '2019-07-19', '9845813662', 'Fixed account', '073BCT626', 'Citizenship', 'Student', 'Chitwan', 'Lamachaur Pokhara', 1150.199300700676, '', 207500002, 'Hari Aryal', '2075-09-17', 'kathmandu'),
('Netra Pr', '', '', 'select', 'year-month-day', '2019-03-10', '', 'select', '', 'select', 'select/Enter', '', '', 111, '', 207500003, 'Netra Prasad Neupane', 'Sun Mar 10 12:26:02 2019', 'select'),
('Bhuwan', '', '', 'male', 'year-month-day', '2019-03-11', '', 'select', '', 'select', 'Student', 'Pokhara', '', 1000, '', 207500004, 'Netra Prasad Neupane', 'Mon Mar 11 12:45:45 2019', 'select'),
('Hari Nepal', '', '', 'female', 'year-month-day', '2019-07-19', '98464', 'Saving', '3333333', 'select', 'select/Enter', '', '', 0, '', 207500005, 'Netra Prasad Neupane', 'Mon Mar 11 21:39:59 2019', 'select'),
('Dipen Thapa', 'Gyan Bahadur Thapa', '', 'male', 'year-month-day', '2019-07-19', '9806725880', 'Saving', '073BCT619', 'Student Card', 'select/Enter', 'Butwal', '', 4103.447973783894, '', 207500006, 'Netra Prasad Neupane', 'Wed Mar 13 13:15:05 2019', 'select'),
('Niraj Yogi', 'kamal Yogi', 'Mm', 'male', '1954-3-4', '2019-07-19', '984666666', 'Current', '11111', 'Citizenship', 'Student', 'ktm', '', 9089.676479639706, '', 207500007, 'Netra Prasad Neupane', 'Wed Mar 20 13:17:09 2019', 'Kathmandu'),
('Radhika Neupane', 'Janak Neupane', 'Janaki Neupane', 'female', '2073-9-7', '2019-07-19', '98476259703', 'Saving', '073hjfh', 'Student Card', 'Student', 'walling 13', 'Pokhara', 20296.207692956556, '', 207500008, 'Netra Prasad Neupane', 'Sat Apr 20 20:00:33 2019', 'Walling'),
('Naran Neupane', 'Peu Neupane', 'Pema Neupane', 'male', '1952-4-7', '2019-07-19', '98466269', 'Fixed account', '22222', 'driving License', 'Broker', 'Syangja', 'Pokhara', 10230.199286920622, 'c:/img1.png', 207500009, 'Netra Prasad Neupane', 'Fri Apr 26 21:03:31 2019', 'Butwal'),
('Nimesh Neupane', 'Peu Neupane', 'Pema Neupane', 'male', '1960-4-4', '2019-07-19', '984776545', 'Saving', '88888', 'Student Card', 'Doctor', 'Syangja', 'Pokhara', 5095.712531431788, '', 207500010, 'Netra Prasad Neupane', 'Sat Mar 27 12:16:21 2019', 'Bharatpur'),
('Dipesh Gautam', 'Surya', '', 'select', 'year-month-day', '2019-07-19', '93784764', 'Current', '888888888888', 'Citizenship', 'Teacher', 'Chitwan', 'pokhara', 11091.275158644397, '', 207500011, 'Netra Prasad Neupane', 'Thu May  9 17:44:53 2019', 'Butwal'),
('Mukti Prasad Dumre', 'Poskanta Dumre', 'Thagikala Dumre', 'male', '2050-9-7', '2019-07-19', '9847557382', 'Fixed account', '422047/235', 'Citizenship', 'Accountant', 'Walling-14 Syangja', 'Butwal', 996000, '', 207500012, 'Netra Prasad Neupane', 'Fri Jul 19 20:24:52 2019', 'Pokhara');

-- --------------------------------------------------------

--
-- Table structure for table `dipen_thapa_7500034_loan`
--

CREATE TABLE `dipen_thapa_7500034_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipen_thapa_7500034_loan`
--

INSERT INTO `dipen_thapa_7500034_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Wed Mar 13 13:30:54 2019', 'withdraw loan', '1000.0', 'self', 'select', 'Netra Prasad Neupane', 75000340000),
('Wed Mar 13 13:33:26 2019', 'loan payment', '1000', 'self', 'select', '--------', 75000340001);

-- --------------------------------------------------------

--
-- Table structure for table `dipen_thapa_207500006`
--

CREATE TABLE `dipen_thapa_207500006` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipen_thapa_207500006`
--

INSERT INTO `dipen_thapa_207500006` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Wed Mar 13 13:15:05 2019', 'Acoount register', '1000.0(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000060000),
('Wed Mar 13 13:16:52 2019', 'deposit', '5000', 'Amar Nepali', '--------', 'select', '--------', 2075000060001),
('Wed Mar 13 13:18:22 2019', 'withdraw', '1000', 'Netra Neupane', '--------', 'select', '--------', 2075000060002),
('Wed Mar 13 13:19:11 2019', 'Transfer', '1000', 'Dipen Thapa', 'Netra Prasad Neupane(207500001)', 'kathmandu', '--------', 2075000060003),
('Wed Mar 13 13:20:41 2019', 'edit', '0', 'self', '--------', 'select', '--------', 2075000060004);

-- --------------------------------------------------------

--
-- Table structure for table `dipesh_gautam_207500011`
--

CREATE TABLE `dipesh_gautam_207500011` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipesh_gautam_207500011`
--

INSERT INTO `dipesh_gautam_207500011` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Thu May  9 17:44:53 2019', 'Acoount register', '10000.0(deposit)', 'self', '______________', 'Butwal', 'Netra Prasad Neupane', 2075000110000),
('Thu May  9 17:48:05 2019', 'deposit', '2000', 'surya', '--------', 'Butwal', '--------', 2075000110001),
('Thu May  9 17:48:48 2019', 'withdraw', '1000', 'bikash', '--------', 'Butwal', '--------', 2075000110002),
('Thu May  9 17:50:44 2019', 'Transfer', '2', 'Dipesh Gautam', 'Netra Prasad Neupane(207500001)', 'kathmandu', '--------', 2075000110003),
('Thu May  9 17:55:28 2019', 'edit', '0', 'self', '--------', 'Butwal', '--------', 2075000110004),
('Thu May  9 18:02:30 2019', 'edit', '0', 'self', '--------', 'Butwal', '--------', 2075000110005);

-- --------------------------------------------------------

--
-- Table structure for table `donald_trump_7500019_loan`
--

CREATE TABLE `donald_trump_7500019_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `donald_trump_7500019_loan`
--

INSERT INTO `donald_trump_7500019_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:55:03 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000190000);

-- --------------------------------------------------------

--
-- Table structure for table `hakdjkhsjkfhdjkf_7500023_loan`
--

CREATE TABLE `hakdjkhsjkfhdjkf_7500023_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hakdjkhsjkfhdjkf_7500023_loan`
--

INSERT INTO `hakdjkhsjkfhdjkf_7500023_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 15:13:37 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000230000);

-- --------------------------------------------------------

--
-- Table structure for table `hari_nepal_207500005`
--

CREATE TABLE `hari_nepal_207500005` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hari_nepal_207500005`
--

INSERT INTO `hari_nepal_207500005` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Mon Mar 11 21:39:59 2019', 'Acoount register', '0.0(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000050000);

-- --------------------------------------------------------

--
-- Table structure for table `harooooo_7500017_loan`
--

CREATE TABLE `harooooo_7500017_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `harooooo_7500017_loan`
--

INSERT INTO `harooooo_7500017_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:47:53 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000170000);

-- --------------------------------------------------------

--
-- Table structure for table `hekjfkdjfd_7500030_loan`
--

CREATE TABLE `hekjfkdjfd_7500030_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hekjfkdjfd_7500030_loan`
--

INSERT INTO `hekjfkdjfd_7500030_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sun Mar 10 12:43:23 2019', 'withdraw loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000300000);

-- --------------------------------------------------------

--
-- Table structure for table `hellowedsf_7500024_loan`
--

CREATE TABLE `hellowedsf_7500024_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hellowedsf_7500024_loan`
--

INSERT INTO `hellowedsf_7500024_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 15:28:18 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000240000);

-- --------------------------------------------------------

--
-- Table structure for table `hellowr_7500018_loan`
--

CREATE TABLE `hellowr_7500018_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hellowr_7500018_loan`
--

INSERT INTO `hellowr_7500018_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:48:55 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000180000);

-- --------------------------------------------------------

--
-- Table structure for table `hhhhkfg_7500029_loan`
--

CREATE TABLE `hhhhkfg_7500029_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hhhhkfg_7500029_loan`
--

INSERT INTO `hhhhkfg_7500029_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sun Mar 10 12:39:12 2019', 'withdraw loan', '100000.0', 'self', 'select', 'Netra Prasad Neupane', 75000290000);

-- --------------------------------------------------------

--
-- Table structure for table `janak_207500025`
--

CREATE TABLE `janak_207500025` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `janak_207500025`
--

INSERT INTO `janak_207500025` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Mon Feb 25 18:37:54 2019', 'Acoount register', '20000.0(deposit)', 'self', '______________', 'Butwal', 'Netra Prasad Neupane', 2075000250000),
('Mon Feb 25 18:52:52 2019', 'withdraw', '4343', 'Netra Neupane', '--------', 'Butwal', '--------', 2075000250001),
('Mon Feb 25 18:54:18 2019', 'deposit', '2000', 'self', '--------', 'Butwal', '--------', 2075000250002),
('Mon Feb 25 18:55:05 2019', 'Transfer', '1000', 'Janak', 'Netra(207500004)', 'pokhara', '--------', 2075000250003),
('Mon Feb 25 18:57:32 2019', 'edit', '0', 'self', '--------', 'Butwal', '--------', 2075000250004);

-- --------------------------------------------------------

--
-- Table structure for table `jenny_207500018`
--

CREATE TABLE `jenny_207500018` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `jhgjkl_7500015_loan`
--

CREATE TABLE `jhgjkl_7500015_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jhgjkl_7500015_loan`
--

INSERT INTO `jhgjkl_7500015_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:44:49 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000150000);

-- --------------------------------------------------------

--
-- Table structure for table `jnaak_207500023`
--

CREATE TABLE `jnaak_207500023` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jnaak_207500023`
--

INSERT INTO `jnaak_207500023` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Sun Feb  3 23:16:29 2019', 'Acoount register', '1000(deposit)', 'self', '______________', 'Walling', 'Netra Prasad Neupane', 1),
('Mon Feb  4 20:52:10 2019', 'Receive amt', '1000', 'Netra', 'Netra(207500004)', 'pokhara', '--------', 5),
('Mon Feb  4 22:20:08 2019', 'Receive amt', '1000', 'Netra', 'Netra(207500004)', 'pokhara', '--------', 6),
('Mon Feb  4 22:23:02 2019', 'Receive amt', '4544', 'Netra', 'Netra(207500004)', 'pokhara', '--------', 7);

-- --------------------------------------------------------

--
-- Table structure for table `keshav_bhusal_7500028_loan`
--

CREATE TABLE `keshav_bhusal_7500028_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `keshav_bhusal_7500028_loan`
--

INSERT INTO `keshav_bhusal_7500028_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Tue Mar  5 19:36:08 2019', 'get loan', '200000.0', 'self', 'Butwal', 'Netra Prasad Neupane', 75000280000),
('Tue Mar  5 19:42:20 2019', 'loan payment', '10000', 'Balika Bhusal', 'Butwal', '--------', 75000280001);

-- --------------------------------------------------------

--
-- Table structure for table `keshav_bhusal_207500019`
--

CREATE TABLE `keshav_bhusal_207500019` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `keshav_bh_207500028`
--

CREATE TABLE `keshav_bh_207500028` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `keshav_bh_207500028`
--

INSERT INTO `keshav_bh_207500028` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Tue Mar  5 20:01:41 2019', 'Acoount register', '0.0(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000280000),
('Tue Mar  5 20:04:35 2019', 'Receive amt', '1000', 'Netra', 'Netra(207500004)', 'pokhara', '--------', 2075000280001),
('Tue Mar  5 20:08:15 2019', 'Receive amt', '1000', 'Netra', 'Netra(207500004)', 'pokhara', '--------', 2075000280002);

-- --------------------------------------------------------

--
-- Table structure for table `kjkjdkfdjfdkfb_7500022_loan`
--

CREATE TABLE `kjkjdkfdjfdkfb_7500022_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `kjkjdkfdjfdkfb_7500022_loan`
--

INSERT INTO `kjkjdkfdjfdkfb_7500022_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:58:02 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000220000);

-- --------------------------------------------------------

--
-- Table structure for table `loan_data`
--

CREATE TABLE `loan_data` (
  `ac_holder_name` varchar(55) NOT NULL,
  `f_name` varchar(55) NOT NULL,
  `m_name` varchar(55) NOT NULL,
  `sex` varchar(55) NOT NULL,
  `dob` date NOT NULL,
  `mobile_no` varchar(15) NOT NULL,
  `loan_type` varchar(55) NOT NULL,
  `id_number` varchar(55) NOT NULL,
  `id_type` varchar(55) NOT NULL,
  `occupation` varchar(55) NOT NULL,
  `per_address` varchar(55) NOT NULL,
  `tem_address` varchar(55) NOT NULL,
  `lalpurja_no` varchar(55) NOT NULL,
  `loan_amount` double NOT NULL,
  `image_directory` varchar(55) NOT NULL,
  `loan_acc_no` bigint(20) NOT NULL,
  `created_by` varchar(55) NOT NULL,
  `date_account_open` varchar(55) NOT NULL,
  `branch` varchar(55) NOT NULL,
  `loan_date` date NOT NULL,
  `paid_time_in_years` int(11) NOT NULL,
  `loan_withdrawn_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `loan_data`
--

INSERT INTO `loan_data` (`ac_holder_name`, `f_name`, `m_name`, `sex`, `dob`, `mobile_no`, `loan_type`, `id_number`, `id_type`, `occupation`, `per_address`, `tem_address`, `lalpurja_no`, `loan_amount`, `image_directory`, `loan_acc_no`, `created_by`, `date_account_open`, `branch`, `loan_date`, `paid_time_in_years`, `loan_withdrawn_date`) VALUES
('Netra Prasad Neupane', 'Peu Narayan Neupane', 'Pema Neupane', 'male', '2055-01-30', '9846626929', 'educational loan', '422045/740', 'citizenship', 'student', 'Syangja', 'Pokhara', '3376763', 10899.811961541644, 'kdjffdfd/dfljdf', 7500001, 'Netra Prasad Neupane', '2048-3-33', 'Pokhara', '2019-07-19', 2, '0000-00-00'),
('Hari', '', '', 'select', '1953-06-05', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500002, 'Netra Prasad Neupane', 'Fri Mar  1 23:39:15 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Suraj', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500003, 'Netra Prasad Neupane', 'Fri Mar  1 23:41:19 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Himal Puri', '', '', 'select', '1952-04-05', '', 'Vehicle loan', '', 'driving License', 'select/Enter', '', '', '', 0, '', 7500004, 'Netra Prasad Neupane', 'Fri Mar  1 23:56:19 2019', 'Pokhara', '2019-07-19', 2, '0000-00-00'),
('Harui', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500005, 'Netra Prasad Neupane', 'Fri Mar  1 23:59:22 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Hari', '', '', 'select', '0000-00-00', '33333', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500006, 'Netra Prasad Neupane', 'Sat Mar  2 00:00:12 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Sujan', '', '', 'select', '0000-00-00', '22222', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500007, 'Netra Prasad Neupane', 'Sat Mar  2 00:01:54 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Surya', '', '', 'select', '0000-00-00', '0000', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500008, 'Netra Prasad Neupane', 'Sat Mar  2 00:04:04 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Suraj', '', '', 'select', '0000-00-00', '9845534333', 'select', '', 'select', 'select/Enter', '', '', '', 10947.644320822525, '', 7500009, 'Netra Prasad Neupane', 'Sat Mar  2 12:42:08 2019', 'select', '2019-07-19', 4, '0000-00-00'),
('Suraj', 'Thagparsad Neupane', 'Fofala', 'male', '2054-05-05', '8888888', 'Ag farming loan', '4354/45', 'driving License', 'Engineer', 'syangja', 'ktm', '454554545', 107751.44329815797, 'kjhm', 7500010, 'Netra Prasad Neupane', 'Sat Mar  2 12:58:36 2019', 'Pokhara', '2019-07-19', 2, '0000-00-00'),
('Suraj', 'Thagparsad Neupane', 'Fofala', 'male', '2054-05-05', '88888888889', 'Ag farming loan', '4354/458', 'driving License', 'Engineer', 'syangja', 'ktm', '454554545', 107751.44329815797, 'kjhm', 7500011, 'Netra Prasad Neupane', 'Sat Mar  2 12:58:36 2019', 'Pokhara', '2019-07-19', 2, '0000-00-00'),
('Rabindara', 'Syjdf', 'Maya', 'male', '2002-07-08', '4390843', 'Ag farming loan', '43545l454', 'driving License', 'Doctor', 'pkhr', 'ktm', '8976890-', 10775.144329815801, '21323lkjhgk', 7500012, 'Netra Prasad Neupane', 'Sat Mar  2 13:01:05 2019', 'Butwal', '2019-07-19', 1, '0000-00-00'),
('Oihjk', '', '', 'select', '0000-00-00', 'lkiuhkl', 'select', '890p9', 'select', 'select/Enter', '', '', '', 0, '', 7500013, 'Netra Prasad Neupane', 'Sat Mar  2 14:26:40 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500014, 'Netra Prasad Neupane', 'Sat Mar  2 14:43:20 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Jhgjkl', '', '', 'select', '0000-00-00', '', 'select', 'kjhgf,', 'select', 'select/Enter', '', '', '', 0, '', 7500015, 'Netra Prasad Neupane', 'Sat Mar  2 14:44:49 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Sunil', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500016, 'Netra Prasad Neupane', 'Sat Mar  2 14:47:27 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Harooooo', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500017, 'Netra Prasad Neupane', 'Sat Mar  2 14:47:53 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Hellowr', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500018, 'Netra Prasad Neupane', 'Sat Mar  2 14:48:55 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Donald Trump', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500019, 'Netra Prasad Neupane', 'Sat Mar  2 14:55:03 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Barak Obama', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500020, 'Netra Prasad Neupane', 'Sat Mar  2 14:56:21 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Lkjhgjkl;', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500021, 'Netra Prasad Neupane', 'Sat Mar  2 14:57:22 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Kjkjdkfdjfdkfb', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500022, 'Netra Prasad Neupane', 'Sat Mar  2 14:58:02 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Hakdjkhsjkfhdjkf', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500023, 'Netra Prasad Neupane', 'Sat Mar  2 15:13:37 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Hellowedsf', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500024, 'Netra Prasad Neupane', 'Sat Mar  2 15:28:18 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Mahesh', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 93.80530097348064, '', 7500025, 'Netra Prasad Neupane', 'Sat Mar  2 18:47:22 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Sunil Dumre', '', '', 'select', '0000-00-00', '', 'select', '11111', 'select', 'select/Enter', '', '', '222222', 489516.67273435695, '', 7500026, 'Netra Prasad Neupane', 'Sat Mar  2 22:15:48 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Suraj Khanal', '', '', 'select', '0000-00-00', '', 'Helth loan', '', 'select', 'select/Enter', '', '', '3864863873', 2152552.905454065, '', 7500027, 'Netra Prasad Neupane', 'Tue Mar  5 18:40:23 2019', 'select', '2019-07-19', 0, '0000-00-00'),
('Keshav Bhusal', 'Kamal Bhusal', 'Balika Bhusal', 'male', '2056-08-03', '9867232660', 'Buisness loan', 'PAS074BGE021', 'Student Card', 'Student', 'Butwal', 'Butwal', '22222', 204526.12833933107, '', 7500028, 'Netra Prasad Neupane', 'Tue Mar  5 19:36:08 2019', 'Butwal', '2019-07-19', 2, '0000-00-00'),
('Hhhhkfg', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 107351.08920568535, '', 7500029, 'Netra Prasad Neupane', 'Sun Mar 10 12:39:12 2019', 'select', '2019-07-19', 0, '2019-03-10'),
('Hekjfkdjfd', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500030, 'Netra Prasad Neupane', 'Sun Mar 10 12:43:23 2019', 'select', '2019-07-19', 0, '2019-03-10'),
('Sunil Sign', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500031, 'Netra Prasad Neupane', 'Sun Mar 10 12:47:01 2019', 'select', '2019-07-19', 0, '2019-03-10'),
('Sibjrejf', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500032, 'Netra Prasad Neupane', 'Sun Mar 10 12:49:00 2019', 'select', '2019-07-19', 0, '2019-03-10'),
('Sibjrejf7686', '', '', 'select', '0000-00-00', '', 'select', '', 'select', 'select/Enter', '', '', '', 0, '', 7500033, 'Netra Prasad Neupane', 'Sun Mar 10 12:49:00 2019', 'select', '2019-07-19', 0, '2019-03-10'),
('Dipen Thapa', '', '', 'select', '0000-00-00', '', 'Vehicle loan', '', 'select', 'select/Enter', '', '', '66666', 0, '', 7500034, 'Netra Prasad Neupane', 'Wed Mar 13 13:30:54 2019', 'select', '2019-07-19', 0, '2019-03-13'),
('Nimesh Neupane', 'Peu Neupane', 'Pema Neupane', 'male', '1961-04-05', '9784489588', 'Helth loan', '88888', 'Student Card', 'Engineer', 'Syangja', 'Pokhara', '10101010', 425808.3693000563, '', 7500035, 'Netra Prasad Neupane', 'Sat Mar 25 13:19:02 2019', 'Bharatpur', '2019-07-19', 5, '2019-04-27'),
('Mukti', '', '', 'select', '0000-00-00', '', 'Ag farming loan', '', 'select', 'select/Enter', '', '', '', 100000, '', 7500036, 'Netra Prasad Neupane', 'Fri Jul 19 20:40:17 2019', 'select', '2019-07-19', 0, '2019-07-19');

-- --------------------------------------------------------

--
-- Table structure for table `mahesh_7500025_loan`
--

CREATE TABLE `mahesh_7500025_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mahesh_7500025_loan`
--

INSERT INTO `mahesh_7500025_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 18:47:22 2019', 'get loan', '87.0', 'self', 'select', 'Netra Prasad Neupane', 75000250000);

-- --------------------------------------------------------

--
-- Table structure for table `mukti_7500036_loan`
--

CREATE TABLE `mukti_7500036_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mukti_7500036_loan`
--

INSERT INTO `mukti_7500036_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Fri Jul 19 20:40:17 2019', 'withdraw loan', '100000.0', 'self', 'select', 'Netra Prasad Neupane', 75000360000);

-- --------------------------------------------------------

--
-- Table structure for table `mukti_prasad_dumre_207500012`
--

CREATE TABLE `mukti_prasad_dumre_207500012` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mukti_prasad_dumre_207500012`
--

INSERT INTO `mukti_prasad_dumre_207500012` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Fri Jul 19 20:24:52 2019', 'Acoount register', '0.0(deposit)', 'self', '______________', 'Pokhara', 'Netra Prasad Neupane', 2075000120000),
('Fri Jul 19 20:30:39 2019', 'deposit', '1000000', 'self', '--------', 'Pokhara', '--------', 2075000120001),
('Fri Jul 19 20:33:40 2019', 'Transfer', '1000', 'Mukti Prasad Dumre', 'Netra Prasad Neupane(207500001)', 'kathmandu', '--------', 2075000120002),
('Fri Jul 19 20:38:08 2019', 'Transfer', '1000', 'Mukti Prasad Dumre', 'Bhuwan(207500004)', 'select', '--------', 2075000120003),
('Fri Jul 19 20:39:42 2019', 'withdraw', '2000', 'self', '--------', 'Pokhara', '--------', 2075000120004),
('Fri Jul 19 20:42:30 2019', 'edit', '0', 'self', '--------', 'Pokhara', '--------', 2075000120005);

-- --------------------------------------------------------

--
-- Table structure for table `naran_207500024`
--

CREATE TABLE `naran_207500024` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `naran_207500024`
--

INSERT INTO `naran_207500024` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Sun Feb  3 23:52:50 2019', 'Acoount register', '2000(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000240000),
('Sun Feb  3 23:54:01 2019', 'withdraw', '1000', 'self', '--------', 'select', '--------', 2075000240001),
('Sun Feb  3 23:54:38 2019', 'deposit', '1000', 'self', '--------', 'select', '--------', 2075000240002),
('Mon Feb  4 00:05:24 2019', 'edit', '0', 'self', '--------', 'select', '--------', 2075000240003);

-- --------------------------------------------------------

--
-- Table structure for table `naran_neupane_207500009`
--

CREATE TABLE `naran_neupane_207500009` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `naran_neupane_207500009`
--

INSERT INTO `naran_neupane_207500009` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Fri Apr 26 21:03:31 2019', 'Acoount register', '1000.0(deposit)', 'self', '______________', 'Butwal', 'Netra Prasad Neupane', 2075000090000),
('Fri Apr 26 21:06:24 2019', 'deposit', '9000', 'Jk Neupane', '--------', 'Butwal', '--------', 2075000090001),
('Fri Apr 26 21:08:32 2019', 'edit', '0', 'self', '--------', 'Butwal', '--------', 2075000090002);

-- --------------------------------------------------------

--
-- Table structure for table `netra_207500004`
--

CREATE TABLE `netra_207500004` (
  `date_and_time` varchar(50) NOT NULL,
  `operation` varchar(50) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `performed_by` varchar(50) NOT NULL,
  `transfer_to` varchar(50) NOT NULL,
  `branch` varchar(50) NOT NULL,
  `issued_by` varchar(50) NOT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `netra_207500004`
--

INSERT INTO `netra_207500004` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('2075-10-03', 'register and deposit', '1000', '-----', '----', 'ktm', '----', 2075000401),
('Sun Feb  3 23:03:20 2019', 'withdraw', '2000', 'self', '--------', 'pokhara', '--------', 2075000402),
('Mon Feb  4 20:46:04 2019', 'Transfer', '1000', 'Netra', 'Jnaak(207500023)', 'Walling', '--------', 2075000403),
('Mon Feb  4 20:50:06 2019', 'Transfer', '1000', 'Netra', 'Jnaak(207500023)', 'Walling', '--------', 2075000404),
('Mon Feb  4 20:52:10 2019', 'Transfer', '1000', 'Netra', 'Jnaak(207500023)', 'Walling', '--------', 2075000405),
('Mon Feb  4 22:20:08 2019', 'Transfer', '1000', 'Netra', 'Jnaak(207500023)', 'Walling', '--------', 2075000406),
('Mon Feb  4 22:23:02 2019', 'Transfer', '4544', 'Netra', 'Jnaak(207500023)', 'Walling', '--------', 2075000407),
('Mon Feb 25 18:55:05 2019', 'Receive amt', '1000', 'Janak', 'Janak(207500025)', 'Butwal', '--------', 2075000408),
('Sat Mar  2 18:50:35 2019', 'withdraw', '10000', 'mahesh', '--------', 'pokhara', '--------', 2075000409),
('Tue Mar  5 20:04:35 2019', 'Transfer', '1000', 'Netra', 'Keshav Bh(207500028)', 'select', '--------', 2075000410),
('Tue Mar  5 20:08:15 2019', 'Transfer', '1000', 'Netra', 'Keshav Bh(207500028)', 'select', '--------', 2075000411);

-- --------------------------------------------------------

--
-- Table structure for table `netra_pr_207500003`
--

CREATE TABLE `netra_pr_207500003` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `netra_pr_207500003`
--

INSERT INTO `netra_pr_207500003` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Sun Mar 10 12:26:02 2019', 'Acoount register', '1111.0(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000030000),
('Sun Mar 10 12:27:25 2019', 'withdraw', '1000', 'self', '--------', 'select', '--------', 2075000030001);

-- --------------------------------------------------------

--
-- Table structure for table `nimesh_neupane_7500035_loan`
--

CREATE TABLE `nimesh_neupane_7500035_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nimesh_neupane_7500035_loan`
--

INSERT INTO `nimesh_neupane_7500035_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Apr 27 13:19:02 2019', 'withdraw loan', '500000.0', 'self', 'Bharatpur', 'Netra Prasad Neupane', 75000350000),
('Sat Apr 27 13:22:16 2019', 'loan payment', '100000', 'peu neupane(father)', 'Bharatpur', '--------', 75000350001);

-- --------------------------------------------------------

--
-- Table structure for table `nimesh_neupane_207500010`
--

CREATE TABLE `nimesh_neupane_207500010` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nimesh_neupane_207500010`
--

INSERT INTO `nimesh_neupane_207500010` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Sat Apr 27 12:16:21 2019', 'Acoount register', '1000.0(deposit)', 'self', '______________', 'Bharatpur', 'Netra Prasad Neupane', 2075000100000),
('Sat Apr 27 13:00:28 2019', 'deposit', '9000', 'Sarita Neupane', '--------', 'Bharatpur', '--------', 2075000100001),
('Sat Apr 27 13:01:59 2019', 'withdraw', '2000', 'Naran Neupane', '--------', 'Bharatpur', '--------', 2075000100002),
('Sat Apr 27 13:09:03 2019', 'Transfer', '3000', 'Nimesh Neupane', 'Netra Prasad Neupane(207500001)', 'kathmandu', '--------', 2075000100003),
('Sat Apr 27 14:08:33 2019', 'edit', '0', 'self', '--------', 'Bharatpur', '--------', 2075000100004);

-- --------------------------------------------------------

--
-- Table structure for table `niraj_yogi_207500007`
--

CREATE TABLE `niraj_yogi_207500007` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `niraj_yogi_207500007`
--

INSERT INTO `niraj_yogi_207500007` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Wed Mar 20 13:17:09 2019', 'Acoount register', '1000.0(deposit)', 'self', '______________', 'Kathmandu', 'Netra Prasad Neupane', 2075000070000),
('Wed Mar 20 13:21:21 2019', 'withdraw', '500', 'netra prasad neupane', '--------', 'Kathmandu', '--------', 2075000070001),
('Wed Mar 20 13:21:53 2019', 'deposit', '10000', 'self', '--------', 'Kathmandu', '--------', 2075000070002),
('Wed Mar 20 13:22:38 2019', 'Transfer', '1500', 'Niraj Yogi', 'Netra Prasad Neupane(207500001)', 'kathmandu', '--------', 2075000070003),
('Wed Mar 20 13:23:34 2019', 'edit', '0', 'self', '--------', 'Kathmandu', '--------', 2075000070004);

-- --------------------------------------------------------

--
-- Table structure for table `oihjk_7500013_loan`
--

CREATE TABLE `oihjk_7500013_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `oihjk_7500013_loan`
--

INSERT INTO `oihjk_7500013_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:26:40 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000130000);

-- --------------------------------------------------------

--
-- Table structure for table `paras_207500021`
--

CREATE TABLE `paras_207500021` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rabindara_7500012_loan`
--

CREATE TABLE `rabindara_7500012_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rabindara_7500012_loan`
--

INSERT INTO `rabindara_7500012_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 13:01:05 2019', 'get loan', '10000.0', 'self', 'Butwal', 'Netra Prasad Neupane', 75000120000);

-- --------------------------------------------------------

--
-- Table structure for table `radhika_neupane_207500008`
--

CREATE TABLE `radhika_neupane_207500008` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `radhika_neupane_207500008`
--

INSERT INTO `radhika_neupane_207500008` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Sat Apr 20 20:00:33 2019', 'Acoount register', '1000.0(deposit)', 'self', '______________', 'Walling', 'Netra Prasad Neupane', 2075000080000),
('Sat Apr 20 20:03:07 2019', 'deposit', '20000', 'Netra Prasad Neupane', '--------', 'Walling', '--------', 2075000080001),
('Sat Apr 20 20:03:53 2019', 'withdraw', '1000', 'Peu Narayan Neupane', '--------', 'Walling', '--------', 2075000080002);

-- --------------------------------------------------------

--
-- Table structure for table `sibjrejf7686_7500033_loan`
--

CREATE TABLE `sibjrejf7686_7500033_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sibjrejf7686_7500033_loan`
--

INSERT INTO `sibjrejf7686_7500033_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sun Mar 10 12:49:00 2019', 'withdraw loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000330000);

-- --------------------------------------------------------

--
-- Table structure for table `sibjrejf_7500032_loan`
--

CREATE TABLE `sibjrejf_7500032_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sibjrejf_7500032_loan`
--

INSERT INTO `sibjrejf_7500032_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sun Mar 10 12:49:00 2019', 'withdraw loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000320000);

-- --------------------------------------------------------

--
-- Table structure for table `sita_207500026`
--

CREATE TABLE `sita_207500026` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sita_207500026`
--

INSERT INTO `sita_207500026` (`date_and_time`, `operation`, `amount`, `performed_by`, `transfer_to`, `branch`, `issued_by`, `transjection_id`) VALUES
('Sat Mar  2 00:08:06 2019', 'Acoount register', '2.0(deposit)', 'self', '______________', 'select', 'Netra Prasad Neupane', 2075000260000);

-- --------------------------------------------------------

--
-- Table structure for table `staff_data`
--

CREATE TABLE `staff_data` (
  `name` varchar(55) NOT NULL,
  `f_name` varchar(55) NOT NULL,
  `m_name` varchar(55) NOT NULL,
  `sex` varchar(55) NOT NULL,
  `dob` date NOT NULL,
  `mobile_no` varchar(55) NOT NULL,
  `email` varchar(55) NOT NULL,
  `id_number` varchar(55) NOT NULL,
  `id_type` varchar(55) NOT NULL,
  `per_address` varchar(55) NOT NULL,
  `tem_address` varchar(55) NOT NULL,
  `education` varchar(55) NOT NULL,
  `position` varchar(55) NOT NULL,
  `username` varchar(55) NOT NULL,
  `password` varchar(555) NOT NULL,
  `image_directory` varchar(55) NOT NULL,
  `branch` varchar(55) NOT NULL,
  `joined_date` date NOT NULL,
  `created_by` varchar(55) NOT NULL,
  `staff_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_data`
--

INSERT INTO `staff_data` (`name`, `f_name`, `m_name`, `sex`, `dob`, `mobile_no`, `email`, `id_number`, `id_type`, `per_address`, `tem_address`, `education`, `position`, `username`, `password`, `image_directory`, `branch`, `joined_date`, `created_by`, `staff_id`) VALUES
('Netra Prasad Neupane', 'Peu narayan Neupane', 'Pema Neupane', 'male', '2055-01-30', '9846626929', 'nimesh.neupane43@gmail.com', '422045/740', 'Citizenship', 'Syangja', 'Pokhara Nepal', 'PHD level', 'Manager', 'netrayvn', 'yvn00001n', 'c:/ddkjfhjkdhf/f', 'Pokhara', '0275-01-14', '', 6930001),
('Sujan', '', '', 'select', '0000-00-00', '45454', '', '', 'select', '', '', 'select', 'Loan officer', 'sujanvn', 'yvn00002s', '', 'select', '2019-03-04', 'Manager', 6930002),
('Sunadjf', '', '', 'select', '0000-00-00', 'dfdf', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-04', 'Manager', 6930003),
('Sukandar', '', '', 'select', '0000-00-00', '4444', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-04', 'Manager', 6930004),
('Sukendardd', '', '', 'select', '0000-00-00', '22323232', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-04', 'Manager', 6930005),
('Suraj', '', '', 'select', '0000-00-00', '894798748', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-04', 'Manager', 6930006),
('Hey', '', '', 'select', '0000-00-00', '11', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-04', 'Manager', 6930007),
('Sujil', 'Dd', 'Kk', 'female', '1951-02-03', 'ddd', 'gdf', 'fdfd', 'driving License', 'syangja', 'pokhara', 'Intermediate level', 'Teller', 'sujilyvn', 'yvn00004s', '', 'Butwal', '2019-03-04', 'Manager', 6930008),
('Sujilllll', '', '', 'select', '0000-00-00', '', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-04', 'Manager', 6930009),
('Sunil', 'M', 'S', 'other', '1952-04-04', 'dhfdlkfj', 'dfdfd', 'sddd', 'Citizenship', 'syandf', 'oijdopfj', 'Bachelor level', 'Teller', 'hariskdf', 'dlfkhjdfldjkf', '///fdfdf', 'Pokhara', '2019-03-04', 'Manager', 6930010),
('', '', '', 'select', '0000-00-00', '', '', '', 'select', '', '', 'select', 'Select', '', '', '', 'select', '2019-03-10', 'Manager', 6930011),
('Dipen Thapa', '', '', 'select', '0000-00-00', '', '', '', 'select', '', '', 'select', 'Select', 'dipenyvn', 'yvn00006d', '', 'select', '2019-03-13', 'Manager', 6930012),
('Nimesh Neupane', 'Peu Neupane', 'Tika Neupane', 'male', '1952-04-03', '66878687897', 'nimkdjfk@gmail.com', '089878876876', 'driving License', 'Syangja', 'Ktm', 'Master level', 'Loan officer', 'nimeshyvd', 'yvd000030n', '', 'Walling', '2019-04-27', 'Manager', 6930013),
('Mukti Dumre', 'M', 'K', 'male', '2052-04-06', '9847557382', 'muktiprasad78@gmail.com', '422047/235', 'Citizenship', 'Syangja', 'Butwal', 'Bachelor level', 'Financial Analyst', 'mdumre', '12345678', '', 'Walling', '2019-07-19', 'Manager', 6930014);

-- --------------------------------------------------------

--
-- Table structure for table `staff_only`
--

CREATE TABLE `staff_only` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `Join_date` date NOT NULL,
  `id_number` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_only`
--

INSERT INTO `staff_only` (`id`, `name`, `username`, `password`, `mobile`, `email`, `position`, `Join_date`, `id_number`, `address`) VALUES
(1, 'Hari Aryal', 'hariyvn', 'yvn00001h', '9846272727', 'hari4@gmail.com', 'Teller', '2070-01-30', '2087/33', 'Kathmandu Nepal'),
(2, 'Netra Prasad Neupane', 'netrayvn', 'yvn00001n', '9846252522', 'netra77@gmail.com', 'Manager', '2073-02-22', '422045/740', 'Syangja');

-- --------------------------------------------------------

--
-- Table structure for table `sunil_dumre_7500026_loan`
--

CREATE TABLE `sunil_dumre_7500026_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sunil_dumre_7500026_loan`
--

INSERT INTO `sunil_dumre_7500026_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 22:15:48 2019', 'get loan', '500000.0', 'self', 'select', 'Netra Prasad Neupane', 75000260000),
('Sat Mar  2 22:16:46 2019', 'loan payment', '1000', 'self', 'select', '--------', 75000260001),
('Sat Mar  2 22:20:47 2019', 'loan payment', '10000', 'self', 'select', '--------', 75000260002),
('Sat Mar  2 22:21:40 2019', 'loan payment', '1000', 'netra', 'select', '--------', 75000260003),
('Sat Mar  2 22:23:56 2019', 'loan payment', '10000', 'hari', 'select', '--------', 75000260004),
('Sat Mar  2 22:28:15 2019', 'loan payment', '1000', 'self', 'select', '--------', 75000260005),
('Sat Mar  2 22:29:58 2019', 'loan payment', '1000', 'self', 'select', '--------', 75000260006),
('Sat Mar  2 22:32:56 2019', 'loan payment', '10000', 'self', 'select', '--------', 75000260007),
('Sun Mar  3 14:17:00 2019', 'loan payment', '10000', 'self', 'select', '--------', 75000260008),
('Sun Mar  3 21:49:22 2019', 'loan payment', '1000', 'self', 'select', '--------', 75000260009),
('Sun Mar 10 18:08:46 2019', 'loan payment', '1000', 'self', 'select', '--------', 75000260010);

-- --------------------------------------------------------

--
-- Table structure for table `sunil_sign_7500031_loan`
--

CREATE TABLE `sunil_sign_7500031_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sunil_sign_7500031_loan`
--

INSERT INTO `sunil_sign_7500031_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sun Mar 10 12:47:01 2019', 'withdraw loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000310000);

-- --------------------------------------------------------

--
-- Table structure for table `suraj_7500009_loan`
--

CREATE TABLE `suraj_7500009_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `suraj_7500010_loan`
--

CREATE TABLE `suraj_7500010_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `suraj_7500011_loan`
--

CREATE TABLE `suraj_7500011_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `suraj_khanal_7500027_loan`
--

CREATE TABLE `suraj_khanal_7500027_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `suraj_khanal_7500027_loan`
--

INSERT INTO `suraj_khanal_7500027_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Tue Mar  5 18:40:23 2019', 'get loan', '2000000.0', 'self', 'select', 'Netra Prasad Neupane', 75000270000);

-- --------------------------------------------------------

--
-- Table structure for table `yogesh_207500020`
--

CREATE TABLE `yogesh_207500020` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `transfer_to` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `transjection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `_7500014_loan`
--

CREATE TABLE `_7500014_loan` (
  `date_and_time` varchar(255) DEFAULT NULL,
  `operation` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `performed_by` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `issued_by` varchar(255) DEFAULT NULL,
  `loan_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `_7500014_loan`
--

INSERT INTO `_7500014_loan` (`date_and_time`, `operation`, `amount`, `performed_by`, `branch`, `issued_by`, `loan_id`) VALUES
('Sat Mar  2 14:43:20 2019', 'get loan', '0.0', 'self', 'select', 'Netra Prasad Neupane', 75000140000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barak_obama_7500020_loan`
--
ALTER TABLE `barak_obama_7500020_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `bhuwan_207500004`
--
ALTER TABLE `bhuwan_207500004`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `binayak_207500022`
--
ALTER TABLE `binayak_207500022`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `customer_data`
--
ALTER TABLE `customer_data`
  ADD PRIMARY KEY (`account_num`);

--
-- Indexes for table `dipen_thapa_7500034_loan`
--
ALTER TABLE `dipen_thapa_7500034_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `dipen_thapa_207500006`
--
ALTER TABLE `dipen_thapa_207500006`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `dipesh_gautam_207500011`
--
ALTER TABLE `dipesh_gautam_207500011`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `donald_trump_7500019_loan`
--
ALTER TABLE `donald_trump_7500019_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `hakdjkhsjkfhdjkf_7500023_loan`
--
ALTER TABLE `hakdjkhsjkfhdjkf_7500023_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `hari_nepal_207500005`
--
ALTER TABLE `hari_nepal_207500005`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `harooooo_7500017_loan`
--
ALTER TABLE `harooooo_7500017_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `hekjfkdjfd_7500030_loan`
--
ALTER TABLE `hekjfkdjfd_7500030_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `hellowedsf_7500024_loan`
--
ALTER TABLE `hellowedsf_7500024_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `hellowr_7500018_loan`
--
ALTER TABLE `hellowr_7500018_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `hhhhkfg_7500029_loan`
--
ALTER TABLE `hhhhkfg_7500029_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `janak_207500025`
--
ALTER TABLE `janak_207500025`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `jenny_207500018`
--
ALTER TABLE `jenny_207500018`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `jhgjkl_7500015_loan`
--
ALTER TABLE `jhgjkl_7500015_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `jnaak_207500023`
--
ALTER TABLE `jnaak_207500023`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `keshav_bhusal_7500028_loan`
--
ALTER TABLE `keshav_bhusal_7500028_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `keshav_bhusal_207500019`
--
ALTER TABLE `keshav_bhusal_207500019`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `keshav_bh_207500028`
--
ALTER TABLE `keshav_bh_207500028`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `kjkjdkfdjfdkfb_7500022_loan`
--
ALTER TABLE `kjkjdkfdjfdkfb_7500022_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `loan_data`
--
ALTER TABLE `loan_data`
  ADD PRIMARY KEY (`loan_acc_no`);

--
-- Indexes for table `mahesh_7500025_loan`
--
ALTER TABLE `mahesh_7500025_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `mukti_7500036_loan`
--
ALTER TABLE `mukti_7500036_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `mukti_prasad_dumre_207500012`
--
ALTER TABLE `mukti_prasad_dumre_207500012`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `naran_207500024`
--
ALTER TABLE `naran_207500024`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `naran_neupane_207500009`
--
ALTER TABLE `naran_neupane_207500009`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `netra_207500004`
--
ALTER TABLE `netra_207500004`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `netra_pr_207500003`
--
ALTER TABLE `netra_pr_207500003`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `nimesh_neupane_7500035_loan`
--
ALTER TABLE `nimesh_neupane_7500035_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `nimesh_neupane_207500010`
--
ALTER TABLE `nimesh_neupane_207500010`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `niraj_yogi_207500007`
--
ALTER TABLE `niraj_yogi_207500007`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `oihjk_7500013_loan`
--
ALTER TABLE `oihjk_7500013_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `paras_207500021`
--
ALTER TABLE `paras_207500021`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `rabindara_7500012_loan`
--
ALTER TABLE `rabindara_7500012_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `radhika_neupane_207500008`
--
ALTER TABLE `radhika_neupane_207500008`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `sibjrejf7686_7500033_loan`
--
ALTER TABLE `sibjrejf7686_7500033_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `sibjrejf_7500032_loan`
--
ALTER TABLE `sibjrejf_7500032_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `sita_207500026`
--
ALTER TABLE `sita_207500026`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `staff_data`
--
ALTER TABLE `staff_data`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `staff_only`
--
ALTER TABLE `staff_only`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sunil_dumre_7500026_loan`
--
ALTER TABLE `sunil_dumre_7500026_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `sunil_sign_7500031_loan`
--
ALTER TABLE `sunil_sign_7500031_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `suraj_7500009_loan`
--
ALTER TABLE `suraj_7500009_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `suraj_7500010_loan`
--
ALTER TABLE `suraj_7500010_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `suraj_7500011_loan`
--
ALTER TABLE `suraj_7500011_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `suraj_khanal_7500027_loan`
--
ALTER TABLE `suraj_khanal_7500027_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- Indexes for table `yogesh_207500020`
--
ALTER TABLE `yogesh_207500020`
  ADD PRIMARY KEY (`transjection_id`);

--
-- Indexes for table `_7500014_loan`
--
ALTER TABLE `_7500014_loan`
  ADD PRIMARY KEY (`loan_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barak_obama_7500020_loan`
--
ALTER TABLE `barak_obama_7500020_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `bhuwan_207500004`
--
ALTER TABLE `bhuwan_207500004`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `binayak_207500022`
--
ALTER TABLE `binayak_207500022`
  MODIFY `transjection_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer_data`
--
ALTER TABLE `customer_data`
  MODIFY `account_num` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=207500013;

--
-- AUTO_INCREMENT for table `dipen_thapa_7500034_loan`
--
ALTER TABLE `dipen_thapa_7500034_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `dipen_thapa_207500006`
--
ALTER TABLE `dipen_thapa_207500006`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `dipesh_gautam_207500011`
--
ALTER TABLE `dipesh_gautam_207500011`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `donald_trump_7500019_loan`
--
ALTER TABLE `donald_trump_7500019_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `hakdjkhsjkfhdjkf_7500023_loan`
--
ALTER TABLE `hakdjkhsjkfhdjkf_7500023_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `hari_nepal_207500005`
--
ALTER TABLE `hari_nepal_207500005`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `harooooo_7500017_loan`
--
ALTER TABLE `harooooo_7500017_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `hekjfkdjfd_7500030_loan`
--
ALTER TABLE `hekjfkdjfd_7500030_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `hellowedsf_7500024_loan`
--
ALTER TABLE `hellowedsf_7500024_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `hellowr_7500018_loan`
--
ALTER TABLE `hellowr_7500018_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `hhhhkfg_7500029_loan`
--
ALTER TABLE `hhhhkfg_7500029_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `janak_207500025`
--
ALTER TABLE `janak_207500025`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `jenny_207500018`
--
ALTER TABLE `jenny_207500018`
  MODIFY `transjection_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jhgjkl_7500015_loan`
--
ALTER TABLE `jhgjkl_7500015_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `jnaak_207500023`
--
ALTER TABLE `jnaak_207500023`
  MODIFY `transjection_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `keshav_bhusal_7500028_loan`
--
ALTER TABLE `keshav_bhusal_7500028_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `keshav_bhusal_207500019`
--
ALTER TABLE `keshav_bhusal_207500019`
  MODIFY `transjection_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `keshav_bh_207500028`
--
ALTER TABLE `keshav_bh_207500028`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `kjkjdkfdjfdkfb_7500022_loan`
--
ALTER TABLE `kjkjdkfdjfdkfb_7500022_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `loan_data`
--
ALTER TABLE `loan_data`
  MODIFY `loan_acc_no` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7500037;

--
-- AUTO_INCREMENT for table `mahesh_7500025_loan`
--
ALTER TABLE `mahesh_7500025_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `mukti_7500036_loan`
--
ALTER TABLE `mukti_7500036_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `mukti_prasad_dumre_207500012`
--
ALTER TABLE `mukti_prasad_dumre_207500012`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `naran_207500024`
--
ALTER TABLE `naran_207500024`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `naran_neupane_207500009`
--
ALTER TABLE `naran_neupane_207500009`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `netra_207500004`
--
ALTER TABLE `netra_207500004`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2075000412;

--
-- AUTO_INCREMENT for table `netra_pr_207500003`
--
ALTER TABLE `netra_pr_207500003`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `nimesh_neupane_7500035_loan`
--
ALTER TABLE `nimesh_neupane_7500035_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `nimesh_neupane_207500010`
--
ALTER TABLE `nimesh_neupane_207500010`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `niraj_yogi_207500007`
--
ALTER TABLE `niraj_yogi_207500007`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `oihjk_7500013_loan`
--
ALTER TABLE `oihjk_7500013_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `paras_207500021`
--
ALTER TABLE `paras_207500021`
  MODIFY `transjection_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rabindara_7500012_loan`
--
ALTER TABLE `rabindara_7500012_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `radhika_neupane_207500008`
--
ALTER TABLE `radhika_neupane_207500008`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `sibjrejf7686_7500033_loan`
--
ALTER TABLE `sibjrejf7686_7500033_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `sibjrejf_7500032_loan`
--
ALTER TABLE `sibjrejf_7500032_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `sita_207500026`
--
ALTER TABLE `sita_207500026`
  MODIFY `transjection_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `staff_data`
--
ALTER TABLE `staff_data`
  MODIFY `staff_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6930015;

--
-- AUTO_INCREMENT for table `staff_only`
--
ALTER TABLE `staff_only`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sunil_dumre_7500026_loan`
--
ALTER TABLE `sunil_dumre_7500026_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `sunil_sign_7500031_loan`
--
ALTER TABLE `sunil_sign_7500031_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `suraj_7500009_loan`
--
ALTER TABLE `suraj_7500009_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suraj_7500010_loan`
--
ALTER TABLE `suraj_7500010_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suraj_7500011_loan`
--
ALTER TABLE `suraj_7500011_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suraj_khanal_7500027_loan`
--
ALTER TABLE `suraj_khanal_7500027_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;

--
-- AUTO_INCREMENT for table `yogesh_207500020`
--
ALTER TABLE `yogesh_207500020`
  MODIFY `transjection_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `_7500014_loan`
--
ALTER TABLE `_7500014_loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483647;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
