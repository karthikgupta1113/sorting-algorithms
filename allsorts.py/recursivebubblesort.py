
def recursiveBubbleSort(nums,n):
    if n==1:
        return 
    for i in range(n-1):
        if(nums[i]>nums[i+1]):
            nums[i],nums[i+1]=nums[i+1],nums[i]
    recursiveBubbleSort(nums,n-1) 
    return nums

    

        

    