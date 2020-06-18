def whatFlavors(costs, money):
    table = []

    for i, cost in enumerate(costs):
        need = money - cost

        if cost in table: return (table[cost], i+1)
        
        table[need] = i+1

    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        # m = 6
        # ice = [1,3,4,5,6]

        # result = index 1 and 4

        print(whatFlavors(cost, money))