

def check(n):
    if n ==1:
      if n ==1:
        return "Monday"
    elif n ==2:
        return "Tuesday"
    elif n ==3:
        return "wednesday"
    elif n ==4:
        return "Thursday"
    elif n ==5:
        return "friday"
    elif n ==6:
        return "saturday"
    elif n ==0:
        return "sunday"
    else:
        return -1
        




n = int(input("enter week day number"))
a = check(n)
print("week day is",a)