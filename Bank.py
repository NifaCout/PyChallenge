import csv


with open('C:/Users/NCout/Desktop/LearnPy/Resources/budget_data.csv', 'r') as file:
    reader=csv.reader(file)
    header=next(reader)
    total_months = 0
    net_total = 0
    prev_profit = 0
    changes =[]
    max_increase = 0
    max_decrease = 0
    max_decrease_data = 0
    max_increase_data = 0
    for row in reader:
        total_months +=1
        profit = int(row[1])
        net_total +=int(row[1])

        if total_months >1:
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

print("Financial Analysis\n")
print("-------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total}\n")
print(f"Average Change: ${average_change:.2f}\n")
print(f"Greatest Increase in Profits: {max_increase_data} (${max_increase})\n")
print(f"Greatest Decrease in Profits: {max_decrease_data} (${max_decrease})\n")

with open('analysis.txt', 'w') as output:
    output.write("Financial Analysis\n")
    output.write("\n")
    output.write("\n")
    output.write("-------------------------\n")
    output.write("\n")
    output.write("\n")
    output.write(f"Total Months: {total_months}\n")
    output.write("\n")
    output.write("\n")
    output.write(f"Total: ${net_total}\n")
    output.write("\n")
    output.write("\n")
    output.write(f"Average Change: ${average_change:.2f}\n")
    output.write("\n")
    output.write("\n")
    output.write(f"Greatest Increase in Profits: {max_increase_data} (${max_increase})\n")
    output.write("\n")
    output.write("\n")
    output.write(f"Greatest Decrease in Profits: {max_decrease_data} (${max_decrease})\n")