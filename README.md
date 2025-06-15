# QUANT_ALGORITHMS
Using mathematical concepts to turn a profit in the stock market


This is a simple mathematical algorithm that uses z scores of the past 20 ticks from the current tick and the current tick as well as the maximum volume from the past ticks to compare to the current tick volume
The Z-Score is calculated taking the previous 20 ticks' rolling mean as well as standard deviation to determinte the risk and volatility of current tick's shares.
Through testing over various parameter, I have determined the HOLD signal threshold to be -0.3 to 1.3, z scores on either side of these boundaries sends a BUY and a SELL signal respectively
During backtesting of various popular stocks (AAPL, AMZN, MSFT, etc.), the buy/sell percentages were inclined at buying shares worth 90% of our current amount and selling at least 1 share or 35% of our shares, whatever is the valid case.
In an added condition, even if the Z-Score is not favourable but current previous tick volume lies within a 15% margin of the max volume of previous 20 ticks, a buy or sell order will be made, according to stance.
Backtesting has revealed a return of almost 0.35% in a day on a single stock 

NOTE: The algorithm seems to perform especially well on relatively volatile stocks when intraday trading over a duration of 5 or more days seein upwards of 1.5% returns in that time period