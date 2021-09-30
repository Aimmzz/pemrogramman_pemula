<!DOCTYPE html>
<html>
<head>
	<title>Input Tugas 7</title>
</head>
<body>
	<form action="outputtugas.php" method="POST">
	<table border = "1" cellspacing="3" cellpadding="10">
		<tr>
			<td>Nilai 1</td>
			<td>
				<input type="text" name="nilai1">
			</td>
		</tr>
		<tr>
			<td>Nilai 2</td>
			<td>
				<input type="text" name="nilai2">
			</td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="radio" name="rumus" value="segitiga">segitiga<br>
				<input type="radio" name="rumus" value="persegipanjang">Persegi Panjang
			</td>
		</tr>
	</table><br>
	<input type="submit" value="Hitung"> <input type="reset" value="Batal">
</form>

</body>
</html>