######################
# mass postage rates.py
# 2014-03-25, by Aaronlaw
# This program calculates postage rates of manybo
######################
# PSEUDO CODE: 同時show 幾個不同取貨地點的郵費，自己比較
# ============
# weight = raw_input
# round weight to next integer
# payment (weight):
# first_kg + (weight - 1) * addition_kg + addition_fee

# first_kg = 15
# addition_kg = 5
# addition_fee = 25
# display payment: 'Payment of home...' = payment(weight)
# first_kg = 15
# addition_kg = 5
# addition_fee = 0
# display payment: 'Payment of factory...' = payment(weight)
# first_kg = 10
# addition_kg = 6
# addition_fee = 0
# display payment: 'Payment of self taken...' = payment(weight)
######################
