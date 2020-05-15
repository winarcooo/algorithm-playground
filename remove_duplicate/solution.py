def removeDuplicates(nums):
    uniqueList = []
    
    for num in nums:
        if num not in uniqueList:
            uniqueList.append(num)

    nums[:] = uniqueList
    return nums


print(removeDuplicates([1,1,2]))