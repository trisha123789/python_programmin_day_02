def check(n):
    if n >=65 and n <=90 or n >=97 and n <=125:
        return "character"
    elif n >48  and n <55:
        return "digit"
    else:
        return "special character"
    








n = ord(input())
a = check(n)
print(a)