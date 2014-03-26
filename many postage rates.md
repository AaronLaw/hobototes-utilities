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
----
PSEUDO CODE: 選好寄去邊，show 郵費
============
weight = raw_input
round weight to next integer
dist = raw_input

dist:
case: send to home
first_kg = 15
addition_kg = 5
addition_fee = 25
case: send to factory
first_kg = 15
addition_kg = 5
addition_fee = 0
case: self taken
first_kg = 10
addition_kg = 6
addition_fee = 0

payment = first_kg + (weight - 1) * addition_kg + addition_fee
display payment

