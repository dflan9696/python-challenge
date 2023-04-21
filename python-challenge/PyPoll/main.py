# import os

import os
import csv

# import csv

election_path = os.path.join("Resources", "election_data.csv")

election_path_save = os.path.join("Analysis", "election_analysis.txt")

# declaring variables

total_votes = 0
candidate_option = []
candidate_vote = {}
county_vote = {}
county_location = []
winning_candidate = ""
winning_count = 0
winning_pct = 0
largest_county = ""
largest_turnout = 0 

# open csv

with open(election_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    # calculate total vote count

    for row in csvreader:

        # get candadite names

        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        # adds candidate names to list

        if candidate_name not in candidate_option:

            candidate_option.append(candidate_name)
            candidate_vote[candidate_name] = 0

        candidate_vote[candidate_name] += 1

        # adds county name to list

        if county_name not in county_location:

            county_location.append(county_name)
            county_vote[county_name] = 0

        county_vote[county_name] += 1

# save results to text file

with open(election_path_save, "w") as txt_file:

    # prints total vote count

    election_results = (
        f"\nElection Results\n\n"
        f"-------------------------\n\n"
        f"Total Votes: {total_votes:,}\n\n"
        f"-------------------------\n\n" )
    print(election_results, end="")

    txt_file.write(election_results)

    # saves final candidate name and votes

    for candidate_name in candidate_vote:

        votes = candidate_vote.get(candidate_name)
        vote_pct = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_pct:.1f}% ({votes:})\n")
        
        print(candidate_results)

        txt_file.write(candidate_results)

        # determines winning candidate and votes 

        if (votes > winning_count) and (vote_pct > winning_pct):
            winning_count = votes
            winning_candidate = candidate_name
            winning_pct = vote_pct

    # prints winning candidate

    winning_candidate_total = (
        f"-------------------------\n\n"
        f"Winner: {winning_candidate}\n\n"
        f"-------------------------\n")
    
    print(winning_candidate_total)

    txt_file.write(winning_candidate_total)
        

