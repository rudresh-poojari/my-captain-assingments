s = input("please enter a string ")
counts=dict()
for l in s :
    if l not in counts :
        counts[l]=1
    else :
        counts[l]=counts[l]+1

for n in counts :
    print(n,counts[n])
