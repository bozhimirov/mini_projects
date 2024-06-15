import math
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('calculator by SB')
root.minsize(260, 160)

first = ''
second = ''
operator = ''
memory = 0
last_key = ''


def check_num(n):
    if not isinstance(n, str):
        n = str(n)
    ln = n.split('.')
    if len(ln) == 1:
        return int(n)
    elif len(ln) == 2:
        return float(n)
    else:
        return 'Error'


def mem_clean():
    global memory
    memory = 0


def mem_plus():
    global memory
    if not operator:
        memory += check_num(first)
    else:
        memory += check_num(second)


def mem_minus():
    global memory
    if not operator:
        memory -= check_num(first)
    else:
        memory -= check_num(second)


def mem_recall():
    global memory
    global first
    global second
    global operator
    global last_key
    input_field['text'] = memory
    if not operator:
        first = memory
    else:
        second = memory
    last_key = 'num'


def factorial_function(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_function(number - 1)


def factorial():
    global first
    global second
    global operator
    global last_key
    if last_key in ['num', 'equal']:
        if not operator:
            if check_num(first) < 0:
                input_field['text'] = 'Error'
                first = ''
                second = ''
                operator = ''
            elif '.' in first:
                input_field['text'] = 'Error'
                first = ''
                second = ''
                operator = ''
            else:
                res = factorial_function(check_num(first))
                first = str(res)
                if len(first) > 100:
                    input_field['text'] = "Error: too long number cannot process"
                    first = ''
                    second = ''
                    operator = ''
                else:
                    input_field['text'] = first
        else:
            if check_num(second) < 0:
                input_field['text'] = 'Error'
                first = ''
                second = ''
                operator = ''
            elif '.' in second:
                input_field['text'] = 'Error'
                first = ''
                second = ''
                operator = ''
            else:
                res = factorial_function(check_num(second))
                second = str(res)
                if len(second) > 100:
                    input_field['text'] = "too long number cannot process"
                    first = ''
                    second = ''
                    operator = ''
                else:
                    input_field['text'] = second
        last_key = '!'


def sqrt():
    global first
    global second
    global operator
    global last_key
    try:
        if not operator:
            res = math.sqrt(check_num(first))
            first = str(res)
            input_field['text'] = first
        else:
            res = math.sqrt(check_num(second))
            second = str(res)
            input_field['text'] = second
    except ValueError:
        input_field['text'] = 'Error'
        first = ''
        second = ''
        operator = ''

    last_key = 'sqrt'


def clear_e():
    global first
    global second
    global operator
    global last_key
    if not operator:
        first = ''
        input_field['text'] = ''
    else:
        second = ''
        input_field['text'] = ''
    last_key = 'equal'


def all_clear():
    global first
    global second
    global operator
    global last_key
    input_field['text'] = ''
    first = ''
    second = ''
    operator = ''
    last_key = 'num'


def num(x):
    global first
    global second
    global last_key
    if last_key not in ['equal', 'sqrt', '!', 'percent']:
        if not operator:
            if x == '<':
                first = first[:-1]
            else:
                if x == '.' and '.' in first:
                    pass
                elif first:
                    first += x
                else:
                    first = x
            input_field['text'] = first
        else:
            if x == '<':
                second = second[:-1]
            else:
                if x == '.' and '.' in second:
                    pass
                elif second:
                    second += x
                else:
                    second = x

            input_field['text'] = second
        last_key = 'num'


def operator_f(x):
    global operator
    global last_key
    if last_key in ['num', 'equal', 'sign', 'back', 'sqrt', '!', 'percent']:
        if not operator:
            input_field['text'] = first
            operator = x
            last_key = 'operator'
        else:
            last_key = 'equal'
            equal()
            if last_key != 'percent':
                operator = x
                last_key = 'operator'
    elif last_key == 'operator':
        operator = x


def equal():
    global first
    global second
    global operator
    global last_key
    result = 0
    if last_key != 'operator':
        if operator == '+':
            try:
                result = check_num(first) + check_num(second)
                first = str(result)
                if first[-2:] == '.0':
                    first = first[:-2]
                input_field['text'] = first
                second = ''
                operator = ''
            except ValueError:
                input_field['text'] = 'Error'
                result = 'Error'
        elif operator == '-':
            try:
                result = check_num(first) - check_num(second)
                first = str(result)
                if first[-2:] == '.0':
                    first = first[:-2]
                input_field['text'] = first
                second = ''
                operator = ''
            except ValueError:
                input_field['text'] = 'Error'
                result = 'Error'
        elif operator == '*':
            try:
                result = check_num(first) * check_num(second)
                first = str(result)
                if first[-2:] == '.0':
                    first = first[:-2]
                input_field['text'] = first
                second = ''
                operator = ''
            except ValueError:
                input_field['text'] = 'Error'
                result = 'Error'
        elif operator == '/':
            try:
                result = check_num(first) / check_num(second)
                first = str(result)
                if first[-2:] == '.0':
                    first = first[:-2]
                input_field['text'] = first
                second = ''
                operator = ''
            except ZeroDivisionError:
                input_field['text'] = 'Error'
                result = 'Error'
            except ValueError:
                input_field['text'] = 'Error'
                result = 'Error'

    if result == 'Error':
        input_field['text'] = result
        first = ''
        second = ''
        operator = ''

    last_key = 'equal'


def percent():
    global first
    global second
    global operator
    global last_key

    if operator in ['*', "/"] and second:
        second = str(check_num(second) / 100)
        if second[-2:] == '.0':
            second = second[:-2]
        input_field.config(text=second)
    elif operator in ['-', '+'] and second:
        second = str(check_num(second) * check_num(first) / 100)
        if second[-2:] == '.0':
            second = second[:-2]
        input_field.config(text=second)
    last_key = 'percent'


def sign_change():
    global first
    global second
    global last_key

    if not operator:
        res = check_num(first) * (-1)
        first = str(res)
        input_field['text'] = first
    else:
        res = check_num(second) * (-1)
        second = str(res)
        input_field['text'] = second
    last_key = 'sign'


input_field = ttk.Label(root, text='0', font=('Arial', 16))
# row0
input_field.grid(column=0, row=0, columnspan=7, sticky='e', pady=10)
# row1
Button(root, text='MC', command=mem_clean, font=('Arial', 11)).grid(column=0, row=1, sticky='news', padx=1, pady=1)
Button(root, text='MR', command=mem_recall, font=('Arial', 11)).grid(column=1, row=1, sticky='news', padx=1, pady=1)
Button(root, text='m+', command=mem_plus, font=('Arial', 11)).grid(column=2, row=1, sticky='news', padx=1, pady=1)
Button(root, text='m-', command=mem_minus, font=('Arial', 11)).grid(column=3, row=1, sticky='news', padx=1, pady=1)
# row2
Button(root, text='CE', command=clear_e, font=('Arial', 11)).grid(column=0, row=2, sticky='news', padx=1, pady=1)
Button(root, text='AC', command=all_clear, font=('Arial', 11)).grid(column=1, row=2, sticky='news', padx=1, pady=1)
Button(root, text='<', command=lambda n='<': num(n), font=('Arial', 11)).grid(column=2, columnspan=2, row=2, sticky='news', padx=1, pady=1)
# row3
Button(root, text='%', command=percent, font=('Arial', 10)).grid(column=0, row=3, sticky='news', padx=1, pady=1)
Button(root, text=chr(8730), command=sqrt, font=('Arial', 10)).grid(column=1, row=3, sticky='news', padx=1, pady=1)
Button(root, text='!', command=factorial, font=('Arial', 10)).grid(column=2, row=3, sticky='news', padx=1, pady=1)
Button(root, text=chr(247), command=lambda x='/': operator_f(x), font=('Arial', 11)).grid(column=3, row=3, sticky='news', padx=1, pady=1)
# row4
Button(root, text='7', command=lambda n='7': num(n), font=('Arial', 11)).grid(column=0, row=4, sticky='news', padx=1, pady=1)
Button(root, text='8', command=lambda n='8': num(n), font=('Arial', 11)).grid(column=1, row=4, sticky='news', padx=1, pady=1)
Button(root, text='9', command=lambda n='9': num(n), font=('Arial', 11)).grid(column=2, row=4, sticky='news', padx=1, pady=1)
Button(root, text='*', command=lambda x='*': operator_f(x), font=('Arial', 11)).grid(column=3, row=4, sticky='news', padx=1, pady=1)
# row 5
Button(root, text='4', command=lambda n='4': num(n), font=('Arial', 11)).grid(column=0, row=5, sticky='news', padx=1, pady=1)
Button(root, text='5', command=lambda n='5': num(n), font=('Arial', 11)).grid(column=1, row=5, sticky='news', padx=1, pady=1)
Button(root, text='6', command=lambda n='6': num(n), font=('Arial', 11)).grid(column=2, row=5, sticky='news', padx=1, pady=1)
Button(root, text='-', command=lambda x='-': operator_f(x), font=('Arial', 11)).grid(column=3, row=5, sticky='news', padx=1, pady=1)
# row 6
Button(root, text='1', command=lambda n='1': num(n), font=('Arial', 11)).grid(column=0, row=6, sticky='news', padx=1, pady=1)
Button(root, text='2', command=lambda n='2': num(n), font=('Arial', 11)).grid(column=1, row=6, sticky='news', padx=1, pady=1)
Button(root, text='3', command=lambda n='3': num(n), font=('Arial', 11)).grid(column=2, row=6, sticky='news', padx=1, pady=1)
Button(root, text='+', command=lambda x='+': operator_f(x), font=('Arial', 11)).grid(column=3, row=6, sticky='news', padx=1, pady=1)
# row 7
Button(root, text='+/-', command=sign_change, font=('Arial', 11)).grid(column=0, row=7, sticky='news', padx=1, pady=1)
Button(root, text='0', command=lambda n='0': num(n), font=('Arial', 11)).grid(column=1, row=7, sticky='news', padx=1, pady=1)
Button(root, text='.', command=lambda n='.': num(n), font=('Arial', 11)).grid(column=2, row=7, sticky='news', padx=1, pady=1)
Button(root, text='=', command=equal, font=('Arial', 11)).grid(column=3, row=7, sticky='news', padx=1, pady=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

root.mainloop()
