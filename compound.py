def compound_interest(p, n):
    if n == 0:
        return 1;
    else:
        return p * compound_interest(p, n-1);

p = int(input("enter the principal growth: "))
n = int(input("enter the number of years: "))
print(compound_interest(p, n))
