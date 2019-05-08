def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 2
    if num == 0:
        fib = []
    elif num == 1:
        fib = [0]
    elif num == 2:
        fib = [0,1]
    elif num > 2:
        fib = [0,1]
        while i < num:
            fib.append(fib[i-1] + fib[i-2])
            i += 1
    return fib

print(fibonacci())
