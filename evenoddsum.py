n=int(input("Enter size : "))
ar=[1,2,3,4,5,6]
evensum=0
oddsum=0
for i in range(n):
    if(ar[i]%2==0):
        evensum=evensum+ar[i]
    else:
        oddsum=oddsum+ar[i]
print(oddsum,evensum)
        