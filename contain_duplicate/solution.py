def containsDuplicate(nums):
    for i in range(len(nums)):
        start = i+1
        if start > len(nums):
            return False
        
        print(nums[start:len(nums)])
        if nums[i] in nums[i+1:len(nums)]:
            return True
        
    return False

print(containsDuplicate([2,14,18,22,22]))