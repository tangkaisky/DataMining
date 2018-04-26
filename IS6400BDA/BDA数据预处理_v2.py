#coding = utf-8

import sys
import numpy as np
import pandas as pd 
from hash_for_bda_v2 import hash_bda, sort_bda
#清洗目录 使用数字等效编码非数字变量
from datacleaner import autoclean

path = 'traindata_cleaned_list_and_property.csv'
path_o = 'traindata_cleaned.csv'

_reader = pd.read_csv(path, iterator = True)
# 循环读入CSV,每次100000
loop = True
chunkSize = 1000
chunks = []
_write = 0
_dic_col = dict()
while loop:
	try:
		chunk = _reader.get_chunk(chunkSize)
		# chunks.append(chunk)
		if not _write:
			_dic_col = sort_bda(chunk)
			df.to_csv(path_o, index = False)
		else:
			_dic_col = sort_bda(chunk,_dic_col)
			df.to_csv(path_o, mode='a', header=False,index = False)
		_write += 1
	except StopIteration:
		loop = False
		print "Iteration is stopped."
# df = pd.concat(chunks, ignore_index=True)


'''
path = 'traindata_cleaned_list_and_property.csv'
# path = 'traindata_cleaned_1w.csv'
# reader = pd.read_csv(path)


_reader = pd.read_csv(path, iterator = True)
#打开前5行观察数据的类型，列标签
chunkSize = 47000
print 'preproc',chunkSize
reader = _reader.get_chunk(chunkSize)
# print chunk

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
'''