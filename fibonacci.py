n =int(input(" enter the number of terms you want to find : "))

a=0
b=1
temp=0
count=0

if n<0 :
    print ("please enter a positive number")
else :
    print("the fibonacci series of the given number of term is : \n ")
    while count<n :  #loop for calculating fibonacci series
        print(a)
        temp=a+b
        a=b
        b=temp
        count=count+1
