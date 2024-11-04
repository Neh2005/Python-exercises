def milageClaim(miles):
    # Check if the provided miles value is non-negative and check different mileage ranges and calculate expense accordingly
    if miles >= 0 and miles <= 10:
        claim = miles * 0.5   # Expense rate for the first 10 miles
        print("Total expense:", claim)
    elif miles > 10 and miles <= 100: 
        claim = 10 * 0.5 + (miles - 10) * 0.37   # Expense rate for the next 90 miles after the first 10 miles
        print("Total expense:", claim)
    elif miles > 100:
        claim = 10 * 0.5 + 90 * 0.37   # If miles exceed 100, no additional expense is allotted
        print("No money allotted above 100 miles:", claim)
    else:
        claim = 0.0   # If miles are negative, no claim can be made
        print("Miles can't be negative.")
    # Round the claim amount to two decimal places
    return round(claim, 2)

if __name__ == "__main__":
    # Prompt user for input
    miles = int(input("How many miles? "))
    # Calculate and display the mileage claim
    print("Claim is for £" + str(milageClaim(miles)))
