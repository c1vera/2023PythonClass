st_price = int(input("기본 통신비 : "))
st_data = int(input("기본 데이터량 : "))
add_price = int(input("1기가당 추가 통신비 : "))
used = int(input("한 달 기본 사용량 : "))

left = used - 5
total = int(st_price + add_price * left)

print("\n%d기가까지 %d원" % (st_data, st_price))
print("%d기가 사용하면 %d원\n" % (used, total))

if (total > 76000) :
    print("76000원의 무제한 요금제를 추천합니다.")
else :
    print("42000원의 특판 요금제를 추천합니다.")