# Description: Program for One Stop Insurance Company to process insurance policies.
# Author: Donovan Head
# Date(s): March 13-24, 2024

# import required libraries

import datetime
from datetime import timedelta 
import time
import FormatValues as FV
import sys

# Define program constants.

# Using a Defaults file to store the default values for the program.

f = open("Default.dat", "r")
POLICY_NUM = int(f.readline())
BASIC_PREM_COST = float(f.readline())
EXTRA_CAR_DISCOUNT_RATE = float(f.readline())
EXTRA_LIABILITY_COST = float(f.readline())
GLASS_COVERAGE_COST = float(f.readline())
LOANER_COST = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PRCSSING_FEE = float(f.readline())
f.close()

CURRENT_DATE = datetime.datetime.now()

# Define program functions.
def CalcExCost(NumInsu, GlassCov, ExtLia, LoanCar):
        global GlassCovAmt
        global ExtLiabAmt
        global LoanAmt
        global TotExtCost


        if GlassCov == 'Y':
            GlassCovAmt = GLASS_COVERAGE_COST * NumInsu
        else:
            GlassCovAmt = 0

        if ExtLia == 'Y':
            ExtLiabAmt = EXTRA_LIABILITY_COST * NumInsu
        else:
            ExtLiabAmt = 0

        if LoanCar == 'Y':
            LoanAmt = LOANER_COST * NumInsu
        else:
            LoanAmt = 0 

        TotExtCost = GlassCovAmt + ExtLiabAmt + LoanAmt


        return  GlassCovAmt, ExtLiabAmt, LoanAmt, TotExtCost

def CalcMonthlyPayment():
        global MonthPay
        global DownPay

        if PayMeth == 'D':
            DownPay = input("Enter the down payment amount: ")
            try:
                DownPay = float(DownPay)
                MonthPay = ((TotalCost - DownPay) + MONTHLY_PRCSSING_FEE) / 8
            except:
                print("Data Entry Error - down payment must be a numeric value")
        elif PayMeth == 'M':
            DownPay = "N/A"
            MonthPay = (TotalCost + MONTHLY_PRCSSING_FEE) / 8
        else:
            DownPay = "N/A"
            MonthPay = 0
        
        return MonthPay, DownPay

def ValidateDateFormat(DateStr, FormStr):
        try:
            datetime.datetime.strptime(DateStr, FormStr)
            return True
        except:
            return False 
        
def CalcMonthPayDate():
        global InvDate
        global FirstMonPayDate

        InvDate = datetime.datetime.now()

        FirstMonPayDate = (InvDate.replace(day=1) + timedelta (days=32)).replace(day=1)

        return FirstMonPayDate, InvDate

# initialize list
ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
PayMethLst = ["F", "M", "D"]

# Main Program.
while True:
    # Gather user imputs.
    print("")
    print("ONE STOP INSURANCE COMPANY - INSURANCE POLICY PROGRAM")
    print("")
    print("CUSTOMER INFORMATION")
    print("")
    while True: 
        FirstName = input("Enter customer first name: ").title()
        if FirstName == "":
            print("Data Entry Error - first name cannot be blank")
        else:
            break

    while True:
        LastName = input("Enter customer last name: ").title()
        if LastName == "":
            print("Data Entry Error - last name cannot be blank")
        else:
            break

    while True:
        StrAdd = input("Enter customer street address: ").title()
        if StrAdd == "":
            print("Data Entry Error - street address cannot be blank")
        else:
            break

    while True: 
        City = input("Enter customer city: ").title()
        if City == "":
            print("Data Entry Error - city cannot be blank")
        else:
            break
    
    while True:
        Prov = input("Enter the customer province (XX): ").upper()
        Prov = Prov.replace(".","")
        if Prov == "":
            print("Data Entry Error - province cannot be blank.")
        elif len(Prov) != 2:
            print("Data Entry Error - province must be 2 characters only.")
        elif Prov not in ProvLst:
            print("Data Entry Error - invalid province entered")
        else:
            break

    while True:
        PostCode = input("Enter customer postal code (L0L-0L0): ").upper()
        if PostCode == "":
            print("Data Entry Error - postal code cannot be blank")
        elif len(PostCode) != 6:
            print("Data Entry Error - postal code must be 6 characters only")
        else:
            break

    
    while True: 
        PhoNum= input("Enter customer phone number (999-999-9999): ")
        if len(PhoNum) != 10:
            print("Data Entry Error - please enter phone number in provided format. ")
        elif PhoNum == "":
            print("Data Entry Error - phone number cannot be blank")
        elif (PhoNum).isdigit == False:
            print('Data Entry Error - phone number must be digits')
        else:
            break
    
    print("")
    print("POLICY INFORMATION")
    print("")
    while True: 
        NumInsu = input("Enter the number of cars being insured : ")
        try:
            NumInsu = int(NumInsu)
        except:
            print("Data Entry Error  - number of cars insured must be a numeric value")
        else:
            if NumInsu == "":
                print("Data Entry Error  - number of cars cannot be blank")
            elif NumInsu < 1:
                print("Data Entry Error - number of cars insured must be 1 or greater")
            break
    
    while True: 
        ExtLia =  input("Would you like to apply optional extra liability (Y/N)?: ").upper()
        if ExtLia != "Y" and ExtLia != "N":
            print("Data Entry Error - extra liability answer must be 'Y or 'N'")
        elif ExtLia == "":
            print('Data Entry Error - extra liability option cannot be blank')
        else:
            break 
    
    while True: 
        GlassCov =  input("Would you like to apply optional glass coverage(Y/N)?: ").upper()
        if GlassCov != "Y" and GlassCov != "N":
            print("Data Entry Error  - glass coverage must be 'Y' or 'N'")
        elif GlassCov == "":
            print('Data Entry Error  - glass coverage option cannot be blank')
        else:
            break 
    
    while True: 
        LoanCar =  input("Would you like to apply optional loan cars(Y/N)?: ").upper()
        if LoanCar != "Y" and LoanCar != "N":
            print("Data Entry Error - loan car must be 'Y' or 'N'")
        elif LoanCar == "":
            print('Data Entry Error - loan car option cannot be blank')
        else:
            break 
    
    while True:
        PayMeth = input("How is the customer paying? Enter 'F' for in full, 'M' for monthly payments and 'D' for down payment: ").upper()
        if PayMeth not in PayMethLst:
            print("Data Entry Error - pay option must be 'F','M' or 'D'")
        elif PayMeth == "":
            print('Data Entry Error - pay option cannot be blank')
        else: 
            break
    
    # Calculations.
        
    DisAmnt = (BASIC_PREM_COST / (1 + EXTRA_CAR_DISCOUNT_RATE)) 

    InsPrem = BASIC_PREM_COST + ((NumInsu - 1) * DisAmnt)

    GlassCovAmt, ExtLiabAmt, LoanAmt, TotExtCost = CalcExCost(NumInsu, GlassCov, ExtLia, LoanCar)

    TotInsPrem = InsPrem + TotExtCost

    HST = TotInsPrem * HST_RATE

    TotalCost = TotInsPrem + HST

    MonthPay, DownPay = CalcMonthlyPayment()

    if PayMeth == "D":
        DownDsp = FV.FComma2(DownPay)
    else:
        DownDsp = "N/A"

    if MonthPay == "F":
        MonthPayDsp = "Paid in Full - No Payments Due"
    else:
        MonthPayDsp = FV.FComma2(MonthPay)
    
    
    # Gathering previous claim information.
    PrevClaimLst = []

    print("")
    print("PREVIOUS CLAIM INFORMATION")
    print("")

    while True: 
            while True: 
                ClaimNum = input("Enter customer claim number (99999): ")
                if ClaimNum == "":
                    print('Data Entry Error - claim number cannot be blank')
                elif len(ClaimNum) != 5:
                    print("Data Entry Error - claim number must be 5 digits only")
                else:
                    break
            while True: 
                ClaimDate = input ("Enter claim date (YYYY-MM-DD): ")
                if ClaimDate == "":
                    print("Data Entry Error - claim date cannot be blank")
                elif ValidateDateFormat(ClaimDate, "%Y-%m-%d") == False:
                     print("Data Entry Error - please enter claim date in provided format")
                else:
                    break
            while True: 
                ClaimAmt = input("Enter the total of previous claim for current customer: ")
                
                ClaimAmt = ClaimAmt.replace("$","")
                ClaimAmt = ClaimAmt.replace(",","")
                ClaimAmt = ClaimAmt.replace(".","")
                ClaimAmt = float(ClaimAmt)
                if ClaimAmt == "":
                    print("Data Entry Error - amount of previous claims cannot be blank")
                else:
                    break 
            PrevClaimLst.append((ClaimNum, ClaimDate, ClaimAmt))
            break 
    while True:
        continue_opt = input("Would you like to process another claim for customer? Enter Y / N: ").upper()
        if continue_opt == "":
            print("Data Entry Error - continue option cannot be blank")
        elif continue_opt != "Y" and continue_opt != "N":
            print("Data Entry Error - continue option must be 'Y' or 'N'")
        elif continue_opt == "Y":
            continue
        else:
            break
            break 
    for ClaimNum, ClaimDate, ClaimAmt in PrevClaimLst:
        print(f"                {ClaimNum:<7}            {ClaimDate:<12}         ${float(ClaimAmt):>.2f}")
    FirstMonPayDate, InvDate = CalcMonthPayDate()

    FirstMonPayDsp = FirstMonPayDate.strftime("%Y-%b-%d")

    InvDateDsp = InvDate.strftime("%Y-%b-%d")


     # display results to user in the form of a receipt 
    print(f"")
    print(f"")
    print(f"")
    print(f"--------------------------------------------------------------------------------")
    print(f"                                                                                ")
    print(f"                          ONE STOP INSURANCE COMPANY                            ")
    print(f"                      Customer Insurance Policy Receipt                         ")
    print(f" {POLICY_NUM}                                                  Invoice Date: {InvDateDsp:<9s}")
    print(f"--------------------------------------------------------------------------------")
    print(f" Customer Name  : {FirstName:<} {LastName:<}                     Phone Number: {PhoNum:<7s} ")
    print(f" Customer Adress: {StrAdd:<}, {City:<}                                      ")
    print(f"                  {PostCode:<}, {Prov:<}                                 ")
    print(f"--------------------------------------------------------------------------------")
    print(f" POLICY INFORMATION                                                             ")
    print(f"--------------------------------------------------------------------------------")                
    print(f" Number of Cars on Policy:                                                 {NumInsu:>4d}")
    print(f" Optional Extra Liability:                                        {FV.FComma2(ExtLiabAmt):>13s}")
    print(f" Optional Glass Coverage :                                        {FV.FComma2(GlassCovAmt):>13s} ")
    print(f" Optional Loan Car       :                                        {FV.FComma2(LoanAmt):>13s} ")
    print(f"")
    print(f" TOTAL EXTRA COST:                                                {FV.FComma2(TotExtCost):>13s}")
    print(f"--------------------------------------------------------------------------------")               
    print(f"                                PRICE BREAKDOWN                                 ")
    print(f"--------------------------------------------------------------------------------")
    print(f" Inital Price for First Car                   :                      {FV.FComma2(BASIC_PREM_COST):>10s}            ")
    print(f" Discounted Price for Additonal Cars on Policy:                      {FV.FComma2(DisAmnt):>10s}                  ")
    print(f" Insurance Premium - Before Extra Costs       :                      {FV.FComma2(InsPrem):>10s}              ")
    print(f" Total Insurance Premium                      :                      {FV.FComma2(TotInsPrem):>10s}            ")
    print(f"--------------------------------------------------------------------------------")                
    print(f"               HST: {FV.FComma2(HST):>10s}         Total Cost: {FV.FComma2(TotalCost):>13s}        ")
    print(f"--------------------------------------------------------------------------------")                
    print(f" Payment Option :  {PayMeth}                 Down Payment  : {DownDsp:<9s}")
    print(f" Monthly Payment:  {MonthPayDsp:<10s}        First Pay Date: {FirstMonPayDsp:<9s}")
    print(f"--------------------------------------------------------------------------------")
    print(f"                           PREVIOUS CLAIM INFORMATION                           ")
    print(f"               -------------------------------------------------                ")
    print(f"                Claim #            Claim Date            Amount                 ")
    print(f"               -------------------------------------------------                ")

    for ClaimNum, ClaimDate, ClaimAmt in PrevClaimLst:
        print(f"                {ClaimNum:<7}            {ClaimDate:<12}       ${ClaimAmt:>.2f}")
    print(f" ")
    

    # save data to text file and 

    print("your claim is being processed and saved. please wait...")

    for _ in range(3):
        print("")
        print('saving claim data ...', end='\r')
        time.sleep(1)  
        sys.stdout.write('\033[2K\r')

    f = open("Claims.dat", "a")

    f.write("{}, ".format(str(POLICY_NUM))) 
    CustName = FirstName + " " + LastName
    f.write("{}, ".format(CustName)) 
    cust_add = StrAdd + " " + City + " " + PostCode + " " + Prov
    f.write("{}, ".format(cust_add)) 
    f.write("{}, ".format(PhoNum)) 
    f.write("{}, ".format(NumInsu)) 
    f.write("{}, ".format(ExtLia)) 
    f.write("{}, ".format(GlassCov)) 
    f.write("{}, ".format(LoanCar))
    f.write("{}, ".format(PayMeth))
    f.write("{}\n, ".format(str(TotInsPrem)))


    # increase policy number by 1 each time a new policy is entered 
    POLICY_NUM += 1

    # Any HouseKeeping to be done before the program ends.
    while True:
        print("")
        EndOption = input("Would you like to process another claim for customer? Enter Y / N: ").upper()
        if EndOption == "":
            print("Data Entry Error - continue option cannot be blank")
        elif EndOption !="Y" and EndOption != "N":
            print("Data Entry Error - continue option must be 'Y' or 'N'")
        else:
            break

    if EndOption == "N":
        print("")
        print("Thank you for using One Stop Insurance Company's Program!")
        print("")
        break 
    



    


