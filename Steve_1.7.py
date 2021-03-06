#python 3.9.5
#Steve, the helpful python bot
#version 1.8, PrettyPrinting to the stars
import os, sys
os.chdir("C:\\PyEnviron\\Steveenviron\\")
sys.path.append(r"Lib\\site-packages")
import webbrowser, requests
import subprocess
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import messagebox as box
from tkinter import filedialog
from time import sleep
from random import seed
from random import randint


#webbrowser selector for links
chrome_browser = webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s")

#Tkinter frame
root= tk.Tk()
results = []

#tk padding
space1 = tk.Label(root, width=5)
space1.grid(row=0, column=0)
space2 = tk.Label(root, width=5)
space2.grid(row=0, column=2)

#greeting text
#seed(1)
#for _ in range (1):
    #randle = randint(0,3)
    #if randle = (1):
        

w = tk.Label(root, text="Hello world, have a beautiful day")
w.grid(row=0, column=1)
canvas2 = tk.Canvas(root, width=300, height=25)
canvas2.grid(row=1, column=1)
canvas3 = tk.Canvas(root, width=300, height=25)
canvas3.grid(row=2, column=1)
canvas4 = tk.Canvas(root, width=300, height=25)
canvas4.grid(row=3, column=1)
canvas5 = tk.Canvas(root, width=300, height=25)
canvas5.grid(row=4, column=1)
canvas6 = tk.Canvas(root, width=300, height=25)
canvas6.grid(row=5, column=1)
canvas9 = tk.Canvas(root, width=300, height=25)
canvas9.grid(row=6, column=1)
canvas7 = tk.Canvas(root, width=300, height=25)
canvas7.grid(row=7, column=1)
canvas8 = tk.Canvas(root, width=300, height=25)
canvas8.grid(row=8, column=1)
canvas1 = tk.Canvas(root, width = 300, height=25)
canvas1.grid(row=9, column=1)
x=tk.Label(root, width=30, height=5, text="Steve Ver 1.7")
x.grid(row=10, column=1)

#modules
def fib1():
    os.system('python Fibonacci.py')
    
#pending implementation
def goog():
    os.system('Websearch_Module.py')

def ves():
    os.system('python Vessel_Abbr.py')
    

def BI():
    url = "http://appcmotaprod01/Pasha.BI.YieldManagement/Pasha.BI.YieldManagement.application"
    webbrowser.open(url)

def N4():
    url = "https://n4apps.hawaiistevedores.com/apex/apex.jnlp"
    chrome_browser.open(url)

def N4S():
    url = "http://10.1.50.82:9080/apex/apex.jnlp"
    chrome_browser.open(url)

def gmp():
    links = ['https://pashagroup.lightning.force.com/one/one.app', 'http://server1.vilden.net:8023/presto/presto', 'http://server1.vilden.net:8023/presto/presto', 'http://server1.vilden.net:8023/presto/presto', 'https://server1.vilden.net/cgi-wec/login.pgm'] 
    url3= "https://pashagroup.lightning.force.com/one/one.app"
    url4= "http://server1.vilden.net:8023/presto/presto"
    url5= "https://server1.vilden.net/cgi-wec/login.pgm"
    try:
        r = requests.get(url4)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print('Vilden Presto Unavailable')
    #chrome_browser.open(url4)
    #chrome_browser.open(url4)
    #chrome_browser.open(url4)
    #chrome_browser.open(url5)
    #chrome_browser.open(url3)
    for link in links:
        chrome_browser.open_new_tab(link)
        sleep(0.1)
    os.startfile("outlook")
    try:
        os.system('C:\\Users\\nwhitehorn\\Desktop\\Pasha^ Control^ Console^ 2.appref-ms')    
    except Exception as exc: 
        print ('Unable to boot PEEF, confirm PEEF is in a desktop shortcut location (default) \n %s' % (exc))
    #PCC is in 32 bits, potential server framework issue
    #subprocess.call(['C:\\Users\\nwhitehorn\\Desktop\\Pasha Control Console 2.appref-ms'])
    #subprocess.call(['C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2016'])
    try:
        os.system('C:\\Program^ Files\\OTA2\\AppStart.exe')    
    except Exception as exc: 
        print ('Unable to boot OTA, confirm OTA is in a default location\n %s' % (exc))
def pprint():
    os.system('python XML_Pretty_Print_Module.py')
                     

#module buttons
button2 = tk.Button (root, text='Fibonacci', command= fib1)
canvas2.create_window(150, 25, window=button2)

button3 = tk.Button (root, text='Search a Subject', command= goog)
canvas3.create_window(150, 25, window=button3)

button4 = tk.Button (root, text='Vessel Abbreviations', command= ves)
canvas4.create_window(150, 25, window=button4)

button5 = tk.Button (root, text='BI Update', command= BI)
canvas5.create_window(150, 25, window=button5)

button6 = tk.Button (root, text='N4 Access', command= N4)
canvas6.create_window(150, 25, window=button6)

button9 = tk.Button (root, text='N4 Staging', command= N4S)
canvas9.create_window(150, 25, window=button9)

button7 = tk.Button (root, text='Good Morning Protocol', command= gmp)
canvas7.create_window(150, 25, window=button7)

button8 = tk.Button (root, text='XML Pretty Printer', command= pprint)
canvas8.create_window(150, 25, window=button8)

button1 = tk.Button (root, text='Close Steve', command= root.destroy)
canvas1.create_window(150, 25, window=button1)


root.mainloop()
