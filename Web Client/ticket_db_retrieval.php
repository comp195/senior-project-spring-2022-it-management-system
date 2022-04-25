<?php
	require ("../db_config.php");
	
	$rows = [];
	get_specific_ticket_rows($eid);
	
	//Function to obtain all Tickets table data rows based on employee ID parameter
	function get_specific_ticket_rows($input_eid)
	{
		global $connection;
		$sql_query = "SELECT * FROM Tickets WHERE client_id = $input_eid";
		$result = mysqli_query($connection, $sql_query);
	
		global $rows;
		while ($row = mysqli_fetch_assoc($result))
		{
			$rows[] = $row;
		}

		//mysqli_free_result($result);		
		//mysqli_close($connection);
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