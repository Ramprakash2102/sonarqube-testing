# FIBONACCI SERIES - FUNCTION
def fibo_fni(n):
  if n <= 0:
     return
     print("Given number of terms should be greater than zero")
  a, b = 0, 1
  for _ in range(n):
     print(a, end=" ")
     a, b = b, a+b
  print("\n")

# DRIVER CODE
n = int(input("Enter the number of terms: "))
fibo_fni(n)
