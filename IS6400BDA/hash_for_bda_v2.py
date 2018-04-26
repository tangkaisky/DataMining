#coding = utf-8
import time

def hash_bda(df):
	print 'hash start'
	length = len(df)
	process_set = set([length//4,length//2,(length*3)//4,length-1])
	col = set(['instance_id','item_id','item_brand_id','item_city_id','user_id','context_id','shop_id'])
	for _i in col:
		print time.clock()
		for _x in xrange(length):
			if _x in process_set: 
				print 'one+25%',time.clock()
			tmp = hash(df.ix[_x,_i])
			df.ix[_x,_i] = tmp
	print 'hash done'

def sort_bda(df,dic_col = None):
	print 'sort start'
	length = len(df)
	process_set = set([length//4,length//2,(length*3)//4,length-1])
	col = set(['instance_id','item_id','item_brand_id','item_city_id','user_id','context_id','shop_id'])
	if not dic_col: dic_col = dict.fromkeys(col,0)
	for _i in col:
		print time.clock()
		tmp = 1
		for _x in xrange(length):
			if _x in process_set:
				print 'one+25%',time.clock()
			if _x == 0:
				#判断是否存在上个chunk
				if not dic_col[_i]: 
					dic_col[_i] = df.ix[_x,_i]
					# tmp = _write*chunkSize + 1
					df.ix[_x,_i] = tmp
				else:
					if dic.ix[_x,_i] == dic_col[_i][0]:
						dic_col[_i] = df.ix[_x,_i]
						#global _write chunkSize
						tmp = _write*chunkSize
						df.ix[_x,_i] = tmp
					else:
						tmp = _write*chunkSize +1
						dic_col[_i] = df.ix[_x,_i]
						df.ix[_x,_i] = tmp

			if _x > 0 and df.ix[_x,_i] != dic_col[_i]:
				tmp += 1
				dic_col[_i] = df.ix[_x,_i] 
				df.ix[_x,_i] = tmp
			else:
				dic_col[_i] = df.ix[_x,_i]
				df.ix[_x,_i] = tmp
				#todo
		# 保存最后一次的排序值和原始值
		dic_col[_i] = [tmp,df.ix[_x,_i]]
		# tmp_pre = 0
	print 'dic_col:',dic_col
	print 'sort finish'
	return dic_col