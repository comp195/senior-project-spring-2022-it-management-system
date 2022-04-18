<?php
    require ("../db_config.php");
	
    /*["ticket_number", "ticket_status", "client_id", "client_first_name", "client_last_name",
        "equipment_id", "ticket_category", "short_description", "full_description", "issue_scope",
        "priority", "department"]
		["employee_id", "first_name", "last_name", "email", "num_equipment_used", "department",
		"phone_extension"]
    */
    
	printf("<br><br>");
	
	//Comment or uncomment function calls depending on use-case
	//NOTE: also comment out the send_retrieval_request or send_insertion_request function in Form.html
	// get_ticket_rows();	
	insert_ticket_data();	
	
	//Use this to test and view updates to the Tickets table
	function get_ticket_rows()
	{
		global $connection;
		$sql_query = "SELECT * FROM Tickets";
		$result = $connection->query($sql_query);
		
		while ($row = mysqli_fetch_assoc($result))
		{
			printf( $row["ticket_number"] . "<br>" .
					$row["ticket_status"] . "<br>" .
					$row["client_id"] . "<br>" .
					$row["client_first_name"] . "<br>" .
					$row["client_last_name"] . "<br>" .
					$row["equipment_id"] . "<br>" .
					$row["ticket_category"] . "<br>" .
					$row["short_description"] . "<br>" .
					$row["full_description"] . "<br>" .
					$row["issue_scope"] . "<br>" .
					$row["priority"] . "<br>" .
					$row["department"] . "<br><br>");
		}		
	}
	
	function insert_ticket_data()
	{
		global $connection;		
		
		$eid = mysqli_real_escape_string($connection, $_POST["eid"]);
		$f_name = mysqli_real_escape_string($connection, $_POST["f_name"]);
		$l_name = mysqli_real_escape_string($connection, $_POST["l_name"]);
		
		//Associated Equipment Id is optional, so ensure that it is stored as NULL in db if empty string
		if (empty($_POST["equipment_id"])) {$equipment_id = "NULL";}	
		else {$equipment_id = mysqli_real_escape_string($connection, $_POST["equipment_id"]);}
		
		$short_description = mysqli_real_escape_string($connection, $_POST["short_description"]);
		$long_description = mysqli_real_escape_string($connection, $_POST["long_description"]);
		$ticket_category = mysqli_real_escape_string($connection, $_POST["categories"]);
		$scope = mysqli_real_escape_string($connection, $_POST["scope"]);
		
		//Determine the Priority field based on Scope
		if ($scope == "Single User") {$priority = "Low";}
		elseif ($scope == "Team") {$priority = "Medium";}
		elseif ($scope == "Departmental") {$priority = "High";}		
		
		//Obtain Department field from the Employee table			
		$department = get_department_from_eid($eid);
		
		$sql_query = "INSERT INTO dbmanagementsystem.Tickets (ticket_status, client_id, client_first_name, client_last_name, equipment_id, ticket_category, short_description, full_description, issue_scope, priority, department) VALUES ('Submitted', '".$eid."', '".$f_name."', '".$l_name."', '".$equipment_id."', '".$ticket_category."', '".$short_description."', '".$long_description."', '".$scope."', '".$priority."', '".$department."')";   				
		
		// printf($sql_query);
		mysqli_query($connection, $sql_query);
		
		// printf(nl2br($eid . "\n" . $f_name . "\n" . $l_name . "\n" . $equipment_id . "\n" . $short_description . "\n" . $long_description . "\n" . $ticket_category . "\n" . $scope . "\n" . $priority . "\n" . $department));
	}		

	//Helper method to retrieve the Department field associated with an employee.
	function get_department_from_eid($eid)
	{
		global $connection;
		
		$sql_query = "SELECT department FROM Employee WHERE employee_id = '".$eid."'";
		$result = $connection->query($sql_query);
		$row = mysqli_fetch_assoc($result);
		$department = $row["department"];
		return $department;
	}
	
    $connection -> close();
?>