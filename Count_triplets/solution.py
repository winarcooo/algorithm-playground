def countTriplets(arr, n):
    arrLength = len(arr)
    ratio = n
    counter = 0
    for i in range(arrLength - 2):
        firstnum = arr[i]
        for j in range(i+1, arrLength - 1):
            secondnum = arr[j]
            if secondnum != firstnum * ratio: continue
            
            for k in range(j+1, arrLength):
                thirdnum = arr[k]
                if thirdnum != secondnum * ratio: continue

                counter += 1
    
    return counter


            


if __name__ == "__main__":
    arr = [1,3,9,9,27,81]
    arr1 = [1,2,2,4]
    n = 2

    countTriplets(arr1, n)
