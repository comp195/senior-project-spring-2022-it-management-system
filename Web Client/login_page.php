<?php
	//Automatically redirect to main form page if user is already logged in
	session_start();
	console_log("Testing");
	$str = "test";
	console_log($str);
	if (isset($_SESSION["logged_in"]) && $_SESSION["logged_in"] === true
		&& isset($_SESSION["employee_id"]) && isset($_SESSION["first_name"]) && isset($_SESSION["last_name"]))
	{		
		printf($_SESSION["employee_id"]);
		printf($_SESSION["first_name"]);

		$eid = $_SESSION["employee_id"];
		$f_name = $_SESSION["first_name"];
		$l_name = $_SESSION["last_name"];
		header("location: Form.php?eid=".$eid."&f_name=".$f_name."&l_name=".$l_name);
		//header("location: login_verification.php?eid=".$eid."&f_name=".$f_name."&l_name=".$l_name);
		exit;
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


<html>
	<head>
		<title>Ticketing Login</title>
		<h1>Welcome to A.V.D. Ticketing System</h1>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
		<style>
			h1
			{
				font-family: Georgia, serif;				
				font-size: 300%;
				color: DarkCyan;
				white-space: nowrap;
				text-align: center;
			}
			
			body
			{
				font-family: Georgia, serif;
				background-color: Bisque;
			}						
			
			#container
			{
				text-align: center;    
			}

			#container .form-container
			{
				display: inline-block;
			}

			#container form
			{
				background: #eee;
				background-color: LightBlue;
				border: 4px solid DarkSlateGray;
				border-radius: 20px;
				display: flex;
				flex-direction: row;
				flex-wrap: nowrap;
				padding: 20px;
			}

			#container form .column
			{
				display: flex;
				flex-direction: column;
				flex-wrap: nowrap;
			}

			#container form .column label
			{
				padding: 2px;
				text-align: right;
				margin-bottom: 26px;
				margin-left: 50px;
			}

			#container form .column input, 
			#container form .column textarea
			{
				align-self: flex-start;
				height:20px;
				width: 200px;
				margin-bottom: 23px;
				margin-left: 23px;
			}
			
			.login_button
			{
				display: block;
				height: 42px;
				width: 130px;
				/* border: 4px solid LightGreen; */
				border-radius: 20px;
				font-family: verdana;
				font-size: 170%;
				background-color: Turquoise;
				color: MidnightBlue;
				margin-top:15px;
				margin-left: 40px;
				margin-right: 40px;
				position: relative;				
			}
			
			.login_button:hover
			{
				background-color: DarkCyan;
			}
			
			p
			{
				font-size: 20px;
			}
		
			label
			{
				font-size: 20px;
			}			
		</style>
	</head>
	
	<body>
		<div id="container">
			<div class="form-container">
				<p>Enter your login credentials to proceed to the submission form.</p>
				<form id="login_form" action="../dashboard/login_verification.php" method="POST">
					<div class="column">
						<label for="username" id="username_label">Username</label>
						<label for="password" id="password_label">Password</label>						
					</div>    
					<div class="column">
						<input type="text" id="username" name="username" class="form-control <?php echo (!empty($username_error)) ? 'is-invalid' : '';?>" style="margin-top:10px;" required/>					
						<span class="invalid-feedback"><?php echo $username_err; ?></span>
						
						<input type="password" id="password" name="password" class="form-control" style="margin-top:17px;" required/>
					</div>							
					<!-- Log In Button -->
					<input type="submit" name="login_button" id="login_button" value="Log In" class="login_button"/>
				</form>
			</div>
		</div>					
	</body>
</html>