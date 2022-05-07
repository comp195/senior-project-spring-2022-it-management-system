Senior Project - IT Management System


Last Update:     05/06/2022

Contributors:    Daniel Adler - d_adler@u.pacific.edu
		 Vincent Tran - v_tran37@u.pacific.edu
		 Andrew Vu    - a_vu16@u.pacific.edu

Description:     This IT management system exists to provide small business managers and IT technicians to
		 have full scope over their assets, employees, and issues that might be impeding them from
		 delivering their products and services. It also gives employees the ability to access some
		 information from a web client, and gives them the ability to submit tickets about faulty
		 equipment.

Components:	 This system is separated into two components: The Desktop Application used by high
		 permission level internal parties in order to access and modify relevant information for
		 the business, and the Web Application will provide other employees with the ability to
		 submit tickets regarding maintenance and view relevant information.
		
		 The Desktop Application includes:
			- A Login Section that limits access to users with sufficient permissions
			- An Equipment Screen that gives users detailed information about company equipment
			- An Employee Screen that gives users detailed information about employees
			- A Ticket Screen that gives users detailed information about tickets submitted by
			   employees

		 The Web Application Includes:
			- A Login section that limits access to users that are employees
			- A Ticket Screen that gives employees the ability to submit tickets about issues
			- A View Tickets screen that gives employees the ability to view their own tickets

*Special Notes:   STEPS MUST BE TAKEN FOR EXECUTABLE TO WORK:
		  [1] Create conn_details.txt file that must be created and placed into the executable file's 	                     
                  directory. The format should be as follows:
                  <HOST>       
		  <USERNAME OF REMOTE SERVER>
		  <PASSWORD TO REMOTE SERVER>

                  *Ensure there is no leading or trailing whitespace.
		  *REMOTE SERVER in our case refers to an AWS EC2 instance.
		
		  [2] Create a folder called "retrieved_image_files" in "IT Management System\dist\test_screen\"
		  This is necessary if you would like to use the "Show attached image" feature.
		  
		  
		  *THE EXECUTABLE IS LOCATED AT "IT Management System\dist\test_screen\AVD_IT_Management_System.exe"
		   within the 7z file.
		  *THE WEB CLIENT LINK IS: http://ec2-18-144-147-150.us-west-1.compute.amazonaws.com/ OR 
		  http://18.144.147.150/
		  
		  *The executable file may be flagged incorrectly. Check antivirus settings.
