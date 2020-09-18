# Author: Jonathan Ahn jxa5570@psu.edu  
def digit_sum(n):
  if n<= 0:
    return 0
  else:
    return n%10+digit_sum(n//10)

n = int(input("Enter an int: "))
s = int(digit_sum(n))
print(f"sum of digits of {n} is {s}.")
