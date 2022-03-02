# Election_Analysis
This is the repository to store the Election Analysis Challenge

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winnner of the election based on popular vote.

## Resources
- Data source : election_results.csv
- Software Python 3.10.1, Visual studio Code 1.64.2

## Challenge Overview
Prerequisite:
Download the PyPoll_Challenge_starter_code.py file and rename it PyPoll_Challenge.py.

Use the step-by-step instructions below to add code where indicated by the numbered comments in the starter code file.

Step 1: Initialize a county list, like the candidate_options list, that will hold the names of the counties.
		    Initialize a dictionary, like the candidate_votes dictionary, that will hold the county as the key and the votes cast for each county as the values.

Step 2: Initialize an empty string, like winning_candidate, that will hold the county name for the county with the largest turnout.
	      Initialize a variable, like the winning_count variable, that will hold the number of votes of the county that had the largest turnout.
	   
Step 3: While reading the election results from each row inside the for loop, write a script that gets the county name from each row.

Step 4a: Write a decision statement with a logical operator to check if the county name acquired in Step 3 is in the county list you created in Step 1.

Step 4b: If the county is not in the list created in Step 1, add it to the list of county names like you did when adding a candidate to the candidate_options list.

Step 4c: Write a script that initializes the county vote to zero, like you did when you began to track the vote counts for the candidates.

Step 5: Write a script that adds a vote to the county’s vote count as you are looping through all the rows, like you did for the candidate’s vote count.

Step 6a: Write a repetition statement to get the county from the county dictionary that was created in Step 1.

Step 6b: Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.

Step 6c: Write a script that calculates the county’s votes as a percentage of the total votes.

Step 6d: Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line.

Step 6e: Write a script that saves each county, the county’s total votes, and the county’s percentage of total votes to the election_results.txt file.

Step 6f: Write a decision statement that determines the county with the largest vote count and then adds that county and its vote count to the variables created in Step 2.

Step 7: Write a print statement that prints out the county with the largest turnout.

Step 8 : Write a script that saves the county with the largest turnout to the election_results.txt file.

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election

- County Votes breakdown:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)

- County wuth largest number of votes: Denver  

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- Candidate Votes breakdown:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

- The winnner of the election was:
  - Diana DeGette, who received 73.8% of vote and 272,892 number of votes.

## Election Audit Summary
This python script can be reused with minor changes for any election audits provided the structure of the election data is in csv format is not changed.
The following tweaks may needs to be done inorder to reuse the program
  - Tweak for the csv file name and path of the file 
  - Tweak may be required if the column number for the candidate name or county name is changed.