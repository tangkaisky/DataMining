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

def sort_bda(df):
	print 'sort start'
	length = len(df)
	process_set = set([length//4,length//2,(length*3)//4,length-1])
	col = set(['instance_id','item_id','item_brand_id','item_city_id','user_id','context_id','shop_id'])
	for _i in col:
		print time.clock()
		tmp = 1
		tmp_pre = 0
		for _x in xrange(length):
			if _x in process_set:
				print 'one+25%',time.clock()
			if _x > 0 and df.ix[_x,_i] != tmp_pre:
				tmp += 1
				tmp_pre = df.ix[_x,_i] 
				df.ix[_x,_i] = tmp
			else:
				tmp_pre = df.ix[_x,_i]
				df.ix[_x,_i] = tmp
	print 'sort finish'
