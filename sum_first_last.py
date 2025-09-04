n = int(input())
first = -1
last = -1
i =1
while n > 0:
    if(i ==1):
        t = n %10
        n = n/10
first = n
last = t
sum =  first + last
print(sum)

    