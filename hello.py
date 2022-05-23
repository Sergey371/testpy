from decimal import Decimal

print('Hello, World!')

D = Decimal("2312")

print("Нетто         : " + str(D))
print("Нетто в 10 шт.: " + str(D(netto * 10)))
