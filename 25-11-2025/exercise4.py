nums=[10,11,12,13,17,20,23]
num=[]
count=0
for i in range(len(nums)):
    count=0
    for j in range(2,nums[i]):
        if nums[i]%j==0:
            count=count+1
    if count==0:
        num.append(nums[i])
print(num)
