# This program will give you a break down as to what you can afford based on you salary :)

name = input("What is your name? ")
weekly_hours = int(input("How many hours do you work per week "))
working_days = int(input("How many days a week do you work "))
annual_salary = float(input("What is you annual salary? "))
monthly_rent = int(input("How much is your rent? "))

# Some napkin math to go here
# Working hours in a year 40hrs a week * 52 weeks in a year = 2080
# So to arrive at your hourly rate we do annual salary / working hours in a year
# Weekly salary is gotten by salary / weeks in a year (52)

hourly_rate = float(annual_salary / (weekly_hours * 52))

daily_rate = hourly_rate * (weekly_hours / working_days)

weekly_rate = float(annual_salary / 52)

monthly_rate = float(annual_salary / 12)

# Florida tax according to https://smartasset.com/taxes/income-taxes

# After tax calculations area

# Tax brackets: federal and fica

# def find_tax_rate(annual_salary):
#     if annual_salary <= 10275 and annual_salary >= 0:
#         tax_rate = .10
#     elif annual_salary <= 41775 and annual_salary >= 10276:
    
#     elif annual_salary <



tax_total = 1 - (.1784 + .0765)

post_tax_daily = tax_total * daily_rate

post_tax_weekly = tax_total * weekly_rate

post_tax_monthly = tax_total * monthly_rate

post_tax_annual  = tax_total * annual_salary

max_rent_amount = post_tax_monthly * .3

income_used_on_rent = float(monthly_rent / post_tax_monthly)

print("====================== "+ name +" Work Information =========================")
print("Name: " + name)
print("Hours worked per week: " + str(weekly_hours))
print("Days a week worked: " + str(working_days))
print("====================== Pre-tax Salary Information =========================")
print("Hourly Rate: {:,.2f}" .format(hourly_rate))
print("Daily Rate: {:,.2f}"  .format(daily_rate))
print("Weekly Rate: {:,.2f}"  .format(weekly_rate))
print("Monthly Rate: {:,.2f}" .format(monthly_rate))
print("Annual Salary: {:,.2f}" .format(annual_salary))
print("====================== Post-tax Salary Information =========================")
print("After tax daily income: {:,.2f}" .format(post_tax_daily))
print("After tax weekly income: {:,.2f}" .format(post_tax_weekly))
print("After tax monthly income: {:,.2f}" .format(post_tax_monthly))
print("After tax annual income: {:,.2f}" .format(post_tax_annual))
print("====================== "+ name +" Financial Information =========================")
print("Disclaimer this will be after tax numbers and percentages")
print("Current Rent: {:,.2f}" .format(monthly_rent))
print("Current Monthly income percentage used on rent: {:.2%}" .format(income_used_on_rent))
print("Maximum that should be used on rent: {:,.2f}" .format(max_rent_amount))