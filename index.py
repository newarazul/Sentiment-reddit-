import pandas as pd
#if you get an error after executing the code, try adding below. pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 1, 27)
SP500 = web.DataReader(['sp500'], 'fred', start, end)

print(SP500)
