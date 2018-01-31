"""function to convert temperature from F to C"""

def temperature(F):
    C = (F - 32) / 1.8
    if C > 30:
        print("It's hot.")
    elif C >= 20 and C <= 30:
        print("It's comfortable")
    else:
        print("It's cold.")
    print(C)

temperature(100)










