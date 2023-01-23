#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
    
def GetHoursWorked():
    hrsWrkd = input("Enter hours worked: ")
    return hrsWrkd
    
      
def GetHourlyRate():
    hrlyRate = input("Enter hourly rate: ")
    return hrlyRate

   
   

def GetTaxRate():
    taxrate = input("Enter Tax Rate: ")
    return taxRate


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    
    print("Hourly Rate: ", "Enter pay rate of the employee: " )
    print("Gross Pay:", empgrosspay)
    print("Tax Rate: ", taxrate )
    print("Income Tax: ",  incometax  )
    print("Netpay ", empnetpay)

    
   
   

   




    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print(f"Total GrossPay: {TotGrossPay: ,.2f}")
    print(f"Total Tax: {TotTax: ,.2f}")
    print(f"Total NetPay: {TotNetPay: ,.2f}")



if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        GetHourWorked = hrsWrked

        GetHourlyRate = hrlyRate

        GetTaxrate = taxRate

       

        
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours

        pay = getGrossPay(annual_salary, no_of_pay_periods)

        print(f"Total gross pay: Rs. {pay:.2f} lakhs ")

        hours = float(input('Enter the hours'))

        rate = float(input('Enter the rate'))

        if hours <=40:
            wage =hours * rate
            
        else:

            wage = ((1.5* rate * hours-40) + (40 * rate))

            print(wage)

            if income >= 30000:
                tax = ((income - 30000) * .1) + (15000 * .05)
                income = income - tax
         
            elif income >= 15000:
                tax = (income -15000) * 0.5
                income = income - tax
            elif income >= 0:
                income = income
            else:
                print("Please enter a valid income of more than $0!")
           

        
        Netpay = ("Wage minus deductions ")

        
           
       

            
              

           

       

         

       

           
            
            



           
        

        



    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)

