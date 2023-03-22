price = int(input("기계값 입력 : "))
used = int(input("사용 개월 수 : "))

mpay = float(price / 24)
left = 24 - used

print("매달 내는 돈 = %d" % mpay)
print("남은 약정기간 = %d개월" %left)
print("위약금 = %.1f원" % float(mpay * left))