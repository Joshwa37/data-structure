arr=[-1,4,3,5,2,1,4,-3,6,98]
k=3 #sliding window range that the array should slide
l=0 #l is a one pointer that start first
m=k-1 #m is a second pointer that point the last element of range K-1 to slide through the range
sum=0 #find the maximum value for slide through 3 element
maxsum=0
in1=0 #index position which has large value
in2=0
for i in range(0,k):
        sum=sum+arr[i]
while(i<len(arr)-1):
        sum=sum-arr[l]
        l+=1
        m+=1
        sum=sum+arr[m]
        if(maxsum<sum):
            in1=l
            in2=m
            maxsum=sum
        i+=1
print(maxsum,in1,in2)
        