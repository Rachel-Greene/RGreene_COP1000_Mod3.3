# This code determines if a date entered is valid #

## ---------- Housekeeping() ---------- ##
# Variables #
validDate = True
validDay = True
minYear = 0
minMonth = 1
maxMonth = 12
minDay = 1
maxDay30 = 30
maxDay31 = 31
maxDay29 = 29

# Input Statements #
print("Please enter numeric values of the date you wish to validate.")
month = input("Month: ")
day = input("Day: ")
year = input("Year: ")
# convert inputs #
month = int(month)
day = int(day)
year = int(year)


## ---------- Detail() ---------- ##
# Check Validity #
if month in [1, 3, 5, 7, 8, 10, 12]:
  validDay = day >= minDay and day <= maxDay31
elif month in [4, 6, 9, 11]:
  validDay = day >= minDay and day <= maxDay30
elif month in [2]:
  validDay = day >= minDay and day <= maxDay29
else: validDay = False

if year <= minYear:
  validDate = False
elif month < minMonth and month > maxMonth:
  validDate = False
elif validDay == False:
  validDate = False


## ---------- endOfJob() ---------- ##
if validDate == True:
    print(f"{month}/{day}/{year} is a valid date")
else:
    print(f"{month}/{day}/{year} is an invalid date")
