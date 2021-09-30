<?php 
session_start();
include("koneksi.php");
$p=$_POST['p'];
$check=mysqli_query($koneksi_db,"SELECT * FROM user WHERE username='$_POST[u]' AND password='$p'");
$result=mysqli_fetch_array($check);
if(mysqli_num_rows($check)==0){
	echo '<script language=JavaScript>alert("Login Gagal");location.href="index.php"</script>';
}else{
	$_SESSION['masuk']=$result['username']; //$_SESSION = variabel global
	header("location:index.php");}
?>