def recursiveSelectionSort(nums,n):
    if n<=1:
        return
    recursiveSelectionSort(nums,n-1)
    last=nums[n-1]
    j=n-2
    while j>=0 and last<nums[j]:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=last 
    return nums
     

# nums=[4,3,1,2,6,5] 

    