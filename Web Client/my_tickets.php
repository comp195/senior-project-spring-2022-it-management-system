<?php
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
				width: 960px;
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
				function draw_table()
				{
					var tickets_data = new google.visualization.DataTable();
					tickets_data.addColumn('string', 'Testing');
					tickets_data.addRows([
						['Test1'],
						['Test2']
					]);
					
					var tickets_table = new google.visualization.Table(document.getElementById('tickets_table_div'));
					
					tickets_table.draw(tickets_data, {showRowNumber: true, width: '100%', height: '100%'});
				}
				google.charts.setOnLoadCallback(draw_table);
			</script>			
		</div>
	</body>

</html>