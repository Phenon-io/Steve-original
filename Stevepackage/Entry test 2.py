import tkinter as tk

ewindow = tk.Tk()

#Padding
space1 = tk.Label(ewindow, width=3, height=2)
space1.grid(row=0, column=0)
space1.grid(row=0, column=2)
space3 = tk.Label(ewindow, width=3, height=2)
space3.grid(row=4, column=2)
space3.grid(row=5, column=2)
space3.grid(row=5, column=5)


Title = tk.Label(ewindow, text = 'Vessel Name or Abbreviation')
Title.grid(row=0, column=2)
entry = tk.Entry()
entry.grid(row=3, column=2)
Button1 = tk.Label(ewindow, text="Submit", width=15)
Button1.grid(row=5, column=1)
Button3 = tk.Label(ewindow, text="Quit", width=15)
Button3.grid(row=5, column=3)

ewindow.mainloop()
