#The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidates won
# 5. The winnder of the election based on popular vote.

# Add dependencies.
import csv
import os

# Assign a variable for the file to load as the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create A filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# ---DECLARING---

# Initialize a total vote counter--this will count the total votes/rows from the [2nd row] down (1st row is skipped because it is the header row).
total_votes = 0 

# To get each candidate from the list, we iterate through the row.
# Declare a new list, candidate_options = [] by adding it BEFORE the with open() statement in the script
candidate_options = [] # will be passed into the for loop below

# Declare an empty dictionary. (To create a dictionary, we first need to declare an empty dictinoary BEFORE the open() statement.)
candidate_votes = {} # will be passed into the for loop below; remember, dictionaries are = {key,value}

# Winning Candidate and Winning Count Tracker:
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# PyPoll_Challenge.py variables/lists/dictionaries:
county_options = []
county_votes = {}
winning_county = ""
winning_county_percentage = 0
winning_county_count = 0

# ---/END DECLARING---

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row (as we do not want the [1st row] header row to be read during the analysis)
    headers = next(file_reader)
    # print(headers)

    # Rows down the file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2] # (Row index of 2 of election_results.csv--Charles Casper Stockam, Diana DeGette, Raymon Anthony Doane)
        
        county_name = row[1] # (Row index of 1--of election_results.csv--either Jefferson, Denver or Arapahoe)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. To create each candidate as a key, use candidate_votes[candidate_name] and then add candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] = 0

        # ^^^ Add a vote to that candidate vote (refer to line of code above).
        candidate_votes[candidate_name] += 1 # (Important!): This has to be outside of the if statement (indentation matters in Python)
        
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        
        # Add a vote to that county vote (refer to the line of code above).
        county_votes[county_name] += 1 # (Important!): This has to be outside of the if statement as well.

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    txt_file.write("\nCounty Votes:\n")

    for county_name in county_votes:
        # Retrieve vote count of a county.
        votescounted = county_votes[county_name]
        # Calculate percentage of votes.
        county_vote_percentage = float(votescounted)/float(total_votes) * 100
        # Print the county name and the percentage of votes.
        county_results = ( 
            f"{county_name}: {county_vote_percentage:.1f}% ({votescounted:,})\n")
        print(county_results) # (Onto terminal)
        txt_file.write(county_results)
        if votescounted > winning_county_count and (county_vote_percentage > winning_county_percentage):
            winning_county_count = votescounted
            winning = county_vote_percentage
            winning_county = county_name

    # Largest turnout summary.
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n\n")
    print(winning_county_summary) # (Onto terminal)
    # Save the county to the text file.
    txt_file.write(winning_county_summary)


    # Determine the percentage of votes for each candidate for looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and the percentage of votes.
        candidate_results = ( 
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's vote count and percentage to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate and
        # determine if the votes is greater than winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #  If true then set winning_count to votes and winning_percent = vote_percentage.
            winning_count = votes

            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # Print out the winning candidate, vote count and percentage to terminal.
        # print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")--commented out per Module 3.6.1; instead, results are written onto the text file.

    # Code below has to be outside of the if statement and aligned with the for loop above:
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)