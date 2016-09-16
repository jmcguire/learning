
def max_profit(prices):
    """get the maximum profit from buying and selling stock"""

    max_profit = None
    lowest_price = None
    highest_price = None

    for price in prices:
        print "checking ", price

        # if we have a new lowest price, grab it and reset out highest
        if not lowest_price or price < lowest_price:
            lowest_price = price
            highest_price = None
            print "\tnew lowest_price ", price

        # if we have a new highest, grab it and calculate the profit
        elif not highest_price or price > highest_price:
            highest_price = price
            profit = highest_price - lowest_price
            print "\tnew highest_price ", price
            print "\tpossible profit ", profit

            # check for a new max_profit
            if not max_profit or max_profit < profit:
                max_profit = profit
                print "\tnew max_profit ", profit

    return max_profit or 0

prices = [10, 5, 3, 7, 11, 1, 4]
bad_prices = [5, 4, 3, 2, 1]

profit = max_profit(prices)

print "maximum profit: ", profit

