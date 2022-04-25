<?php
	require ("ticket_db_retrieval.php");
	console_log("TEST");
	console_log($rows);
		
	if (isset($_POST['link']))
	{
		console_log("testing");
		$eid = $_GET['eid'];
		$f_name = $_GET['f_name'];
		$l_name = $_GET['l_name'];
		console_log($eid);	
		console_log($f_name);
		console_log($l_name);
		console_log("abc");

		//Send the values that were already received BACK to the Form page so that the auto-filled input boxes still work
		header("location: Form.php?eid=".$eid."&f_name=".$f_name."&l_name=".$l_name);
	}
?>

<!DOCTYPE html>
<html>

	<head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
		<title>My Tickets</title>
		<h1>My Tickets</h1>

		<!-- Scripts necessary for Google Charts table -->
		<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
		<script type="text/javascript">
			google.charts.load('current', {'packages':['table']});
		</script>
	
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
			
			#wrapper
			{
				margin-left: auto;
				margin-right: auto;
				width: 1760px;
			}		
	
		</style>
	</head>

	<body>
		<div id="wrapper">
			
			<!--
			* Need to receive EID, First Name, and Last Name values then ensure they are sent back when returning to Ticket Submission Form
			* NOTE: This is due to how the inputs are set up to receive automatic values
			* NOTE: Use 'workaround' of sending POST data with anchor tags through use of a form
			-->		
			<!-- Link to return to the Ticket Submission Form page -->
			<form id="temp_form" method="post" action="<?php $_SERVER['PHP_SELF']?>">
				<input type="hidden" name="link">
				<a href="#" onclick="document.getElementById('temp_form').submit();">Return to Ticket Submission Form</a>			
			</form>	

			<div id="tickets_table_div"></div>			

			<!-- JavaScript -->
			<script>
				var rows;
				$(document).ready(function()
				{				
					//NOTE: must use json_encode here due to issues with special characters	
					rows = <?php echo json_encode($rows); ?>;
					console.log("Rows from JS: ");
					console.log(rows);
				});
				
				function draw_table()
				{
					var TICKET_TABLE_COLUMNS = ["Ticket Number",
												"Ticket Status",
												"Client ID",
												"Client First Name",
												"Client Last Name",
												"Equipment ID",
												"Ticket Category",
												"Short Description",
												"Full Description",
												"Issue Scope",
												"Priority",
												"Department"];
					
					var tickets_data = new google.visualization.DataTable();
					for (var x in TICKET_TABLE_COLUMNS)
					{
						//console.log(TICKET_TABLE_COLUMNS[x]);
						tickets_data.addColumn("string", TICKET_TABLE_COLUMNS[x]);
					}
					
					//NOTE: When 'rows' variable receives value from the PHP variable, the fields are in alphabetical order.
					//		They need to be in correct order based on the columns listed for the table to be drawn.
					//Create a 2D array with the fields in proper order to add to table					
					var rows_with_sorted_fields = [];
					for (var x in rows)
					{
						console.log(rows[x]);
						var curr_row = [];
						curr_row.push(rows[x]["ticket_number"]);
						curr_row.push(rows[x]["ticket_status"]);
						curr_row.push(rows[x]["client_id"]);
						curr_row.push(rows[x]["client_first_name"]);
						curr_row.push(rows[x]["client_last_name"]);
						curr_row.push(rows[x]["equipment_id"]);
						curr_row.push(rows[x]["ticket_category"]);
						curr_row.push(rows[x]["short_description"]);
						curr_row.push(rows[x]["full_description"]);
						curr_row.push(rows[x]["issue_scope"]);
						curr_row.push(rows[x]["priority"]);
						curr_row.push(rows[x]["department"]);
						
						rows_with_sorted_fields.push(curr_row);
					}			
					console.log("HERE:");
					console.log(rows_with_sorted_fields);

					tickets_data.addRows(rows_with_sorted_fields);

					<!-- tickets_data.addColumn('string', 'Testing'); -->
					<!-- tickets_data.addRows([ -->
						<!-- ['Test1'], -->
						<!-- ['Test2'] -->
					<!-- ]); -->
					
					var tickets_table = new google.visualization.Table(document.getElementById('tickets_table_div'));
					
					tickets_table.draw(tickets_data, {showRowNumber: true, width: '100%', height: '100%'});
				}
				google.charts.setOnLoadCallback(draw_table);
			</script>			
		</div>
	</body>

</html>