def personal_allowance(salary):
    if 0 <= salary <= 100000:
        allowance = 12500
        print("Allowance is", allowance)
        return allowance
    elif salary > 100000:
        reduction = (salary - 100000) // 2
        allowance = 12500 - reduction
        if allowance < 0:
            allowance = 0
            print("Allowance is 0")
        else:
            print("Allowance is", allowance)
        return allowance

def incomeTax(salary):
    allowance = personal_allowance(salary)
    if allowance >= salary:
        taxable_salary=0
        income_tax=0
        return income_tax
    elif allowance < salary:
        taxable_salary = salary - allowance
        print("Taxable salary is", taxable_salary)
        if taxable_salary <= 0:
            income_tax = 0
            print("Taxable salary can't be negative")
            return income_tax
        elif 0 < taxable_salary <= 37500:
            income_tax = 20 / 100 * taxable_salary
            print("Income tax is", round(income_tax, 0))
            return round(income_tax, 0)
        elif 37500 < taxable_salary < 150000:
            income_tax = 20 / 100 * 37500 + 40 / 100 * (taxable_salary - 37500)
            print("Income tax is", round(income_tax, 0))
            return round(income_tax, 0)
        else:
            income_tax = 20 / 100 * 37500 + 40 / 100 * (150000 - 37500) + 45 / 100 * (taxable_salary - 150000)
            print("Income tax is", round(income_tax, 0))
            return round(income_tax, 0)

def national_insurance(salary):
    if 0 <= salary <= 183:
        ni = 0
        print("National insurance is", ni)
        return ni
    elif salary < 962:
        ni = 0 + 12 / 100 * (salary - 183)
        print("National insurance is", round(ni, 0))
        return round(ni, 0)
    elif salary >= 962:
        ni = 0 + 12 / 100 * (961 - 183) + 2 / 100 * (salary - 962)
        print("National insurance is", round(ni, 0))
        return round(ni, 0)
    else:
        ni = 0
        print("Invalid salary")
        return ni

if __name__ == "__main__":
  
  salary = int(input("Enter your valid salary: "))
  wages = int(input("Enter your weekly salary: "))
  incomeTax(salary)
  national_insurance(wages)
 
