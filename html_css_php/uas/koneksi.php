<?php
$koneksi_db=mysqli_connect('localhost', 'root', '');
if (!$koneksi_db){die("Koneksi ke database gagal : " . mysqli_connect_error());}
$db_pilih = mysqli_select_db($koneksi_db,'db_uas'); //'sesi' = nama database 
if(!$db_pilih){die("Pemilihan database gagal : " . mysqli_error($koneksi_db));}
?>