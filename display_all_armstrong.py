def armstrong(n):
    temp = n
    sum = 0
    while(temp> 0):
        rem = temp%10
        sum = sum + rem*rem*rem
        temp = temp//10
    if(sum == n):
        return True
    else:
        return False
        
        
        
    

n = int(input())
for i in range(1,n+1):
    if armstrong(i):
        print(i)