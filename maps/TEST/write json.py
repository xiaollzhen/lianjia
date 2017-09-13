# -*- coding: utf-8 -*-
import pandas as pd


if __name__ =="__main__":
    df = pd.read_csv('00.csv')
    names = list(df['小区名']).unique
    for i in names:
        print i