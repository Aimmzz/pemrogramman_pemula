<!DOCTYPE html>
<html>
<head>
	<title>Contoh Percabangan if</title>
</head>
<body>
	<h3>Percabangan if Majmuk(if,elseif,else)</h3>
	<?php
	$nilai = 90;
	if(($nilai >= 0) && ($nilai <=40))
	 { $grade ="E";
		
	}
	elseif (($nilai >=40) && ($nilai <=60))
	{
		$grade = "D";
	}
	elseif (($nilai >=60) && ($nilai <=75))
	{
		$grade = "C";
	}
	elseif (($nilai >=75) && ($nilai <=85))
	{
		$grade = "B";
	}
	elseif (($nilai >=85) && ($nilai <=100))
	{
		$grade = "A";
	}
	else
	{
		$grade = "error";
	}

	echo "Anda mendapatkan nialai $nilai jadi di konpersi menjadi grade $grade";
	?>
	<h3>percabangan switch case</h3>
	<?php
	$angka = 6;
	switch ($angka) {
		case '0': $terbilang = "nol";break;
		case '1': $terbilang = "satu";break;
		case '2': $terbilang = "dua";break;
		case '3': $terbilang = "tiga";break;
		case '4': $terbilang = "empat";break;
		case '5': $terbilang = "lima";break;
		case '6': $terbilang = "enam";break;
		case '7': $terbilang = "tujuh";break;
		case '8': $terbilang = "delapan";break;
		case '9': $terbilang = "sembilan";break;
		
		default: $terbilang = "error"; break;
	}
	echo "Bentuk terbilang dari angka $angka yaitu $terbilang";
	?>

</body>
</html>