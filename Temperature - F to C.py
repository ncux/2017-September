# apparently 104F = 40C
# and 100F = 37C

F = float(input("Enter temperature in Fahrenheit: "))

C = (F-32)/1.8
if C > 30:
   print("It's hot.")
elif C >= 20 and C <= 30:
   print("It's comfortable")
else:
   print("It's cold.")
print(C)






