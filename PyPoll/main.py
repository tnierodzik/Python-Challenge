import os
import csv

print("")
print("Election Results")
print("----------------------------------------------")

csvpath = os.path.join("election_data.csv")

totalvotes = 0
candidates = []
name = []
vote_count = []
vote_percentage = []

with open(csvpath,"r") as csvfile:

	csvreader = csv.reader(csvfile,delimiter=",")
	csv_header = next(csvreader)

	for row in csvreader:

		totalvotes = totalvotes + 1
		candidates.append(row[2])

	for candidate in set(candidates):

		name.append(candidate)
		vote_per_candidates = candidates.count(candidate)
		vote_count.append(vote_per_candidates)
		vote_percentage_per_candidates = (vote_per_candidates/totalvotes)*100
		vote_percentage.append(vote_percentage_per_candidates)
		maximum = max(vote_count)
		maximum_candidate = candidates[vote_count.index(maximum)]


print(f"Total Votes: {str(totalvotes)}")

print("----------------------------------------------")

for i in range(len(name)):
	print(f"{str(name[i])} + {str(vote_percentage[i])} + {int(vote_count[i])}")

print("----------------------------------------------")

print(f"Winner is {str(maximum_candidate)} with a total of {int(maximum)} votes")

output_file = os.path.join("Election Results.csv")

with open(output_file,"w") as text:

		text.write(f"Election Results \n")
		text.write(f"---------------------------------------------------\n")
		text.write(f"Total Votes: {str(totalvotes)} \n")
		for i in range(len(name)):
			text.write(f"{str(name[i])} + {str(vote_percentage[i])} + {int(vote_count[i])} \n")
		text.write("---------------------------------------------------" + "\n")
		text.write(f"Winner is {str(maximum_candidate)} with a total of {str(maximum)} votes")