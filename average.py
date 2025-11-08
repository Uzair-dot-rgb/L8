a = int(input("Enter your speed of the first person : "))
b = int(input("Enter your speed of the second person : "))
c = int(input("Enter your speed of the third person : "))
avg = (a+b+c)/3
print("The average speed is ", avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b , c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b , c))
elif avg > a:
    print("%d is higher than %d" %(avg, a))
elif avg > b:
    print("%d is higher than %d" %(avg, b))
elif avg > c:
    print("%d is higher than %d" %(avg, a))
else :
    print("Ivalid input.")