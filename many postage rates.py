######################
# mass postage rates.py
# 2014-03-25, by Aaronlaw
# This program calculates postage rates of manybo
# Ref: http://code.google.com/p/zhpy/wiki/DataStructure
######################
# PSEUDO CODE: 同時show 幾個不同取貨地點的郵費，自己比較
######################
weight = int( input('Input the weight (kg)...') )
def payment(weight, costs):
	return costs['first_kg'] + (weight - 1) * costs['addition_kg'] + costs['addition_fee']

costs = {'first_kg':15, 'addition_kg':5, 'addition_fee':25}
print ('送去家需付... RMB %s' % payment(weight, costs) )

costs = {'first_kg':15, 'addition_kg':5, 'addition_fee':0}
print ('送去公司需付...RMB %s' % payment(weight, costs) )

costs = {'first_kg':10, 'addition_kg':6, 'addition_fee':0}
print ('自取需付...RMB %s' % payment(weight, costs) )
