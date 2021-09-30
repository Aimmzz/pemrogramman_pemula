<?php 
include("koneksi.php");
//Rename biar gak ribet di bawah, form method POST = ambil nilainya pakai $_POST, GET= $_GET
$n=$_POST['n'];
$u=$_POST['u'];
$w=$_POST['w'];
$s=$_POST['s'];
if($send=mysqli_query($koneksi_db,"INSERT INTO tbl_baju(nama,ukuran,warna,stok) values('$n','$u','$w','$s');")){
	//kalau query SQL berhasil, redirect ke homepage
	header("location:index.php");}
else {
	//kalau gagal tampilkan error
	echo "Error: " . $send . "<br>" . mysqli_error($koneksi_db);
}

?>