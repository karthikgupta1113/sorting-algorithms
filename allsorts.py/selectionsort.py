def selectionSort(nums):
    n=len(nums)
    for i in range(n-1):
        minIndex=i
        for j in range(i+1,n):
            if nums[j]<nums[minIndex]:
                minIndex=j

        nums[minIndex],nums[i]=nums[i],nums[minIndex]    
    return nums