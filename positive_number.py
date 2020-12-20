l=[]
r = int(input("enter the number of elements you want in list : "))
i=0
while i<r :
    e = int(input("enter a number :  "))
    l.append(e)
    i=i+1

print("positive numbers in given lis of numbers is : ")
for n in l :
    if n>0 :
        print(n)
