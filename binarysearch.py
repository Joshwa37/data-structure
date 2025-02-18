pos=-1
def binary(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2

        if(list[mid]==n):
            pos=mid
            return True
        else:
            if(list[mid]<n):
                l=mid
            else:
                u=mid
        if(l+2==u):
            return False
    return False
list=[0,1,2,3,4,5,6,7,8,9]
n=10
if binary(list,n):
    print("got it")
else:
    print("not found")