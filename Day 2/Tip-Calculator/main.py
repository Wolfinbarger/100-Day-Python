print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total bill? $"))

tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12, or 15 ")) / 100

num_people = int(input("How many people will split the bill? "))

tip_amount = total_bill * tip_percentage

pay_per_person = round((tip_amount + total_bill) / num_people, 2)

print(f"Each person should pay: ${pay_per_person}")
