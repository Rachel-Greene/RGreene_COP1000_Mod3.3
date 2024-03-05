# This code determines if a date entered is valid #

## ----- Housekeeping() ----- ##
# Variables #
validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Input Statements #
print("Please enter numeric values below.")
month = input("Month: ")
day = input("Day: ")
year = input("Year: ")

# Convert Inputs #
day = int(day)
month = int(month)
year = int(year)


## ----- Detail() ----- ##
if (year) <= MIN_YEAR:
    validDate = False
elif (month) < MIN_MONTH or (month) > MAX_MONTH:
    validDate = False
elif (day) < MIN_DAY or (day) > MAX_DAY:
    validDate = False


## ----- endOfJob() ----- ##
if validDate == True:
    print(f"{month}/{day}/{year} is a valid date")
else:
    print(f"{month}/{day}/{year} is an invalid date")
