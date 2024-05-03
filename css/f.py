def fun():    
    hs = {}
    arr = [1,5,3,4,3,5,6]
    for i in range(0,len(arr)):
        if arr[i] in hs:
            print(hs[arr[i]]+1)
            break
        else:
            hs[arr[i]] = i

fun()