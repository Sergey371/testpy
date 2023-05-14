# -*- coding: utf-8 -*-
"""Hello World test script."""

from decimal import Decimal

print('Hello, World!')

D = Decimal("2312")

print("Нетто         : " + str(D))
print("Нетто в 10 шт.: " + str(D * 10))

X = 0.1 + 0.1 + 0.1
print(X)
print("----------------------")
X = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(X)
