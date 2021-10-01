# David Wagner - Assignment 4 Payroll - CIDM 6303
# create a function to calculate various taxes for an employee
# see instructions for details

 #       def calc_payroll_tax(gross_pay):
  #  return(calc_payroll_tax(2000))

#def calc_payroll_tax(gross_pay):
#    print(f"Gross Pay is {gross_pay:.f2}")
def calc_payroll_tax(gross_pay):
    return gross_pay
#print(calc_payroll_tax())
    #gross_pay = (float(input("Please enter income: ", )))

    medicare = (gross_pay * .0145)
    futa = (gross_pay * .006)
    ss_tax_employer = (gross_pay * .062)
    ss_tax_employee = (gross_pay * .062)
    total_tax = (medicare + futa + ss_tax_employee)
    net_pay = (gross_pay - total_tax)

print(gross_pay)


print(f"Gross pay = $ {gross_pay:.2f}")
print(f"Medicare = $ {medicare:.2f}")
print(f"Employee SS = ${ss_tax_employee:.2f}")
print(f"FUTA = ${futa:.2f}")
print(f" Total Tax = ${total_tax:.2f}")
print(f"Net Pay = ${net_pay:.2f}")
print("-"*30)