# Add our dependencies.
import csv
import os

#set the current directory
os.chdir("C:/Users/raney/OneDrive/Desktop/Analysis_Projects/Election_Analysis")
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

# declare a list
candidate_options = []

#Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_count = 0
winning_candidate = ""
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #print headers
    headers = next(file_reader)
    #print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total votes
        total_votes += 1

        #get the candidate name from each row
        candidate_name = row[2]
    
        #Check the candidate name is already added
        if candidate_name not in candidate_options:

            #Add the candidate name to the list
            candidate_options.append(candidate_name)

            #Initialize the candidate voye count = 0
            candidate_votes[candidate_name] = 0

        #Initialize the candidate voye count = 0
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as text_file:    

    # Save the results to our text file.
    election_results = (
        f"Election Results \n"
        f"----------------------- \n"
        f"Total votes: {total_votes:,} \n"
        f"----------------------- \n"
        f"\nVotes for each Candidate \n"
        f"---------------------------------------- \n"
    )
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    text_file.write(election_results)


    # Determine the percentage of votes by each candidate
    # interate through the candidate list
    for candidate_name in candidate_votes:
        
        #Retrieve the candidate votes
        votes = candidate_votes[candidate_name]
        
        #calculate the percentage for each candidates
        vote_percentage  = (votes/total_votes) * 100

        #print the percenatge of votes recieved by the candidates
        print(f"{candidate_name}: recieved {vote_percentage:.2f}% of votes")
        
        candidate_results = (
            f"{candidate_name} : {vote_percentage:.1f}% ({votes:,})\n"
        )

        # Save the winning candidate's results to the text file.
        text_file.write(candidate_results)

        # Winning Candidate and Winning Count Tracker
        if (votes > winning_count) and (vote_percentage > winning_percentage) :
            
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Winning candidate summary
    winning_summary = (
        f"\n---------------------------------\n"
        f" **** WINNING SUMMARY **** \n"
        f"Winner: {winning_candidate} \n"
        f"Winning vote count : {winning_count} \n"
        f"Winning vote percentage : {winning_percentage:.1f}% \n"
        f"---------------------------------\n"
    )
    print(winning_summary)
    
    # Save the winning candidate's results to the text file.
    text_file.write(winning_summary)
    
# End of program

    