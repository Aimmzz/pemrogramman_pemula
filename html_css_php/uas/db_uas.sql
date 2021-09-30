-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2021 at 10:55 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_uas`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_baju`
--

CREATE TABLE `tbl_baju` (
  `id_baju` int(10) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `ukuran` varchar(10) NOT NULL,
  `warna` varchar(10) NOT NULL,
  `stok` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_baju`
--

INSERT INTO `tbl_baju` (`id_baju`, `nama`, `ukuran`, `warna`, `stok`) VALUES
(1, 'Saa', 'XL', 'Red', 5),
(2, '1', 'S', '2', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_baju`
--
ALTER TABLE `tbl_baju`
  ADD PRIMARY KEY (`id_baju`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_baju`
--
ALTER TABLE `tbl_baju`
  MODIFY `id_baju` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
