num = int(input("How many numbers that generates?:"));
def fibMine (num):
    fibo = []
    a =0
    b =1
    for i in range (num):
        fibo.append(a)
        a,b = b, a+b

    return fibo

print(fibMine(num))
