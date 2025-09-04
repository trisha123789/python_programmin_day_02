
def check(n):
    if n >2:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True
    




n = int(input())
for i in range(1,n+1):
    if(check(i)):
    
        print(i)
    