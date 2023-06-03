import csv


with open('C:/Users/NCout/Desktop/LearnPy/Resources/election_data.csv', 'r') as file:
    reader=csv.reader(file)
    header=next(reader)

    total_votes = 0
    candidates = {}
    for row in reader:
    
        total_votes +=1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate]+=1
        else:
            candidates[candidate]=1

    max_votes = 0
    winner = ""

    summary = {}
    for i in candidates.items():
        percentage = (i[1] / total_votes) * 100
        summary[i[0]] = {"#votes": i[1], "percentage": percentage}

        if i[1] > max_votes:
            max_votes = i[1]
            winner = candidate 

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in summary.items():
    print(f"{i[0]}: {i[1]['percentage']:.3f}% ({i[1]['#votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------") 

with open('election_analysis.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for i in summary.items():
        output_file.write(f"{i[0]}: {i[1]['percentage']:.3f}% ({i[1]['#votes']})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

    