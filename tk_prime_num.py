"""
prime number analization / tkinter version
author: euewrqe
date: 2022-09-09
"""
from operator import truediv
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, TOP, messagebox
from turtle import color, width
from prime_num import get_primenum_list_2, is_prime, is_happy_func
import time


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

        self.is_happy = False

        label = tk.Label(self.master, text="最小数:")
        label.grid(row=1, column=0, sticky=tk.E)
        self.text2 = tk.Entry()
        self.text2.grid(row=1, column=1)
        

        label = tk.Label(self.master, text="最大数:")
        label.grid(row=2, column=0, sticky=tk.E)
        self.text = tk.Entry()
        self.text.grid(row=2, column=1)

        

        button = tk.Button(text="確定", width=4, height=1, command=self.btn_click)
        button.grid(row=2, column=3, sticky=tk.W)
        self.checkbox = tk.Checkbutton(self.master, text="ハッピー？", command=self.get_happy, variable=self.is_happy)
        self.checkbox.grid(row=1, column=3, sticky=tk.W)
        self.msg = tk.Label(text="msg", foreground="black")
        self.msg.grid(row=2, column=4, sticky=tk.W)
        self.prime_list = []
        
        self.result_label = tk.Label(self.master, text="", foreground="black")
        self.result_label.grid(row=3, column=0, columnspan=4)

        label = tk.Label(self.master, text="素数判定：")
        label.grid(row=5, column=0)
        self.text3 = tk.Entry()
        self.text3.grid(row=6, column=0)
        button2 = tk.Button(self.master, text="確定", width=4, height=1, command=self.btn_click2)
        button2.grid(row=6, column=2, sticky=tk.W)
        self.msg2 = tk.Label(self.master, text="msg", foreground="black")
        self.msg2.grid(row=6, column=3)
    
    def get_happy(self):
        self.is_happy = not self.is_happy

    def push_button(self):
        self.tree.yview("scroll", +1, "units")
    def btn_click2(self):
        # tk.messagebox.showinfo(title="title", message="message")
        """
        message, showaarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel
        """
        prime_num = self.text3.get()
        try:
            prime_num = int(prime_num)
            result, divitor = is_prime(prime_num)

            if result:
                self.msg2.config(text="素数", foreground="black")
                # is happy
                happy = is_happy_func(prime_num)
                if happy:
                    self.msg2.config(text="素数且つハッピー素数", foreground="black")

            else:
                self.msg2.config(text="素数ではない、" + str(divitor) + "に割れる", foreground="black")
        except ValueError:
            self.msg2.config(text="数字をください", foreground="red")
        
        
    def btn_click(self):
        if self.is_happy:
            self.result_label.config(text="ハッピー素数表:")
        else:
            self.result_label.config(text="素数表:")

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
            self.prime_list, self.prime_dict = get_primenum_list_2(max_num, min_num, self.is_happy)
            run_time = time.time() - start_time

            # make a table
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
            
            tree.grid(row=4, column=0, columnspan=5, sticky="nsew")

            scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=4, column=5, sticky="ns")
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
