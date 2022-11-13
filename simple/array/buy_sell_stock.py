class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        arr_len = len(prices)
        arr_profits: list[int] = []
        idx = 0

        while idx < arr_len:
            price = prices[idx]

            arr_to_compare = prices[idx+1:]

            seq_max_price_tracker: int = 0
            seq_max_price_tracker_idx: int = 0

            for next_idx, next_price in enumerate(arr_to_compare):
                if price < next_price and seq_max_price_tracker < next_price:
                    seq_max_price_tracker = next_price
                    seq_max_price_tracker_idx = next_idx + idx + 1
                else:
                    break

            if not seq_max_price_tracker == 0:
                arr_profits.append(seq_max_price_tracker - price)
                idx = seq_max_price_tracker_idx + 1
            else:
                idx += 1

        print(arr_profits)
        max_profit: int = sum(arr_profits) if arr_profits else 0
        return max_profit


solution = Solution()

print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
