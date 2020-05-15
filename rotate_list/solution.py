def rightRotate(nums, k): 
    if(len(nums)==1):
            return

    k = k % len(nums)
    for i in range(len(nums) - k):
        nums.append(nums.pop(0))
        print(nums)


rotate_num = 1
list_1 = [1, 2, 3, 4, 5, 6] 
  
print(rightRotate(list_1, rotate_num))



# print(list_1.pop(2))