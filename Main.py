import csv

with open('C:/Users/NCout/Desktop/ClassGithub/PyChallenge/Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    total_months = 0
    net_total = 0
    prev_profit = 0
    changes = []
    max_increase = 0
    max_decrease = 0
    max_decrease_data = ""
    max_increase_data = ""
    for row in reader:
        total_months += 1
        profit = int(row[1])
        net_total += int(row[1])

        if total_months > 1:
            change = profit - prev_profit
            changes.append(change)
            if change > max_increase:
                max_increase = change
                max_increase_data = row[0]

            if change < max_decrease:
                max_decrease = change
                max_decrease_data = row[0]

        prev_profit = profit

    average_change = sum(changes) / len(changes)

# Budget print and file
print("-------------------------\n")
print("\n")
print("Financial Analysis\n")
print("\n")
print("-------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total Net: ${net_total}\n")
print(f"Average Change: ${average_change:.2f}\n")
print(f"Greatest Increase in Profits: {max_increase_data} (${max_increase})\n")
print(f"Greatest Decrease in Profits: {max_decrease_data} (${max_decrease})\n")

with open('budget_analysis.txt', 'w') as output:
    output.write("-------------------------\n")
    output.write("Financial Analysis\n")
    output.write("\n")
    output.write("-------------------------\n")
    output.write("\n")
    output.write(f"Total Months: {total_months}\n")
    output.write("\n")
    output.write(f"Total: ${net_total}\n")
    output.write("\n")
    output.write(f"Average Change: ${average_change:.2f}\n")
    output.write("\n")
    output.write(f"Greatest Increase in Profits: {max_increase_data} (${max_increase})\n")
    output.write("\n")
    output.write(f"Greatest Decrease in Profits: {max_decrease_data} (${max_decrease})\n")
    output.write("\n")

# election 
with open('C:/Users/NCout/Desktop/ClassGithub/PyChallenge/Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    total_votes = 0
    candidates = {}
    for row in reader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    max_votes = 0
    winner = ""

    summary = {}
    for i in candidates.items():
        percentage = (i[1] / total_votes) * 100
        summary[i[0]] = {"#votes": i[1], "percentage": percentage}

        if i[1] > max_votes:
            max_votes = i[1]
            winner = i[0]

# election print and file 
print("-------------------------\n")
print("\n")
print("Election Results\n")
print("\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
for candidate, data in summary.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['#votes']})\n")
print(f"Winner: {winner}\n")
print("-------------------------\n")

with open('election_analysis.txt', 'w') as output_file:
    output_file.write("-------------------------\n")
    output_file.write("\n")
    output_file.write("Election Results\n")
    output_file.write("\n")
    output_file.write("-------------------------\n")
    output_file.write("\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("\n")
    for candidate, data in summary.items():
        output_file.write(f"{candidate}: {data['percentage']:.3f}% ({data['#votes']})\n")
    output_file.write("\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("\n")