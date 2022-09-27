import time
import pandas as pd # pip install pandas

tables = []

for i in range(0, 3):
    url = 'https://www.marketwatch.com/tools/stockresearch/screener/results.asp?TradesShareEnable=True&TradesShareMin=10&TradesShareMax=50&PriceDirEnable=False&PriceDir=Up&LastYearEnable=False&TradeVolEnable=False&BlockEnable=False&PERatioEnable=False&MktCapEnable=False&MovAvgEnable=False&MovAvgType=Outperform&MovAvgTime=FiftyDay&MktIdxEnable=False&MktIdxType=Outperform&Exchange=All&IndustryEnable=False&Industry=Insurance&Symbol=True&CompanyName=True&Price=True&Change=True&ChangePct=True&Volume=True&LastTradeTime=True&FiftyTwoWeekHigh=False&FiftyTwoWeekLow=True&PERatio=True&MarketCap=True&MoreInfo=False&SortyBy=Symbol&SortDirection=Ascending&ResultsPerPage=OneHundred&PagingIndex={0}'.format(i*100)
    print('Processing Index {0}'.format(i*100))

    try:
        df = pd.read_html(url)[0]
        tables.append(df)
        time.sleep(1)
    except Exception as e:
        print(e)
        continue

results = pd.concat(tables, axis=0)
results.to_excel('Screen Results.xlsx', index=False)