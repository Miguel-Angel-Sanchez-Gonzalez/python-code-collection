# Factorial function
def factorial(num):
  if num == 0 or num == 1 :
    return 1
  else :
    return num * factorial(num - 1)
  
# Example
print(factorial(10))