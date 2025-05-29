# print("Welcome to the tip calculator!")
# bill = input("How much was the total bill? $")
# tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
# number_of_people = int(input("How many people to split the bill? "))

# resutls = round((int(bill) * (int(tip)/100) + int(bill)) / int(number_of_people),2)

# message = f"Each person should pay: ${resutls}"
# print(message)

print("Welcome to the tip calculator!")
bill = float(input("How much was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")