list1=[30,27,25,22,55,51]

for i in range(0,len(list1)):
    if list1[i]%3==0 and list1[i]%5==0:
        continue

    else:
        if list1[i]%3==0 or list1[i]%5==0:
            print(list1[i])
