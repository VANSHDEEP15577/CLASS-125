
def perfecto(n):
    sum=0
    for i in range(1,n):
        if n % i == 0:
            sum+=n
    if sum == n:
        print(n," IS A PERFECT NO.")
    else:
        print(n," IS NOT A PERFECT NO.")
n=int(input("ENTER THE NO. THAT YOU WANT TO CHECK:"))
perfecto(n)
