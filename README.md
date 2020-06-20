# True Range Stock-Analysis

This program takes the user's input and will do the following analysis.
 - Download stock prices from https://www.alphavantage.co/ via its API (users are required to create a token)
 - Calculate the user's chosen indicator (True Range).
 - Print out a detailed report with the outcome of the analysis.
# The Input
The input will be in the following format:
- The path to the API key
- Stock's ticker symbol
- Date range (start date and end date)
- The True Range Indicator (TR)
    - TR means that the true range indicator will be used. This is followed by a space, followed by a buy threshold, followed       by a space, followed by a sell threshold. Each threshold is described by either a < or a > character, followed by a           percentage, which is a non-negative number (with optional decimal point and decimal places). For example, TR <1.5 >0.5         indicates that the true range indicator should be calculated, that a buy signal should be generated when the true range       is less than 1.5%, and that a sell signal should be generated when the true range is greater than 0.5%.

# Indicator
The core of the analysis is the indicator. In this case, the True Range will be calculated. More info on True Range indicator can be found here https://www.investopedia.com/terms/a/atr.asp

# Signal
The program will generate a sell or buy signal based on the given indicator. 

courtesy to Alex Thornton. 
