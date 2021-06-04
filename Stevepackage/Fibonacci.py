import tkinter as tk

#def defib(n):
    #result = []
    #a, b = 377, 610
    #while a > n:
        #result.append(a)
        #a, b = b, a-b
    #return result

def callback():
    value = entry.get()
    v = value
    nterms = int(value)

    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print (n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

def callback2():
    print ('Module closed')
    exit()

    



ewindow = tk.Tk()
space1 = tk.Label(ewindow, width=10)
space1.grid(row=0, column=0)
space2 = tk.Label(ewindow, width=10)
space2.grid(row=0, column=2)



Title = tk.Label(ewindow, text = 'How many terms?')
Title.grid(row=0, column=1)
entry = tk.Entry()
entry.grid(row=1, column=1)
Button1 = tk.Button(ewindow, text="Submit", width=10, command = callback)
Button1.grid(row=2, column=1)
Button2 = tk.Button(ewindow, text="Exit", width=10, command = callback2)
Button2.grid(row=3, column=1)



ewindow.mainloop()    

#FibResult = tk.Label(top, text)
#FibResult.pack

#top.mainloop()
