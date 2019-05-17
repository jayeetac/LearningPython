num = int(input("Enter max less than 500: "))
for i in range(50):
    if i == num:
        break;
    if i%2 == 0:
        continue;
    print(i)
