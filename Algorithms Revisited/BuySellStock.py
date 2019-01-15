'''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

-------------------------------------------------------------------------
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

def maxProfit(prices):
    print('Prices: ', prices)
    



ex1 = maxProfit([7,1,5,3,6,4])
print('ANSWER: ', 'BUY AT DAY: ', ex1[0], '    SELL AT DAY: ', ex1[1], '   PROFIT: ', ex1[2])

ex2 = maxProfit([7,6,4,3,1])
print('ANSWER: ', 'BUY AT DAY: ', ex2[0], '    SELL AT DAY: ', ex2[1], '   PROFIT: ', ex2[2])



# def maxProfit(prices):
#     print('Prices: ', prices)
#     buy = 0
#     sell = 0
#     diff = 0
#     l = len(prices)
#     for i in range(l):
#         for j in range(i,l):
#             if (prices[j] - prices[i]) > diff and (prices[j] - prices[i]) > 0:
#                 diff = prices[j] - prices[i]
#                 buy = i
#                 sell = j
#             print('BUY: ', i, '   SELL: ', j, '   diff: ', diff)
            
#     return buy, sell, diff

        