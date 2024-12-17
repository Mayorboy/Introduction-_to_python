def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        normal_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = normal_pay + overtime_pay
    return pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate per hour: "))

gross_pay = computepay(hours, rate)
print("Pay", gross_pay)

