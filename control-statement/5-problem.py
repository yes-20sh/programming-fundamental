# Write a  program to input electricity unit charge and calculate the total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.


electricityUnit = float(input("Enter the electricity unit : "))

totalElectricityBill = 0

if electricityUnit <= 50:
    totalElectricityBill = electricityUnit * 0.50

elif electricityUnit <= 150:
    totalElectricityBill = (50 * 0.50) + (electricityUnit - 50) * 0.75

elif electricityUnit <= 250:
    totalElectricityBill = (50 * 0.50) + (100 * 0.75) + (electricityUnit - 150) * 1.20

else:
    totalElectricityBill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (electricityUnit - 250) * 1.50


surcharge = totalElectricityBill * 0.20
totalElectricityBill += surcharge

print(f"Total electricity bill = Rs. {totalElectricityBill:.2f}")
