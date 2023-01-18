x = 0

def RecursiveNumber(x, y=2):
    if x == 0:
        return y
    else:
        return 5 * RecursiveNumber(x-1) + 2
        

x = int(input("Enter the value of n: "))

for i in range(x):
    print("Num "+str(i+1), "=", RecursiveNumber(i))
    
