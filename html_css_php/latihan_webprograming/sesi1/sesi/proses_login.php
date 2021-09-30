<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style>
		.container {
           display: flex;
 
           /* Properti lainnya */
           width: 800px;
           height: 250px;
           background-color: #11C5C6;
           border: 2px solid black;
           padding: 20px;
           border-radius: 10px;
           margin: 0 auto;
       }
       .box {
           flex-grow: 1;
 
           /* properti lainnya */
           background-color: #FBDD1C;
           margin: 5px;
           border: 2px solid black;
           border-radius: 10px;
       }
	</style>
</head>
<body>
	<div class="container">
	<div class="box">
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
</div>
</div>

</body>
</html>