# 下面的字典中保存了某些公司的股票代码及股票价格。
"""
美股的股票代码是指英文字母代码，如：AAPL、GOOG。
"""
prices = {
    "AAPL":191.88,
    "GOOG":1186.14,
    "IBM":149.24,
    "ORCL":48.44,
    "ACN":166.89,
    "FB":208.09,
    "SYMC":21.29
}
# 输出价格最高的股票对应的股票代码。
print(max(prices,key=lambda x:prices[x]))
# 用股票价格大于100的股票创建一个新的字典。
stoks = {key: value for key,value in prices.items() if value > 100}
print(stoks)

# 按股票价格从高到低输出股票代码。
sorted_stocks = sorted(prices,key=lambda x:prices[x],reverse = True)
for code in sorted_stocks:
    print(code)