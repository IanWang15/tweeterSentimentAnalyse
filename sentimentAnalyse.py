#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 23:32:29 2019

@author: yiwang
"""
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

filename = 'tweeterData.csv'

data = np.loadtxt(filename)
print 'lenth is ', len(data)
fileIdx = np.zeros(shape = (len(data), 4))

ii = 0
for iline in len(data):
    sentiment_dict = SentimentIntensityAnalyzer.polarity_scores(data[iline,5])
    if sentiment_dict:
        fileidx[ii,0] = data[iline,2]
        fileidx[ii,1] = data[iline,3]
        fileidx[ii,2] = sentiment_dict['pos']
        fileidx[ii,3] = sentiment_dict['neu']
        fileidx[ii,4] = sentiment_dict['neg']
        fileidx[ii,5] = sentiment_dict['compound']
        ii += 1

filename = 'sentimentOutput.txt'
np.savetxt(filename, fileIdx)
print 'computation is finished'
