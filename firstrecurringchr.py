arr = [2,1,9,3,1,4,5,6]
arr2=[]
for x in arr:
    if x in arr2:
        print(x)
        break
    arr2.append(x)