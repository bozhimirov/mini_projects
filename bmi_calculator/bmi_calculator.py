import math
from tkinter import *
from tkinter import ttk


ht = {
    18: ['yellow', 'Underweight'],
    17: ['yellow', 'Underweight'],
    16: ['pink', 'Underweight'],
    20: ['yellow', "Overweight"],
    30: ['pink', "Obesity"],
}


def calculate_bmi(*args):
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        r = (weight / height ** 2)
        result.set(f'{r:.1f}')
        height_entry.delete(0, 'end')
        weight_entry.delete(0, 'end')
        res_label1['text'] = ' Your BMI is: '
        if 18.5 <= r <= 25:
            res['background'] = 'green'
            res_label['text'] = "Normal"
        elif r < 16:
            res['background'] = 'red'
            res_label['text'] = "Underweight"
        elif r < 18.5:
            res['background'] = ht[math.floor(r)][0]
            res_label['text'] = ht[math.floor(r)][1]
        elif r >= 35:
            res['background'] = 'red'
            res_label['text'] = "Obesity"
        else:
            new_r = math.floor(r/10)*10
            res['background'] = ht[math.floor(new_r)][0]
            res_label['text'] = ht[math.floor(new_r)][1]
    except ValueError:
        pass


root = Tk()
root.title('BMI Calculator')
height_entry = ttk.Entry(root, width=7)
weight_entry = ttk.Entry(root, width=7)
height_entry.grid(column=1, row=1, pady=2)
result = StringVar()
weight_entry.grid(column=1, row=2, pady=2)
res = ttk.Label(root, textvariable=result, width=7, justify='center')
res.grid(column=1, row=3, pady=2)
ttk.Label(root, text='height(m)').grid(column=2, row=1, sticky='WS', pady=2)
ttk.Label(root, text='weight (kg)', width=12).grid(column=2, row=2, sticky='WS', pady=2)
ttk.Label(root, text='BMI').grid(column=2, row=3, sticky='WS', pady=2)

ttk.Button(root, text='Calculate BMI', command=calculate_bmi).grid(column=3, row=3, sticky='WS')
ttk.Label(root, width=3).grid(column=4, row=3)
res_label = ttk.Label(root, text='')
res_label1 = ttk.Label(root, text='', width=11)
res_label1.grid(column=1, row=4, sticky='WS', pady=2)
res_label.grid(column=2, row=4, sticky='WS', pady=2)
root.bind('<Return>', calculate_bmi)
height_entry.focus()
root.mainloop()
