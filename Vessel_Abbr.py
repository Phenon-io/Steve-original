#SteveModule

#Grabs vessel abbreviations from vessel names based on static list
#Can be programmed to handle an updating list at another date, hardcoded for
#current list.

import tkinter as tk
import sys
sys.path.append(r"C:\Steveenviron\Scripts\python.exe")



def callback1():
    value = entry.get()
    if value.lower() in ['avessel']:
        print ('AVES')
    elif value.lower() in ['Consumer']:
        print ('CS')
    elif value.lower() in ['marjorie c']:
        print ('MC')
    elif value.lower() in ['enterprise']:
        print ('EN')
    elif value.lower() in ['George III', 'GEORGE III', 'george iii', 'George 3', 'george 3']:
        print ('G3')
    elif value.lower() in ['Jean Anne', 'JEAN ANNE', 'jean anne']:
        print ('JA')
    elif value.lower() in ['Spirit', 'SPIRIT', 'spirit']:
        print ('JB')
    elif value.lower() in ['Horizon Navigator', 'HORIZON NAVIGATOR', 'horizon navigator']:
        print ('NA')
    elif value.lower() in ['Pacific', 'PACIFIC', 'pacific']:
        print ('PS')
    elif value.lower() in ['Reliance', 'RELIANCE', 'reliance']:
        print ('RG')
    elif value.lower() in ['aves']:
        print ('Vname')
    elif value.lower() in ['cs']:
        print ('Consumer')
    elif value.lower() in ['mc']:
        print ('Marjorie C')
    elif value.lower() in ['en']:
        print ('Enterprise')
    elif value.lower() in ['g3']:
        print ('George III')
    elif value.lower() in ['ja']:
        print ('Jean Anne')
    elif value.lower() in ['jb']:
        print ('Spirit')
    elif value.lower() in ['na']:
        print ('Horizon Navigator')
    elif value.lower() in ['ps']:
        print ('Pacific')
    elif value.lower() in ['rg']:
        print ('Reliance')        
    #template
    #elif value in ['vname']:
       # print ('ABBR')
       
    #template
    #elif value.lower() in ['abbr']:
       # print ('VName')       
    else :
        print ('No vesselname or abbreviation found, please use the vessel name found at \nhttps://www.pashahawaii.com/schedules/vessel-schedule \nor choose a valid vessel \nabbreviations tend to be 2 letters')

def callback3():
    print ('Module closed')
    exit()
        


ewindow = tk.Tk()

#Padding
space1 = tk.Label(ewindow, width=3)
space1.grid(row=0, column=0)
space2 = tk.Label(ewindow, width=3)
space2.grid(row=0, column=4)
space3 = tk.Label(ewindow, width=3, height=2)
space3.grid(row=4, column=1)
space3 = tk.Label(ewindow, width=3, height=2)
space3.grid(row=5, column=2)
space3 = tk.Label(ewindow, width=3, height=2)
space3.grid(row=5, column=5)


Title = tk.Label(ewindow, text = 'Vessel Name or Abbreviation')
Title.grid(row=0, column=2)
entry = tk.Entry()
entry.grid(row=3, column=2)
Button1 = tk.Button(ewindow, text="Submit", width=15, command = callback1)
Button1.grid(row=5, column=1)
Button3 = tk.Button(ewindow, text="Quit", width=15, command = callback3)
Button3.grid(row=5, column=3)

ewindow.mainloop()
