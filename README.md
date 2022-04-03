# Election_Analysis
## UCD Module 3: PyPoll with Python; Project Overview
A Colorado Board of Educations employee has given the following tasks to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Determine the winner of the election based on popular vote.
## Resources
Data Source: election_results;
Software: Python 3.7 (64-bit), Visual Studio Code (v. 1.66).
## Summary/Election-Audit Results 
The analysis of the election shows that there were a total of 369,711 votes that were cast in the congressional election.
### There were a total of 3 counties:
1. Jefferson, CO
2. Denver, CO
3. Arapahoe, CO
### The results for the counties are:
1. Jefferson county contributed to 10.5% of the vote with a total of 38,855 votes.
2. Denver county contributed to 82.6% of the vote with a total of 306,055 votes, which was the largest county turnout of all 3 counties.
3. Arapahoe county contributed to 6.7% of the vote with a total of 24,801 votes.
#### (In order to calculate the percentage of votes for a county, divide the total votes of the county by the total number of votes of all counties, then multiply by 100 to get the proper decimal value--code found on line 101 in PyPoll_Challenge.py). 
### There were a total of 3 candidates for all 3 counties:
1. Charles Casper Stockam
2. Diana DeGette
3. Raymon Anthony Doane
### The candidate results were:
1. Candidate Charles Casper Stockam received 23.0% of all votes with a total of 86,213 votes.
2. Candidate Diana DeGette received 73.8% of all votes with a total of 272,892 votes.
3. Candidate Raymon Anthony Doane received 3.1% of all votes with a total of 11,606 votes.
#### (In order to calculate the percentage of votes for a candidate, divide the total votes that the candidate received by the total number of votes that were cast within all 3 counties--code found on line 128 in PyPoll_Challenge.py).
### The winner of the election was: candidate Diana DeGette, who received (73.8%) of the vote with 272,892 total votes.
# Business Proposal: 
#### The script proves to be able to account for hundreds of thousands of votes that made up the election (in the csv file provided election_results.csv). The script can be applied to any election.  A the script may be modified would be if there is a need to go more in-depth in terms of demographics.  Two ways the script can be modified might be (1) to know which age group voted the least/most for each candidate (for example Gen-Z/Millenials/Boomers), or (2) which political party a voter might a afiiliate with when voting (for example, Democrat/Republican/Independent). More examples of demographics in terms of elections include a voter's gender, or socio-economic standing, whether it'd be lower/lower-middle/middle/upper-middle/upper, or a voter's nationality/ethnicity--all of which can be taken into acccount by modifying the script.
