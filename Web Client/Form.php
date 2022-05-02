<?php
	if (isset($_POST['link']))
	{
		//Needed to allow my_tickets.php to retrieve EID value (to send to ticket_db_retrieval.php)
		ob_start();
		session_start();
		$_SESSION['eid'] = $_GET['eid'];			

		$eid = $_GET['eid'];
		$f_name = $_GET['f_name'];
		$l_name = $_GET['l_name'];
		/*
		console_log($eid);	
		console_log($f_name);
		console_log($l_name);
		*/
		//Send values to My Tickets page as temporary storage
		header("location: my_tickets.php?eid=".$eid."&f_name=".$f_name."&l_name=".$l_name);
	}

	//Code to be run if "Log out" is clicked	
	if (isset($_POST['logout_link']))
	{
		session_start();
		session_destroy();
		header("location: login_page.php");
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

<!DOCTYPE html>
<html>
	<head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
		
		<title>Web Form</title>
		<h1>Ticket Submission Form</h1>
		<style>
			h1
			{
				font-family: Georgia, serif;
				font-size: 300%;
				text-align: center;
			}

			body
			{
				font-family: Georgia, serif;
				background-color: lightsteelblue;
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
				margin-right: 25px;
			}

			#container form .column input, 
			#container form .column textarea
			{
				align-self: flex-start;
				height:20px;
				width: 200px;
				margin-bottom: 23px;
			}
						
			label
			{
				display: block;
				font-size: 18px;
			}				
			
			.submit_button
			{
				display: block;
				height: 60px;
				width: 150px;
				/* border: 4px solid LightGreen; */
				border-radius: 20px;
				font-family: verdana;
				font-size: 170%;
				background-color: LightGreen;
				color: MidnightBlue;
				position: relative;				
				top: 50%;
				left: 50%;
				transform: translate(-50%, 50%);				
				
			}

			.submit_button:hover
			{
				background-color: DarkCyan;
			}
			
			.asterisk
			{
				color: red;
			}

			.hidden
			{
				display: none;
			}		

			@keyframes spinner
			{
				0%
				{
					transform: translate3d(-50%, -50%, 0) rotate(0deg);
				}
				100%
				{
					transform: translate3d(-50%, -50%, 0) rotate(360deg);
				}
			}	

			.loading_spinner::before
			{
				animation: 1s linear infinite spinner;
				animation-play-state: inherit;
				border: solid 7px Brown;
				border-bottom-color: Bisque;
				border-radius: 50%;
				content: "";
				height: 40px;
				width: 40px;
				position: relative;
				top: 65.5%;
				left: 62%;
				transform: translate3d(-50%, -50%, 0);
				will-change: transform;
				display: block;
			}
	
			#wrapper
			{
				margin-left: auto;
				margin-right: auto;
				width: 1000px;
			}
		</style>
	</head>
	
	<body>
		<div id="wrapper">
			
			<!-- NO LONGER USING -->
			<!-- <a href="../dashboard/my_tickets.html">View my tickets</a> -->

			<!-- Link to 'My Tickets' page -->
			<form id="temp_form" method="post" action="<?php $_SERVER['PHP_SELF']?>" style="display:inline;">
				<input type="hidden" name="link">
				<a href="#" onclick="document.getElementById('temp_form').submit();">View my tickets</a>			
			</form>

			<!-- Link to Login page (logout link) -->
			<form id="logout_form" method="post" action="<?php $_SERVER['PHP_SELF']?>" style="display:inline; float:right;">
				<input type="hidden" name="logout_link">
				<a href="#" onclick="document.getElementById('logout_form').submit();">Log out</a>
			</form>		
			<!-- <a style="float:right; display:inline;" href="../dashboard/login_page.php">Log out</a> -->


			<div id="container">
				<div class="form-container">
					<form id="form1">
						<div class="column">
							<label for="eid" id="eid_label">Employee ID</label>
							<label for="f_name" id="f_name_label">First Name</label>
							<label for="l_name" id="l_name_label">Last Name</label>
							<label for="equipment_id">Associated Equipment ID</label>						
							<label for="short_description" id="short_description_label" style="margin-top:6px; margin-bottom:66px;">Short Description</label>
							<label for="long_description" id="long_description_label">Long Description</label>
						</div>
						<div class="column">
							<input type="text" name="eid" id="eid" class="form-control" style="width: 240px; margin-top:8px; margin-bottom:37px;" value="<?php echo $_GET['eid']; ?>" readonly/>
							<input type="text" name="f_name" id="f_name" class="form-control" style="width: 240px; margin-bottom:38px;" value="<?php echo $_GET['f_name']; ?>" readonly/>
							<input type="text" name="l_name" id="l_name" class="form-control" style="width: 240px; margin-bottom:37px;" value="<?php echo $_GET['l_name']; ?>" readonly/>
							<input type="text" name="equipment_id" id="equipment_id" class="form-control" style="width: 240px; margin-bottom:37px;"/>
							<textarea name="short_description" id="short_description" class="form-control" style="width:310px; height:70px; resize:none;"></textarea>
							<textarea name="long_description" id="long_description" class="form-control" style="width:310px; height:160px; resize:none;"></textarea>
						</div>
					</form>
				</div>
			</div>

			<form id="form2" style="text-align:center;" enctype="multipart/form-data">			
				<!-- Dropdown List for Ticket Category -->
				<label for="categories" style="text-align:center; margin-top:30px;">Ticket Category:</label>
				<div style="text-align:center;">
					<select id="categories" name="categories">
						<option value="New equipment request">New Equipment Request</option>
						<option value="Damaged equipment">Damaged Equipment</option>
						<option value="Equipment replacement">Equipment Replacement</option>
						<option value="Equipment troubleshooting">Equipment Troubleshooting</option>
						<option value="Equipment setup">Equipment Setup</option>
						<option value="Software issue">Software Issue</option>
					</select>
				</div>

				<!-- Dropdown List for Issue Scope -->
				<label for="scope" style="text-align:center; margin-top:30px;">Issue Scope:</label>
				<div style="text-align:center;">
					<select id="scope" name="scope">
						<option value="Single User">Single User</option>
						<option value="Team">Team</option>
						<option value="Departmental">Departmental</option>
					</select>
				</div>

				<!-- File submit button for optional image -->
				<label for="image_file" style="margin-top:30px;">Image Attachment</label>
				<input type="file" id="image_file" name="image_file" style="margin-left:127px;">
				

				<!-- Submit Button -->
				<input type="button" name="submit_button" id="submit_button" value="Submit" class="submit_button"/>
				
				<!-- Loading Spinner -->
				<div id="spinner" class="loading_spinner hidden"></div>

				<!-- Response text -->
				<div id="response" style="color:crimson; margin-top:-54px; text-align:center"></div>
			</form>							
		</div>
	</body>
</html>

<!-- Javascript -->
<script>
	$(document).ready(function()
	{
		//Automatically check login status (needed to automatically log out in other tabs if user logs out in one tab)
		var status_check_interval = 2000;
		window.setInterval(function()
		{
			$.get("login_status_check.php", function(data)
			{
				if (!data)
				{
					window.location = "login_page.php";
				}
			});
		}, status_check_interval);		
	
		display_loading_spinner();
		hide_loading_spinner();
		$('#submit_button').click(function()
		{
			//Confirm that all fields are filled
			var e_id = $('#eid').val();
			var f_name = $('#f_name').val();
			var l_name = $('#l_name').val();
			var short_description = $('#short_description').val();			
			var long_description = $('#long_description').val();
			var	equipment_id = $('#equipment_id').val();
			
			if (e_id == "" || f_name == "" || l_name == "" || short_description == "" || long_description == "")
			{
				$('#response').html('<span>Check the required fields (<span class=asterisk>*</span>)!</span>');
				var eid_label = document.getElementById('eid_label');
				eid_label.innerHTML = "Employee ID <span class=asterisk>*</span>";
				var f_name_label = document.getElementById('f_name_label');
				f_name_label.innerHTML = "First Name <span class=asterisk>*</span>";
				var l_name_label = document.getElementById('l_name_label');
				l_name_label.innerHTML = "Last Name <span class=asterisk>*</span>";
				var short_description_label = document.getElementById('short_description_label');
				short_description_label.innerHTML = "Short Description <span class=asterisk>*</span>";
				var long_description_label = document.getElementById('long_description_label');
				long_description_label.innerHTML = "Long Description <span class=asterisk>*</span>";
			}
			//If all fields are filled, proceed with insertion request
			else
			{				
				display_loading_spinner();

				//If user did not enter an Associated Equipment ID, default the value to 0.
				//(0 is used as placeholder for tickets where there is no equipment associated with the ticket).
				if (equipment_id == "")
				{
					document.getElementById("equipment_id").value = "0";
				}
			
				//send_retrieval_request();
				send_insertion_request();
			}
		});
	});

	function send_retrieval_request()
	{
		$.ajax({
			url:		"database_access.php",
			type:		"POST",
			data:		$('form').serialize(),
			beforeSend: function()
			{
				$('#response').html('<span>Retrieving ticket data...</span>');
			},
			success:	function (data)
			{
				console.log("this is data");
				//console.log(data);
				$('form').trigger("reset");
				$('#response').fadeIn().html(data);
			},
			error: function ()
			{
				console.log("Error occurred! Insertion request failed...");
			}
		});
	}
	
	//Function used to initiate insertion of new ticket row to 'Tickets' table
	function send_insertion_request()
	{
		//Combine two forms into FormData object
		var form_data = new FormData(document.forms['form2']);	//this form contains the file input
		var non_file_form = jQuery(document.forms['form1']).serializeArray();
		for (var i = 0; i < non_file_form.length; ++i)
			form_data.append(non_file_form[i].name, non_file_form[i].value);
		
		console.log(typeof(this));
		$.ajax({
			url:		"database_access.php",
			type:		"POST",
			// data:		$('form').serialize(),
			// data:		new FormData(document.getElementById('form1')),
			data:		form_data,
			processData:	false,
			contentType:	false,
			dataType:	'json',
			beforeSend: function()
			{
				$('#response').html('<span>Submitting ticket...</span>');
			},
			success:	function (data)
			{
				console.log("Success");
				console.log(data);
				$('form').trigger("reset");
					
				if (data.query_success)
				{
					$('#response').html('<span>Ticket submitted successfully!</span>');
				}
				else
				{
					$('#response').html('<span>Ticket submission failed! Please confirm the information provided...</span>');
				}				
	
				hide_loading_spinner();
			},
			error: function ()
			{
				console.log("Error occurred! Insertion request failed...");
				alert("Error occurred! Insertion request failed...");
			}
			// error: function(xhr, status, error)
			// {
				// alert(xhr.responseText);
			// }
		});
	}

	function display_loading_spinner()
	{
		console.log("SPINNER SHOWN");
		var spinner = document.getElementById("spinner");
		if (spinner.classList.contains("hidden"))
		{
			spinner.classList.remove("hidden");
		}
	}

	function hide_loading_spinner()
	{
		console.log("SPINNER HIDDEN");
		var spinner = document.getElementById("spinner");
		if (!spinner.classList.contains("hidden"))
		{
			spinner.classList.add("hidden");			
		}
	}
</script>