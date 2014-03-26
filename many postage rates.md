The info about manybo postage rates.py
ref: 多寶網 多寶集運收費 http://www.manybo.com/index.php/Page/index/id/3

Send to home:
1st kg: 15+25
>1kg: 15 + (weight - 1)*5 +25
----
PSEUDO CODE: 寄去屋企
============
weight = raw_input
FIRST_KG = 15
ADDITION_KG = 5
ADDITION_FEE = 25

payment = FIRST_KG + (weight - 1)*ADDITION_KG + ADDITION_FEE
