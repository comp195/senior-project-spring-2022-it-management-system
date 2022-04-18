<?php
	require ("../db_config.php");
	
	session_start();
	
	//testing page link from login page to main submission page
	//UNCOMMENT THIS TO TEST
	// $_SESSION["logged_in"] = true;
		
	if (isset($_SESSION["logged_in"]) && $_SESSION["logged_in"] === true)
	{
		$str = "CHECK";
		console_log($str);
		header("location: Form.html"); 
		exit;
	}
			
	$username = $_POST["username"];
	$password = $_POST["password"];
	
	if ($_SERVER["REQUEST_METHOD"] == "POST")
	{			
		$sql_query = "SELECT password FROM Login_Credentials WHERE username = ?";
		
		//Use prepared statement
		$stmt = mysqli_prepare($connection, $sql_query);
		if ($stmt)
		{			
			$username_param = $username;
			mysqli_stmt_bind_param($stmt, "s", $username_param);
			
			if (mysqli_stmt_execute($stmt))
			{					
				//NOTE: result is stored locally
				mysqli_stmt_store_result($stmt);																			
				
				//Determine if username exists
				if (mysqli_stmt_num_rows($stmt) == 1)
				{																		
					mysqli_stmt_bind_result($stmt, $password_hash);
					
					//if data has been fetched successfully
					if (mysqli_stmt_fetch($stmt))
					{
						$password_is_valid = password_verify($password, $password_hash);
						if ($password_is_valid)
						{								
							session_start();
							
							//Use session variables to handle case where user is already logged in
							$_SESSION["logged_in"] = true;
							
							//Send user to form page
							header("location: Form.html");
						}
						else
						{
							$str = "1Username or password is incorrect! Please re-enter your credentials...";
							console_log($str);
							header("location: login_page.html");
						}
					}						
				}
				else
				{						
					$str = "2Username or password is incorrect! Please re-enter your credentials...";
					console_log($str);
					header("location: login_page.html");
				}														
			}
			else
			{
				$str = "Error occurred...";
				console_log($str);
				header("location: login_page.html");
			}
		}			
	}
	
	//Used for console output testing
	function console_log($output, $with_script = true)
	{
		$js = 'console.log(' . json_encode($output, JSON_HEX_TAG) . ');';
		if ($with_script)
		{
			$js = '<script>' . $js . '</script>';
		}
		echo $js;
	}
?>