<!DOCTYPE html>
<html>
<head>
	<title>Form Registrasi</title>
</head>
<body>
	<h1>Form Registrasi</h1>
	<br>
	<p><form action="dataregistrasi.php" method="POST">
	Isi Data Dibawah ini :<br>
	Nama &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; <input type="text" name="nama" size="40"><br>
	Alamat  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; <textarea rows ="6" name="alamat" cols="52"></textarea><br>
	Tempat Lahir &emsp;&emsp;&emsp;&emsp;&emsp; <input type="text" name="tempat" size="40"><br>
	Tanggal Lahir   &ensp;&emsp;&emsp;&emsp;&ensp;&ensp;&ensp; <input type="text" name="tanggal" size="40"><br>
	Jenis kelamin &emsp;&emsp;&emsp;&emsp;&ensp; <input type="radio" name="jeniskel" value="Laki-Laki">Laki-Laki
				  <input type="radio" name="jeniskel" value="Perempuan">Perempuan<br>
	Pendidikan &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp; <select name="pendidikan">
		<option value="Pilih">Pilih</option>
		<option value="D3">D3</option>
		<option value="S1">S1</option>
		<option value="S2">S2</option>
	</select><br>
	<br>
	<br>
	<input type="submit" value="submit"> <input type="reset" value="cancel"></form></p>

</body>
</html>