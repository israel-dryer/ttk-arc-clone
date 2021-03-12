"""
    A simple demonstration of some ARC themed widgets

    Author: Israel Dryer
    Modified: 2021-03-08

"""
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from arc_theme_ttk import themed_style


root = tk.Tk()
root.title('All-in-One')
style = themed_style()

frame = ttk.Frame(root, padding=25)
frame.pack(fill='both', expand='yes')

ttk.Label(frame, text='ARC Themed Widgets', font='-size 30', anchor='center').pack(fill='x')
ttk.Label(frame, text='Here is some text... and a place to enter text', anchor='w').pack(fill='x', pady=10)

entry = ttk.Entry(frame)
entry.pack(fill='x', pady=5)
entry.insert('end', 'This is my text')

lframe = ttk.LabelFrame(frame, text='Options', padding=10)
lframe.pack(fill='x')

rvar = tk.IntVar()
rvar.set(1)
ttk.Checkbutton(lframe, text='Checkbox').pack(side='left', padx=2, fill='x', expand='yes')
ttk.Checkbutton(lframe, text='Another checkbox').pack(side='left', padx=2, fill='x', expand='yes')
ttk.Radiobutton(lframe, var=rvar, value=1, text='Radio option 1').pack(side='left', padx=2, fill='x', expand='yes')
ttk.Radiobutton(lframe, var=rvar, value=2, text='Radio option 2').pack(side='left', padx=2, fill='x', expand='yes')

opt_frame = ttk.Frame(frame)
opt_frame.pack(fill='x', expand='yes', pady=10)
opt_frame.columnconfigure(0, weight=1)
opt_frame.columnconfigure(1, weight=1)

cb = ttk.Combobox(opt_frame, values=['Combobox option1', 'Combobox option2', 'Combobox option 3'])
cb.set('Combobox option1')
cb.grid(sticky='ew')

mb = ttk.Menubutton(opt_frame, text='Seasons Menu Button')
mb.grid(row=0, column=1, sticky='ew')
mb.menu = tk.Menu(mb, tearoff=False)
mb['menu'] = mb.menu
mb.menu.add_checkbutton(label='Summer')
mb.menu.add_checkbutton(label='Fall')
mb.menu.add_checkbutton(label='Winter')
mb.menu.add_checkbutton(label='Spring')

ttk.Scale(frame, from_=0, to=100, value=25).pack(fill='x')

tv = ttk.Treeview(frame, columns=[1, 2, 3], height=2)
tv.heading(1, text='Name')
tv.heading(2, text='Job Title')
tv.heading(3, text='Department')
tv.insert('', 'end', 'accounting', text='Accounting')
tv.insert('accounting', 'end', values=['Richard Webb', 'Senior Accountant', 'Federal Tax'])
tv.insert('accounting', 'end', values=['Mary Hawking', 'Manager', 'Marketing'])
tv.insert('accounting', 'end', values=['Tom Riddle', 'Intern', 'Sales'])
tv.insert('', 'end', 'finance', text='Finance')
tv.insert('finance', 'end', values=['Richard Webb', 'Senior Accountant', 'Federal Tax'])
tv.insert('finance', 'end', values=['Mary Hawking', 'Manager', 'Marketing'])
tv.insert('finance', 'end', values=['Tom Riddle', 'Intern', 'Sales'])

tv.pack(fill='x', pady=10)


btn_frame = ttk.Frame(frame)
sb = ttk.Spinbox(btn_frame, values=['spinbox option 1', 'spinbox option 2', 'spinbox option 3'])
sb.set('spinbox option 1')
sb.pack(side='left', fill='x', expand='yes')
ttk.Button(btn_frame, text='Submit').pack(side='left', fill='x', expand='yes')
ttk.Button(btn_frame, text='Cancel').pack(side='left', fill='x', expand='yes')
btn_frame.pack(fill='x')

root.mainloop()


