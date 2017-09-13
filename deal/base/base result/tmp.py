# -*- coding: utf-8 -*-
import pandas as pd


if __name__ =="__main__":
    df1 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/东城2017-08-11 16:07.csv')
    df2 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/丰台2017-08-18 18:40.csv')
    df3 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/朝阳2017-08-06 17:53.csv')
    df4 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/海淀2017-08-07 18:53.csv')
    df5 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/石景山2017-08-20 18:13.csv')
    df6 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/西城2017-08-11 16:02.csv')

    df7 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/亦庄开发区2017-08-27 17:01.csv')
    df8 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/大兴2017-08-26 19:43.csv')
    df9 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/房山2017-08-26 20:03.csv')
    df10 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/昌平2017-08-15 13:51.csv')
    df11= pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/通州2017-08-28 18:00.csv')
    df12 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/门头沟2017-08-26 20:47.csv')
    df13 = pd.read_csv('/Users/lixiao/PycharmProjects/lj/deal/base/base result/顺义2017-08-20 17:24.csv')

    df1['行政区'] = '东城'
    df2['行政区'] = '丰台'
    df3['行政区'] = '朝阳'
    df4['行政区'] = '海淀'
    df5['行政区'] = '石景山'
    df6['行政区'] = '西城'

    df7['行政区'] = '亦庄'
    df8['行政区'] = '大兴'
    df9['行政区'] = '房山'
    df10['行政区'] = '昌平'
    df11['行政区'] = '通州'
    df12['行政区'] = '门头沟'
    df13['行政区'] = '顺义'



    # dataframe = [df1,df2,df3,df4,df5,df6]
    # result = pd.concat(dataframe)
    # result.to_csv('城六区存量.csv', encoding='UTF-8', index = False)

    # dataframe1 = [df7,df8,df9,df10, df11,df12,df13]
    # result1 = pd.concat(dataframe)
    # result1.to_csv('外城区存量.csv', encoding='UTF-8', index = False)


    df = [df1,df2,df3,df4,df5,df6, df7,df8,df9,df10, df11,df12,df13]
    result = pd.concat(df)
    result.to_csv('北京存量.csv', encoding='UTF-8', index = False)

