pay = int(input("시간당 : "))
wtime = float(input("일한 시간 : "))

total = int(pay * wtime)
tax = int(total * 0.03)

print("시간당 %d원, %.1f시간 일함" % (pay, wtime))
print("세금 %d원, 총액 %d원" % (tax, total-tax))