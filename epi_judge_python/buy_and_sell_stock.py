from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    profit = 0.0
    if not prices:
        return profit
    buy = prices[0]
    for i in range(1, len(prices)):
        buy = min(buy, prices[i])
        profit = max(profit, prices[i] - buy)
    return profit


if __name__ == '__main__':
    # prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    # print(buy_and_sell_stock_once(prices))
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
