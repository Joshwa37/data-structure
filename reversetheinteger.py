class Solution(object):
    def reverse(self, x):
        if(x<0):
            num=-(x)
        else:
            num=x
        copy=x
        rev=0
        rem=0
        while(num>0):
            rem=num%10
            rev=(rev*10)+rem
            num=num//10
        if(copy<0):
            rev=-(rev)
        if(rev>2147483648 or rev<-2147483648):
            return 0
        return rev