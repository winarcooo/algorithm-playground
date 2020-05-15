def mark_and_toys(prices, limit):

    sortedPrices = selection_sort(prices)

    sum = 0
    toysPrices = []
    for price in sortedPrices:
        sum += price
        if sum <= limit:
            toysPrices.append(price)
        else:
            return len(toysPrices)
    
    # return len(toysPrices)

def selection_sort(nums):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    return nums


if __name__ == "__main__":
    # nk = input().split()

    # prices = list(map(int, input().rstrip().split()))

    prices = [1,12,5,111,200,1000,10] 
    print(mark_and_toys(prices, 50))
    