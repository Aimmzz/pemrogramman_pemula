<?php            
session_start();   
session_unset($_SESSION['logged_in']);
session_destroy();  
	header("Location: index.php");   
?> 