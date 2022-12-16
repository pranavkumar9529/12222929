a=''' _____ _         _____       _            _       _             
|_   _(_)       /  __ \     | |          | |     | |            
  | |  _ _ __   | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  | | | | '_ \  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | | | | |_) | | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
  \_/ |_| .__/   \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
        | |                                                     
        |_|                                                     '''

print(a)
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
