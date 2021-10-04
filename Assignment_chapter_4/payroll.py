# David Wagner - Assignment 4 Payroll - CIDM 6303
# create a function to calculate various taxes for an employee
# see instructions for details


def calc_payroll_tax(gross_pay):
    print(f"Gross pay is $: {gross_pay:.2f}")
    medicare = (gross_pay * 0.0145)
    print(f"Medicare is $: {medicare:.2f}")
    futa = (gross_pay * .006)
    print(f"FUTA is: $ {futa:.2f}")
    ss_tax_employer = (gross_pay * .062)
    print(f"Social Security tax paid by employer: ${ss_tax_employer:.2f}")
    ss_tax_employee = (gross_pay * .062)
    print(f"Social Security tax paid by employer: ${ss_tax_employee:.2f}")
    total_tax = (medicare + futa + ss_tax_employee)
    print(f"Total Payroll tax paid by employee: $ {total_tax}")
    net_pay = (gross_pay - total_tax)
    print(f"Net Pay: $ {net_pay}")
    print("")



