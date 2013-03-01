#!/usr/bin/env python
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

"""

d = ''
for n in range(10000000):
    d = d +str(n)
    if len(d) > 10000000:
        break
    else:
        continue
total = int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])
print total
