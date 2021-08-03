#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator? ")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you pay? 10, 12, 15 (in per): "))
people = int(input("How many people to split the bill? "))
tip_per = tip / 100
amt_total = bill + bill*tip_per

amt_each = amt_total/people
#amt_each_round_to_2 = round(amt_each, 2)
amt_each_round_to_2 = "{:.2f}".format(amt_each)
print(f"Each person shoulf pay: {amt_each_round_to_2}")