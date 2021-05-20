#Steve, the helpful python bot
#version 1.7, yelling at webpages version
import sys, os, webbrowser, requests
import subprocess
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import messagebox as box
from tkinter import filedialog
from time import sleep

#webbrowser selector for links
chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

#Tkinter frame
root= tk.Tk()
results = []

#tk padding
space1 = tk.Label(root, width=10)
space1.grid(row=0, column=0)
space2 = tk.Label(root, width=10)
space2.grid(row=0, column=2)

w = tk.Label(root, text="Hello world, have a beautiful day")
w.grid(row=0, column=1)
canvas2 = tk.Canvas(root, width = 300, height = 25)
canvas2.grid(row=1, column=1)
canvas3 = tk.Canvas(root, width = 300, height = 25)
canvas3.grid(row=2, column=1)
canvas4 = tk.Canvas(root, width = 300, height = 25)
canvas4.grid(row=3, column=1)
canvas5 = tk.Canvas(root, width = 300, height = 25)
canvas5.grid(row=4, column=1)
canvas6 = tk.Canvas(root, width = 300, height = 25)
canvas6.grid(row=5, column=1)
canvas7 = tk.Canvas(root, width = 300, height = 25)
canvas7.grid(row=6, column=1)
canvas1 = tk.Canvas(root, width = 300, height = 25)
canvas1.grid(row=7, column=1)
x=tk.Label(root, text="Steve Ver 1.7")
x.grid(row=8, column=1)

#modules
def fib1():
    os.system('python Fibonacci.py')
    return
#pending implementation
def goog():
    os.system('Websearch_Module.py')
    print('This function is pending an update, please try again later')

def ves():
    os.system('python Vessel_Abbr.py')
    return

def BI():
    url = "http://appcmotaprod01/Pasha.BI.YieldManagement/Pasha.BI.YieldManagement.application"
    webbrowser.open(url)

def N4():
    url2 = "https://n4apps.hawaiistevedores.com/apex/"
    chrome_browser.open(url2)

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
        
    #PCC is in 32 bits, potential server framework issue
    #subprocess.call(['C:\\Users\\nwhitehorn\\Desktop\\Pasha Control Console 2.appref-ms'])
    #subprocess.call(['C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2016'])

                     

#module buttons
button2 = tk.Button (root, text='Fibonacci', command= fib1)
canvas2.create_window(150, 15, window=button2)

button3 = tk.Button (root, text='Search a Subject', command= goog)
canvas3.create_window(150, 15, window=button3)

button4 = tk.Button (root, text='Vessel Abbreviations', command= ves)
canvas4.create_window(150, 15, window=button4)

button5 = tk.Button (root, text='BI Update', command= BI)
canvas5.create_window(150, 15, window=button5)

button6 = tk.Button (root, text='N4 Access', command= N4)
canvas6.create_window(150, 15, window=button6)

button7 = tk.Button (root, text='Good Morning Protocol', command= gmp)
canvas7.create_window(150, 15, window=button7)

button1 = tk.Button (root, text='Close Steve', command= root.destroy)
canvas1.create_window(150, 15, window=button1)


root.mainloop()


