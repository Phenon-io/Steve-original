import tkinter as tk

#entry window function
def callback():
    value = entry.get()
    print (value)

ewindow = tk.Tk()
space1 = tk.Label(ewindow, width=10)
space1.grid(row=0, column=0)
space2 = tk.Label(ewindow, width=10)
space2.grid(row=0, column=2)
Title = tk.Label(ewindow, text = 'Input value here')
Title.grid(row=0, column=1)
entry = tk.Entry()
entry.grid(row=1, column=1)
Button1 = tk.Button(ewindow, text="Submit", width=10, command = callback)
Button1.grid(row=2, column=1)



ewindow.mainloop()
