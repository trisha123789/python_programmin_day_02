def fact(n):
    p =1
    for i in range(1,n+1):
        p = p *i
    return p
def strong(i):
    temp = i
    sum = 0
    while(temp > 0):
        rem = temp %10
        sum = sum + fact(rem)
        temp = temp //10
    if sum == i:
        return True
    else:
        return False
    





n = int(input())
for i in range(1,n+1):
    if strong(i):
        print(i)