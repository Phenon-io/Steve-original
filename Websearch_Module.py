import tkinter as tk
import webbrowser, sys, os
os.chdir("C:\\")
sys.path.append(r"C:\\PyEnviron\\Steveenviron\\Lib\\site-packages")
import requests
from bs4 import BeautifulSoup
from time import sleep
from googlesearch import *


chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

def callback():
    value = entry.get()
    query = value
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    #search_terms = value
    #for term in search_terms:
    #for url in search(query, tld="co.in", num=1, stop=1, pause=2):
    search = ("https://www.google.com/search?q=" + ''.join(query))
    print('Searching %s' % (query))
    res = requests.get(search)
    try: 
        res.raise_for_status()
    except Exception as exc:
        print('Failure to load Search: %s' % (exc))
    chrome_browser.open(search)
    print('Search Loaded')

def callback2():
    print ('Module closed')
    exit()

ewindow = tk.Tk()
space1 = tk.Label(ewindow, width=10)
space1.grid(row=0, column=0)
space2 = tk.Label(ewindow, width=10)
space2.grid(row=0, column=2)
space3 = tk.Label(ewindow, width=10)
space3.grid(row=1, column=1)
space4 = tk.Label(ewindow, width=10)
space4.grid(row=5, column=2)
space5 = tk.Label(ewindow, width=10)
space5.grid(row=5, column=4)
space6 = tk.Label(ewindow, width=10)
space6.grid(row=4, column=1)

Welcome = tk.Label(ewindow, text = 'Welcome to the Websearch Module')
Welcome.grid(row=0, column=1)
Title = tk.Label(ewindow, width=25, text = 'Input Search term here')
Title.grid(row=2, column=1)
entry = tk.Entry(width=25)
entry.grid(row=3, column=1)
Button1 = tk.Button(ewindow, text="Submit Websearch", width=25, command = callback)
Button1.grid(row=5, column=1)
B1exp = tk.Label(ewindow, text = 'Will search the entered value in google and display the search results page')
B1exp.grid(row=5, column=3)
Button2 = tk.Button(ewindow, text="Exit", width=25, command = callback2)
Button2.grid(row=6, column=1)


ewindow.mainloop()
