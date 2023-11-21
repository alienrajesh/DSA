# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and
#              sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 
# is not allowed because you must buy before you sell.

import time

prices = [2,1,2,1,0,1,2]

# the given below algo fails at the above test case
def maxProfit(prices: list[int]) -> int:
     
    l = min(prices)
    min_l_i = prices.index(l)
    max_profit = 1
    for i in range(min_l_i,len(prices)):
        max_profit = max(max_profit,prices[i]-prices[min_l_i])
        
    return max_profit

    
# print(maxProfit(prices))    

# timeout error
def maxProfit1(prices: list[int]) -> int:

    start = time.time()
    max_profit = 0
    
    for i , v  in enumerate(prices):
        
        for j in range(i+1,len(prices)):
            max_profit = max(max_profit ,prices[j] - v)
    
    end = time.time()
    print("time = " ,(end-start))
    return max_profit    
        

# print(maxProfit1(prices)) 


def maxProfit2(prices:list[int]) -> int:
    l , r = 0 , 1
    
    maxprofit = 0
    
    while r <= len(prices)-1 :
        
        profit = prices[r] - prices[l]
        
        maxprofit = max(profit,maxprofit)
        
        if prices[l] >= prices[r]:
            l = r 
            r+=1
        else:
            profit = prices[r] - prices[l]
        
            maxprofit = max(profit,maxprofit)
            r+=1
    return maxprofit
    

print(maxProfit2(prices))












