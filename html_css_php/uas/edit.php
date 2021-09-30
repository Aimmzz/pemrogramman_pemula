<?php 
include("koneksi.php");
$n=$_POST['n'];
$u=$_POST['u'];
$w=$_POST['w'];
$s=$_POST['s'];
$id=$_POST['id'];
if($send=mysqli_query($koneksi_db,"UPDATE tbl_baju SET nama='$n', ukuran='$u',warna='$w',stok='$s' WHERE id_baju='$id'")){
	header("location:index.php");}
else {
	echo "Error: " . $send . "<br>" . mysqli_error($koneksi_db);
}

?>