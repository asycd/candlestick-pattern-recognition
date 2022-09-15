# If you don't have 'pandas' or 'mplfinance' installed on your system
# python -m pip install mplfinance
# python -m pip install pandas

#importing libaries
import pandas as pd
import mplfinance as mpf


# Unpacking the price data
df = pd.read_csv(r'C:\Users\user\Documents\Financial Data Analysis using Python\Candlestick Pattern Recognition Project\BTC-USD Data.csv')

# Manipulating the Data
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df.dropna() #drops NaN values

print(df.head())
print(df.describe())

# Plot
mpf.plot(df, type="candle", title = 'BTC-USD Candlestick Pattern 2021-2022', volume = True, mav = (10,20), savefig='BTC-USD Advanced Candlestick Chart.png')  # You need the whole dataframe for candlestick data

# Depending on the direction of price change, I want to have a candle column that is either +1 or -1
# We can then look for patterns in the column


df['candle'] = 0 # intializing the 'ticker' column
# Counting the candles
count_negative = 0 
count_postive = 0
count_equal = 0


for i in range(1,len(df)):
    if df['Close'].iloc[i] < df['Close'].iloc[i-1]:
        df['candle'].iloc[i] = -1
        count_negative += 1
        
    elif df['Close'].iloc[i] > df['Close'].iloc[i-1]:
        df['candle'].iloc[i] = 1
        count_postive += 1
        
    else:
        df['candle'].iloc[i] = 0 # else equal
        count_equal += 1


print('The number of positive candles is ' + str(count_postive))
print('The number of negative candles is ' + str(count_negative))
print('The number of equal candles is ' + str(count_equal))




candles = list(df['candle']) # creating a list of candles
# finding the longest sequence
print(candles) # outputs a list of +1's and -1's

# 'longest_run' computes the longest run of negative candles or positive candle
def longest_run(candles):

    maxCount = 1 # intializing the 'maxCount' variable
    actualCount = 1 # initializing the 'actualCount' variable

    for i in range(len(candles)-1):
        if candles[i] == candles[i+1]:
            actualCount += 1
        else:
            actualCount = 1
        if actualCount > maxCount:
            maxCount = actualCount

    return(maxCount)
print('The longest sequence of candles in any direction is ' + str(longest_run(candles)))  

# 'longest_positive_or_negative' is computes the largest sequence in both directions and returns it
def longest_positive_or_negative(candles):
    maxPositive = 1
    actualPositive = 1
    maxNegative = 1
    actualNegative = 1

    for i in range(1,len(candles)):
        if candles[i] == candles[i-1] and candles[i] == 1:
            actualPositive += 1
        else:
            actualPositive = 1
        
        if candles[i] == candles[i-1] and candles[i] == -1:
            actualNegative += 1
        else:
            actualNegative = 1
        
        if actualPositive > maxPositive:
            maxPositive = actualPositive
        if actualNegative > maxNegative:
            maxNegative = actualNegative

    return maxPositive,maxNegative
result = longest_positive_or_negative(candles)
print('The longest positive sequence is ' + str(result[0]))
print('The longest negative sequence is ' + str(result[1]))




        













