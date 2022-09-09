"""
prime number analization
author: euewrqe
date: 2022-09-09
"""
import math
from operator import truediv
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, TOP, messagebox
from turtle import color, width
import time

"""
素数を作り出すメソッド v2
max_num: 最大数
min_num: 最小数
"""
def get_primenum_list_2(max_num, min_num=None):
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
def is_happy(n):
  s = set()
  while (n > 1) and (n not in s):
    s.add(n)
    n = sum(SQUARE[d] for d in str(n))
  return n == 1



class NumSmallError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

"""
window生成クラス
"""
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # Window画面サイズ設定
        self.master.geometry("700x500")
        self.master.title("素数の検証")
        master = self.master
        label = tk.Label(self.master, text="最大数を入力してください")
        label.grid(row=10, column=0)
        self.text = tk.Entry()
        self.text.grid(row=10, column=20)

        label2 = tk.Label(self.master, text="最小数を入力してください")
        label2.grid(row=20, column=0)
        self.text2 = tk.Entry()
        self.text2.grid(row=20, column=20)

        button = tk.Button(text="行こう", width=4, height=1, command=self.btn_click)
        button.grid(row=30, column=0, sticky=tk.W)
        self.msg = tk.Label(text="msg", foreground="black")
        self.msg.grid(row=40, column=0)
        self.prime_list = []

        self.result_label = tk.Label(text="result:", foreground="black")
        self.result_label.grid(row=50, column=0)

        label = tk.Label(self.master, text="いずれの数は素数であるかを判定する：")
        label.grid(row=70, column=0)
        self.text3 = tk.Entry()
        self.text3.grid(row=80, column=0)
        button2 = tk.Button(text="行こう", width=4, height=1, command=self.btn_click2)
        button2.grid(row=90, column=0, sticky=tk.W)
        self.msg2 = tk.Label(text="msg", foreground="black")
        self.msg2.grid(row=100, column=0)
        
    def push_button(self):
        self.tree.yview("scroll", +1, "units")
    def btn_click2(self):
        prime_num = self.text3.get()
        try:
            prime_num = int(prime_num)
            result, divitor = is_prime(prime_num)

            if result:
                self.msg2.config(text="素数である", foreground="black")
                # is happy
                happy = is_happy(prime_num)
                if happy:
                    self.msg2.config(text="素数である、ハッピー素数である", foreground="black")

            else:
                self.msg2.config(text="素数でない、" + str(divitor) + "に割れる", foreground="black")
        except ValueError:
            self.msg2.config(text="数字をください", foreground="red")
        
        
    def btn_click(self):
        max_num = self.text.get()
        min_num = self.text2.get()
        try:
            max_num = int(max_num)
            if min_num is None:
                min_num = 7
            min_num = int(min_num)
            if min_num > max_num:
                raise(NumSmallError)
            
            self.msg.config(text=max_num, foreground="black")
            if max_num < 7: 
                raise(NumSmallError)
            start_time = time.time()
            self.prime_list, self.prime_dict = get_primenum_list_2(max_num, min_num)
            run_time = time.time() - start_time

            column = ("head", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
            self.tree = ttk.Treeview(self.master, columns=column)
            tree = self.tree
            w = 50

            tree.column('#0',width=0, stretch='no')
            tree.column('head', anchor='center',width=w)
            tree.column('0', anchor='center', width=w)
            tree.column('1', anchor='center', width=w)
            tree.column('2', anchor='center', width=w)
            tree.column('3', anchor='center', width=w)
            tree.column('4', anchor='center', width=w)
            tree.column('5', anchor='center', width=w)
            tree.column('6', anchor='center', width=w)
            tree.column('7', anchor='center', width=w)
            tree.column('8', anchor='center', width=w)
            tree.column('9', anchor='center', width=w)

            tree.heading('#0',text='')
            tree.heading('head', text='head',anchor='center')
            tree.heading('0', text='0',anchor='center')
            tree.heading('1', text='1',anchor='center')
            tree.heading('2', text='2',anchor='center')
            tree.heading('3', text='3',anchor='center')
            tree.heading('4', text='4',anchor='center')
            tree.heading('5', text='5',anchor='center')
            tree.heading('6', text='6',anchor='center')
            tree.heading('7', text='7',anchor='center')
            tree.heading('8', text='8',anchor='center')
            tree.heading('9', text='9',anchor='center')
            


            count = 0

            # for prime in self.prime_list:
            #     tree.insert(parent='', index='end', iid=count ,values=(count + 1, prime))
            #     count += 1


            while count <= max_num:
                if self.prime_dict.get(str(count)):
                    self.prime_dict[str(count)].insert(0, count)
                    tree.insert(parent='', index='end', iid=count ,values=self.prime_dict[str(count)])
                count += 1
            
            tree.grid(row=60, column=0, sticky="nsew")

            scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=60, column=1, sticky="ns")
        except ValueError:
            self.msg.config(text="数字しか受けない", foreground="red")
        except NumSmallError:
            self.msg.config(text="受けた数字が小さすぎる", foreground="red")

        


if __name__ == "__main__":
    # prime_list, prime_dict = get_primenum_list_2(2000000)
    # print(prime_list)
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
