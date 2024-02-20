from tkinter import *
import argparse
import sys, os
import errno, pathlib, re
import datetime, time
import json, requests, urllib.request
import sqlite3
import requests
import json

window=Tk()
window.title("Dylan's URL Scanner")
window.geometry('500x300')


label1=Label(window,text='Enter the URL to scan:', fg='blue', font=('Arial',14))
label1.grid(row=0,column=0,padx=5,pady=10)

url=StringVar()

textbox1=Entry(window,textvariable=url,fg='Black',font=('Arial',14))
textbox1.grid(row=0,column=1)

def buttonpress():

    url = 'https://www.virustotal.com/vtapi/v2/url/report'

    params = {'apikey': '0b1d96b92fe6abdbfec9e42a99abf41abb0aa9f908395a15bdc08d7cf70f928f', 'resource': url}

    response = requests.get(url, params=params)
    parsed = response.json()
    positives = parsed.get('positives')
    total = parsed.get('total')
    emptylabel.config(text='VT Positives='+  str(positives) + '/' + str(total))
    ##print('Positives =', parsed.get('positives'), '/', parsed.get('total'))
    
    



button1=Button(window,command=buttonpress,text='Scan',fg='Blue',font=('Arial',14))
button1.grid(row=1,column=1,sticky=W)

emptylabel=Label(window,fg='black',font=('Arial',11))
emptylabel.grid(row=2,column=1,sticky=W)

window.mainloop()
