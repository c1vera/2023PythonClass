person = int(input("MT 인원수: "))

pack = person // 12
bottle = person % 12

print("\n%d 명이 마실 생수를 구매하려면 %d 팩과 낱개 %d 개를 구매하면 됩니다." % (person, pack, bottle))