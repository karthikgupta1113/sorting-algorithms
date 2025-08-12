def merge(arr,st,mid,end):
    i=st
    j=mid+1
    nums=[]
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            nums.append(arr[i])
            i=i+1
        else:
            nums.append(arr[j])
            j=j+1
    while i<=mid:
        nums.append(arr[i])
        i=i+1
    while j<=end:
        nums.append(arr[j])
        j=j+1
    for i in range(len(nums)):
        arr[st+i]=nums[i]
def mergeSort(arr,st,end):
    if st>=end:
        return
    mid=(st+end)//2
    mergeSort(arr,st,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,st,mid,end)
    return arr






