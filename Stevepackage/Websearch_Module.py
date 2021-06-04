import tkinter as tk
import webbrowser, sys, requests
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
Title = tk.Label(ewindow, text = 'Input value here')
Title.grid(row=0, column=1)
entry = tk.Entry()
entry.grid(row=1, column=1)
Button1 = tk.Button(ewindow, text="Submit", width=10, command = callback)
Button1.grid(row=2, column=1)
Button2 = tk.Button(ewindow, text="Exit", width=10, command = callback2)
Button2.grid(row=3, column=1)


ewindow.mainloop()