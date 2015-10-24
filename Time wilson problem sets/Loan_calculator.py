def payment_sched(monthly_payment,amount,inst_count):
    print ("         Amount     Remaining")
    print ("Pymt#     Paid       Balance ")
    print ("-----    ------     ---------")

    for payment_number in range(0,int(inst_count)+1):
        if payment_number == 0:
            monthly_inst = 0
        else:
            monthly_inst = monthly_payment
        amount = amount - monthly_inst
        print (" %2d      $ %4.2f      $ %6.2f ") % (payment_number,monthly_inst,abs(amount))
        
def calc_interest(amount,rate,years):
    f_amount = float(amount)
    f_rate   = float(rate)
    f_years  = float(years)
    interest = f_amount * (f_rate/100) * f_years
    total_amount = f_amount + interest
    number_of_inst = f_years * 12
    monthly_payment = (total_amount/number_of_inst)

    print "Amount borrowed    : $%6.2f" % f_amount
    print "Total interest paid: $%6.2f" % interest
    print "monthly installment: $%6.2f" % monthly_payment
    print "Total amount       : $%6.2f" % total_amount
    
    payment_sched(monthly_payment,total_amount,number_of_inst)

def main():
    print ("Loan calculator")
    amount = raw_input("Amount borrowed: ")
    interest_rate = raw_input("Interest rate  : ")
    term = raw_input("Term (years)   : ")

    calc_interest(amount,interest_rate,term)

if __name__ == '__main__': main()
