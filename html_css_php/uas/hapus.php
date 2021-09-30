<?php 
include("koneksi.php");

$id=$_GET['id'];
if($send=mysqli_query($koneksi_db,"DELETE FROM tbl_baju WHERE id_baju='$id'")){
	header("location:index.php");}
else {
	echo "Error: " . $send . "<br>" . mysqli_error($koneksi_db);
}

?>