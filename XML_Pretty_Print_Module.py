#python 3
#sections pending completion, code will not function
import sys, os
os.chdir("C:\\")
sys.path.append(r"C:\\PyEnviron\\Steveenviron\\Lib\\site-packages")
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import messagebox as box
from tkinter import filedialog
from time import sleep
import xml.dom.minidom

#Callback Functions

def callback():
    value = entry.get()
    original_stdout = sys.stdout
    try:
        file = open("C:\\Users\\nwhitehorn\\Documents\\XML-Pretty-Print\\xml-pretty-print-temp.txt", "w+")
    except:
        print("Unable to generate or edit temporary file, confirm xml-pretty-print-temp.txt file is not read only")
    else:
        print("Temporary file loaded, pending xml upload")
        file.truncate(0) #ensures file truncation
        file.close()
  
    sys.stdout = open("C:\\Users\\nwhitehorn\\Documents\\XML-Pretty-Print\\xml-pretty-print-temp.txt", "w+")
    print(value)
    sys.stdout.close()
    sys.stdout = original_stdout
    print("Processing XML file")
    dom = xml.dom.minidom.parse("C:\\Users\\nwhitehorn\\Documents\\XML-Pretty-Print\\xml-pretty-print-temp.txt")
    prettyxml = dom.toprettyxml()
    sys.stdout = open("C:\\Users\\nwhitehorn\\Documents\\XML-Pretty-Print\\xml-pretty-print-final.txt", "w+")
    print(prettyxml)
    print("\n\n\n")
    print("If you would like to save this Pretty-Print, Save this File As another file name\nThis File's Name: xml-pretty-print-final.txt")
    sys.stdout.close()
    sys.stdout = original_stdout
    print("File successfully processed, opening processed file")
    os.startfile(r"C:\\Users\\nwhitehorn\\Documents\\XML-Pretty-Print\\xml-pretty-print-final.txt")


def callback2():
    print("Module closed")
    quit()
    
def callback3():
    value = entry.get()

#Tkinter Framework
root= tk.Tk()

#Tkinter Padding
space1 = tk.Label(root, width=5)
space1.grid(row=0, column=0)
space2 = tk.Label(root, width=5)
space2.grid(row=4, column=0)
space3 = tk.Label(root, width=5)
space3.grid(row=0, column=4)
space4 = tk.Label(root, width=5)
space4.grid(row=6, column=0)

#Tkinter Objects


Title = tk.Label(root, text = 'Paste or type XML to Pretty-Print')
Title.grid(row=0, column=2)
entry = tk.Entry()
entry.grid(row=3, column=2)
Button1 = tk.Button(root, text="Submit", width=15, command = callback)
Button1.grid(row=5, column=1)
Button3 = tk.Button(root, text="Quit", width=15, command = callback2)
Button3.grid(row=5, column=3)





    
root.mainloop()
