def check(n):
    if n >=80 and n <=100:
           return  "distinction"
    elif n >=71 and n <=80:
            return "A"
    elif n >=51 and n <=70:
        return  "B"
    elif n <=50 and n >= 40:
        return "C"
    else:
        return "fail"

name = input("enter the name")
num = int(input("enter roll no"))
s1 = int(input("enter marks of first subject"))

s2 = int(input("enter marks of second student"))
s3 = int(input("enter the marks of third student"))
print(check(s1))
print(check(s2))
print(check(s3))
if check(s1) !=  "fail" and check(s2) !=  "fail" and check(s3) != "fail":
    

    total = s1 +s2+s3
    avg = total/3
    a = round(avg,2)

    print("details")
    print(f"name is {name} num is {num} ")
    print(f"subject1 is {s1} subject2 marks {s2} subject3 {s3}")
    print(f" total is {total} avg is {a}")