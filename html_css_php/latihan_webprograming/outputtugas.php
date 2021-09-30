<!DOCTYPE html>
<html>
<head>
	<title>Output Tugas 7</title>
</head>
<body>
	<?php
	$nilai1 =$_POST["nilai1"];
	$nilai2 =$_POST["nilai2"];
	$rumus=$_POST["rumus"];
	?>
	<h1>HASIL HITUNGAN RUMUS</h1>
	<br>
	Nilai a Adalah = <?php echo $nilai1; ?><br>
	Nilai b Adalah = <?= $nilai2 ?><br>
	Rumus yang dipilih adalah = <?php echo $rumus; ?><br>
	<?php
	if ($rumus == "segitiga") {
		$hasil = 1/2 * $nilai1*$nilai2;
	}
	elseif ($rumus == "persegipanjang") {
		$hasil = $nilai1 * $nilai2;
	}
	
	?>
	Hasil perhitungan Rumus = <?php echo $hasil; ?>

</body>
</html>