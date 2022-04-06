<?php
	require ("db_config.php");
	
	session_start();
	
	//testing page link from login page to main submission page
	$_SESSION["logged_in"] = true;
		
	if (isset($_SESSION["logged_in"]) && $_SESSION["logged_in"] === true)
	{
		header("location: Form.html"); 
		exit;
	}
?>