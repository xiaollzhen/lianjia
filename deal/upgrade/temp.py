# -*- coding: utf-8 -*-
import pandas as pd


if __name__ =="__main__":

    df_base = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/城六区存量.csv')
    df_up = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/upgrade/城六区增量.csv')

    dataframe = [df_base, df_up]
    result = pd.concat(dataframe)
    print('old lines:=' + str(len(result)))
    newresult = result.drop_duplicates()
    print('new lines:='+str(len(newresult)))

    newresult.to_csv('城六区存量new.csv', encoding='UTF-8', index=False)




