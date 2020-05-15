def stock_prices(prices):
    margin = []
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                margin.append(profit)
    
    if not margin:
        return -1

    return max(margin)

if __name__ == "__main__":
    prices = [1,4,3,2,1]
    print(stock_prices(prices))