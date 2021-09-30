<!DOCTYPE html>
<html>
<head>
	<title>FORM KOMENTAR</title>
</head>
<body>
	<h1>BUKU TAMU</h1>
	<br>
	Komentar dan Saran anda sangant kami butuhkan<br>
	untuk meningkatkan kualitas situs kami<br>
	<hr>
	<p><form action="tampilkomentar.php" method="POST">
		Nama Anda &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;	: <input type="text" name="nama" size="50"><br>
		Email Anda &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; : <input type="text" name="email" size="50"><br>
		Komentar Anda	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;: <textarea rows ="6" name="komen" cols="50" ></textarea><br>
		<input type="submit" value="Kirim"> <input type="reset" value="Batal">

	</form></p>

</body>
</html>