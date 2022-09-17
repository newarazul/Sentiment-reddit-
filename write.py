from datetime import date
import pandas as pd
import pandas_datareader.data as web
import datetime




def get_SP500_daily(date):
    SP500=web.DataReader(["sp500"], "fred", start,end)
    for i in SP500:
        Percent.append(



def getSP500_value(start,end):
    SP500=web.DataReader(["sp500"], "fred", start,end)
    print(SP500)
    return SP500


def getcurrentDate():
    current_date=date.today()
    print(current_date)
    return current_date

def print_Date(current_date):
    print("Today is the:", current_date)




def write_to_file(name,values):
    with open(name, "w") as writer:
        for i in values:
            writer.write(str(i)+"   ")


#data=(5, 6, 7)
#write_to_file("value.dat",data)


#print_Date(getcurrentDate())

hmvalue = datetime.datetime(2021, 1, 11)
dmvalue = datetime.datetime(2021, 1, 12)

#getSP500_value(hmvalue,dmvalue)

