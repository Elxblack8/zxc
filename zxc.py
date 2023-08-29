z=int(input("Enter Your First number: "))
print()
x=int(input("Enter Your list number: "))

start = z
end = x
print()
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    
    if num > 1:
        for i in range(2, num):
           
            if (num % i) == 0:
                
                break
        else:
            print(num)
