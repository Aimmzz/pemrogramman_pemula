<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style>
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
	<div class="box">
		<div style="text-align: center;">
	<?php
session_start();
include "koneksi.php";
if(isset($_SESSION['masuk'])){ //cek apakah variabel $_SESSION['masuk'] sudah terdaftar/terisi
echo"<h2>Selamat Datang $_SESSION[masuk]</h2>
<a href=logout.php>Keluar</a>";}
else{ //Kalau belum, tampilkan form login
echo"
<link href=asset/css/bootstrap.min.css rel=stylesheet>
	<title>Sign In</title>
		<body>

			<div align=center>
				<form action=proses_login.php method=post >
					<h1>Sign In</h1>
					<table height=100px>
						<tbody>
					<tr><td>Username</td>
						<td>: <input name=u type=text placeholder=\"Enter your username\"></td>
					</tr>
					<tr><td>Password</td>
						<td>: <input name=p type=password placeholder=Password></td>
					</tr>
					<tr><td colspan=2 align=right>
							<input value=\"Sign In\" type=submit class=\"btn btn-primary\">
					</table>
				</form>
			</div>
		</body>	
";}
					?>
				</div>
				</div>

</body>
</html>
