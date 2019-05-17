#!/usr/bin/env python3

# def Prime_Num():
#     return int(input("Give me a number: "))
#    if Prime_Num % == 0
#         print ("Not a Prime Number")
#
# else:
#  print ( "Prime Number")

# Tests:
# normal cases:
## 6 - not prime
## 7 - prime
## 0 or - ask business
## -ve - ask business
## 9 - square
## 12 - more than

#num = int(input("enter an integer: "))
def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

#safe_cast('tst', int, 0) # will return 0

import sys
num = 0
if(len(sys.argv) > 1):
    num = safe_cast(sys.argv[1], int, 0)

if(num == 0):
    num = int(input("enter an integer: "))

isPrime = True
for i in range(2, num-1):
    if num % i  == 0:
        isPrime = False
        break

if(isPrime):
    print("Prime number")
else:
    print("not prime")
