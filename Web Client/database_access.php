<?php
    require ("db_config.php");

    /*["ticket_number", "ticket_status", "client_id", "client_first_name", "client_last_name",
        "equipment_id", "ticket_category", "short_description", "full_description", "issue_scope",
        "priority", "department"]
    */
    $sql_query = "SELECT * FROM Tickets";

    // Run query
    $result = $connection->query($sql_query);
	printf("<br><br>");
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
	
    $connection -> close();
?>