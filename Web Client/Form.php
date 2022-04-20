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
			
		</style>
	</head>
	
	<body>
		<div id="container">
			<div class="form-container">
				<form>
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

		<form>
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

			<!-- Submit Button -->
			<input type="button" name="submit_button" id="submit_button" value="Submit" class="submit_button"/>
			
			<!-- Response text -->
			<div id="response" style="margin-top:-700px; margin-left:200px;"></div>
		</form>
	</body>
</html>

<!-- Javascript -->
<script>
	$(document).ready(function()
	{
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
		$.ajax({
			url:		"database_access.php",
			type:		"POST",
			data:		$('form').serialize(),
			beforeSend: function()
			{
				$('#response').html('<span>Submitting ticket...</span>');
			},
			success:	function (data)
			{
				console.log("Success");
				console.log(data);
				$('form').trigger("reset");
				<!-- $('#response').fadeIn().html(data); -->
			},
			error: function ()
			{
				console.log("Error occurred! Insertion request failed...");
			}
		});
	}
</script>