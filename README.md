# devopsTasks
original text of assignment:

1. [Scripting] Write 2 scripts
	a. Script that uses alphavantage to retrieve ticker data. https://www.alphavantage.co/documentation/
		Script should retrieve ticker data for BCH (Bitcoin-Cash), ETH (Ethereum), LTC (Litecoin), OPT (Opus) and one of your choosing traded on EUR (Euro) (Daily). 
		Write all tickers to one file where gains are positive
		Write all other tickers to another file where gains are negative
	b. Second script should read both files and print out which stock had biggest gains and which had biggest loss

2. [Windows] Setup a scheduled task to run 2 previous scripts daily.
3. [Linux] Write a bash script which would check If sshd.sevice is running and output status to a file.
4. [Scripting] Write a regex expression to return every line that is not heartbeat check. Log file attached.
5. [Scripting] Write a script to get status of service on a remote machine.
6. [SQL] You have 5 tables:
        1) Sensitive customers: CustomerID, IsActive, DateOfBirth.
		2) Non-sensitive customers: CustomerID, IsActive, DateOfBirth. (Has more than 3 million entries)
		3) Foreign customers: CustomerID, IsActive, DateOfBirth.
		4) Customer address: CustomerID, CustHouseNo, CustStreetNm, CustAddressLine1, CustAddressLine2, CustAddressLine3
		5) Customer interests: CustomerID, CustomerInterest1, CustomerInterest2

	Write queries to extract following:
		1) Get addresses of active customers that are not sensitive
		2) Get interests of all customers that were born in 1986
7. [Scripting] Write a script to split log file (attached) into different files based on activity code. Activity code is present just before log entry level. Additionally create one single files with all entries sorted by activity code.
8. [Scripting] Write a script to check who has access to a particular directory.
