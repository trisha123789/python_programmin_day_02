def dev(n):
    if n == 1:
        return "one"
    elif n ==2:
        return "two"
    elif n ==3:
        return "three"
    elif n ==4:
        return "four"
    elif n==5:
        return "five"
    elif  n==6:
        return "six"
    elif n==7:
        return  "seven"
    elif n==8:
        return "eight"
    elif n==9:
        return "nine"
    else:
        return -1
    


n = int(input())
temp = int(str(n)[::-1])
while temp > 0:
    r = temp%10
    print(dev(r))
    temp = temp/10

    
    
    