# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

extra_payment_start_month = int(input('set month to start payment: '))
extra_payment_end_month = int(input('set month to end payment: '))
extra_payment = int(input('set payment: '))

while principal > 0:
    if extra_payment_start_month < month and extra_payment_end_month > month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:    
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    month = month + 1

    if principal < 0:
        total_paid = total_paid + principal
        principal = 0

    print(month,round(total_paid,2),round(principal,2))

tp = f'Total paid {total_paid}'
m = f'Months {month}'
print(tp)
print(m)