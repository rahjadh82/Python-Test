#Factorial.py
import sys

#Program for finding factorial of a number

input_num = int(sys.argv[1])
print(f"Input number = {input_num}")

if input_num <= 0 :
    fact = 0
else :
    fact = 1;
    while input_num > 0:
        fact = fact * input_num
        input_num -= 1

print(f"Factorial = {fact}")
