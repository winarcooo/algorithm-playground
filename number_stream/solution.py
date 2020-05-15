def number_stream(nums):

    numList = list(map(int,nums))
    listLength = len(numList)
    
    stash = []
    for i in range(listLength):
        stash = [numList[i]]
        for j in range(i+1, listLength):
            if stash[-1] == 1:
                return True
            
            if numList[i] == numList[j]:
                stash.append(numList[i])

                if len(stash) >= stash[0]:
                    return True
            else:
                break

    return False

if __name__ == "__main__":
    testCase = input()
    number_stream(testCase)
