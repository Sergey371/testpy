from decimal import Decimal

print('Hello, World!')

D = Decimal("2312")

print(u"Нетто         : " + str(D))
print(u"Нетто в 10 шт.: " + str(D * 10))

x = 0.1 + 0.1 + 0.1
print(x)
print("----------------------")
x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(x)
