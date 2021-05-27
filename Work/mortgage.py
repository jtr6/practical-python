# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    payment = base_payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment += extra_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment    
    month += 1
    print(month, round(total_paid,4) , round(principal, 4))

if principal < 0:
    total_paid = total_paid + principal

print('Total paid', round(total_paid, 4), " in {} months".format(month))