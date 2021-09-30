<!DOCTYPE html>
<html>
<head>
	<title>Data Registrasi</title>
</head>
<body>
	<?php
	$nama=$_POST["nama"];
	$alamat=$_POST["alamat"];
	$tempat=$_POST["tempat"];
	$tanggal=$_POST["tanggal"];
	$jeniskel=$_POST["jeniskel"];
	$pendidikan=$_POST["pendidikan"]
	?>
	<h1>Data Registrasi</h1>
	<br>
	<table border = "1" cellspacing="3" cellpadding="10">
		<tr>
			<td>Nama</td>
			<td> <?php echo $nama; ?> </td>
		</tr>
		<tr>
			<td>Alamat</td>
			<td> <?php echo $alamat; ?> </td>
		</tr>
		<tr>
			<td>Tempat Lahir</td>
			<td> <?php echo $tempat; ?> </td>
		</tr>
		<tr>
			<td>Tanggal Lahir</td>
			<td> <?php echo $tanggal; ?> </td>
		</tr>
		<tr>
			<td>Jenis Kelamin</td>
			<td> <?php echo $jeniskel; ?> </td>
		</tr>
		<tr>
			<td>Pendidikan</td>
			<td> <?php echo $pendidikan?> </td>
		</tr>
		<br>
	</table>
	<a href="formregistrasi.php">BACK TO HOME</a>

</body>
</html>