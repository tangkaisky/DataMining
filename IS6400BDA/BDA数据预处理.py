#coding = utf-8

import sys
import numpy as np
import pandas as pd 
from hash_for_bda import hash_bda, sort_bda
#清洗目录 使用数字等效编码非数字变量
from datacleaner import autoclean
# import 


# path = 'traindata_sample_1_100.csv'
path = 'traindata_cleaned_list_and_property.csv'
# path = 'traindata_cleaned_1w.csv'
# reader = pd.read_csv(path)


_reader = pd.read_csv(path, iterator = True)
#打开前5行观察数据的类型，列标签
chunkSize = 47000
print 'preproc',chunkSize
reader = _reader.get_chunk(chunkSize)
# print chunk

#test chunk = 1000,all = 10000
# read csv

# chunkSize = 1000

import time
#clock 比time更精准
start = time.clock()
# bda_pre(chunk)
# 删除重复行，默认判断全部列
reader.drop_duplicates()
#做非数字型字符转换成数字
clean_data = autoclean(reader)
# #hash
# hash_bda(reader)
# sort 1->n
sort_bda(reader)
reader.to_csv('traindata_cleaned.csv',index = False)
end = time.clock()
print end