def jump(list,n,m):
    i=0
    l=m
    while l<len(list):
        if(l>len(list)):
            l=len(list)-1
        if n>=list[i] and n<list[l]:
            for i in range(i,l+1):
                if(list[i]==n):
                    return True
        else:
            i=l
            l=l+m
        if(l>len(list)):
            return False
list=[0,1,2,3,4,5,6,7,8,9]
n=6
m=1
if jump(list,n,m):
    print("got it")
else:
    print("not found")

    