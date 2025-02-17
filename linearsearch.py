def linear(list,n):
    i=0
    while i<len(list):
        if(list[i]==n):
            return True
        i+=1
    return False

list=[1,2,3,4,5,6,7,8,9,0]
n=9
if linear(list,n):
    print("got it")
else:
    print("not found")