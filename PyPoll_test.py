# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5.The winner of the election based on popular vote
import os
import csv

#os.getcwd() to get the current working directory
#os.chdir(path) to change the current working directory

os.chdir("C:/Users/raney/OneDrive/Desktop/Analysis_Projects/Election_Analysis")
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")

#open the file
#election_data = open(file_to_load, 'r')

#close the file
#election_data.close()

#open and read the file
with open(file_to_load) as election_data1:
    print(election_data1)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
with open(file_to_save, "w") as text_file:

#write Hello World
#outfile.write("Hello World")
    #Write three counties to file
    #text_file.write("Arapahoe, Denver, Jefferson")
    #text_file.write("Denver, ")
    #text_file.write("Jefferson")
    text_file.write("Counties in the Election")
    text_file.write("\n------------------------\n")
    text_file.write("Arapahoe\nDenver\nJefferson")


# close the file
#outfile.close()

