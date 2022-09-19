# -*- coding: utf-8 -*-
"""
prime number analization
author: euewrqe
date: 2022-09-09
"""
import math
import time

"""
素数を作り出すメソッド v2
max_num: 最大数
min_num: 最小数
"""
def get_primenum_list_2(max_num, min_num=None, is_happy=None):
    num = max_num
    prime_list = []
    
    if min_num is None or min_num < 7:
        min_num = 7
    if max_num < min_num: 
        return
    while num >= min_num:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            if is_happy and is_happy_func(num):
                prime_list.append(num)
            elif not is_happy:
                prime_list.append(num)
        num -= 1
    
    prime_dict = {}
    for prime in prime_list:
        prime_other, prime_one = str(prime)[:-1], int(str(prime)[-1])
        if prime_other == "":
            prime_other = "0"
        if prime_dict.get(prime_other) is None:
            prime_dict[prime_other] = ["", "", "", "", "", "", "", "", "", ""]
        prime_dict[prime_other][prime_one] = prime
    return prime_list, prime_dict

"""
素数を作り出すメソッド v1
max_num: 最大数
min_num: 最小数
"""
def get_primenum_list(max_num, min_num=None):
    num = max_num
    prime_list = []
    
    if min_num is None or min_num < 7:
        min_num = 7
    if max_num < min_num: 
        return
    


    while num >= min_num:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            num = num - 1
            continue
        divitor = 7
        
        while divitor <= math.floor(num / 2):
            if num % divitor == 0:
                break
            divitor = divitor + 1
            # if divitor % 2 == 0 or divitor % 3 == 0 or divitor % 5 == 0  or divitor % 7 == 0:
            #     continue
            
           
        else:
            print(num)
            prime_list.append(num)
            # break
        num = num - 1
    prime_dict = {}
    for prime in prime_list:
        prime_other, prime_one = str(prime)[:-1], int(str(prime)[-1])
        if prime_other == "":
            prime_other = "0"
        if prime_dict.get(prime_other) is None:
            prime_dict[prime_other] = ["", "", "", "", "", "", "", "", "", ""]
        prime_dict[prime_other][prime_one] = prime
    return prime_list, prime_dict

# def is_prime(num):
#     divitor = 2
#     while divitor <= math.ceil(num / 2):
#         print(divitor)
#         if num % divitor == 0:
#             break
#         divitor = divitor + 1
#     else:
#         return True, None
#     return False, divitor

"""
素数判定メソッド
n: 最大数
"""
def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, i
    return True, None

# is happy
SQUARE = dict([(c, int(c) ** 2) for c in "0123456789"])
def is_happy_func(n):
  s = set()
  while (n > 1) and (n not in s):
    s.add(n)
    n = sum(SQUARE[d] for d in str(n))
  return n == 1
