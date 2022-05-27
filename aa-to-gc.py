# aa-to-gc.py
# converts telescope coordinates into galactic coordinates
# Input and output GUI using tkinter
# Uses Chicago latitude and longitude
# Uses current time from R-Pi only
# May 23, 2022

from tkinter import *
import numpy as np
from datetime import datetime
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

#Location and Time Info
LAT=41.867; LON=-87.630
Chicago = EarthLocation(lat=LAT*u.deg, lon=LON*u.deg, height=0*u.m)
UNIVERSALTIME = Time.now()
print("Universal Time")
print(UNIVERSALTIME)

def convert():
    UNIVERSALTIME = Time.now()
    print("Universal Time")
    print(UNIVERSALTIME)
    output1.delete("1.0","end")
    output2.delete("1.0","end")    
    ALT=float(ent1.get())
    AZ=float(ent2.get())
    aa=SkyCoord(alt=ALT*u.degree, az=AZ*u.degree, frame='altaz',location=Chicago,obstime=UNIVERSALTIME)
    gc=aa.galactic
    GLONG=gc.l.deg
    GLAT=gc.b.deg
    output1.insert(1.0,int(GLONG))
    output2.insert(1.0,int(GLAT))

def clear_all():
    ent1.delete(0,END)
    ent2.delete(0,END)
    output1.delete("1.0","end")
    output2.delete("1.0","end")

#GUI settings
win=Tk()
win.geometry('300x300')
fontsize=50
frame=Frame(win)
win.title('aa-to-gc Converter')

ent1=Entry(win,font=fontsize)
ent1.grid(row=0, column=1)
ent2=Entry(win,font=fontsize)
ent2.grid(row=1, column=1)

text1=Label(win,text='ALT',font=fontsize)
text1.place(x=10,y=0)
ent1.place(x=10,y=20)

text2=Label(win,text='AZ',font=fontsize)
text2.place(x=10,y=50)
ent2.place(x=10,y=70)

btn=Button(text='CONVERT',font=fontsize,command=convert)
btn.place(x=10,y=100)

output1=Text(win,height=1,width=20,font=fontsize)
text3=Label(win,text='GLONG',font=fontsize)
text3.place(x=10,y=140)
output1.place(x=10,y=170)

output2=Text(win,height=1,width=20,font=fontsize)
text4=Label(win,text='GLAT',font=fontsize)
text4.place(x=10,y=200)
output2.place(x=10,y=220)

clrbtn=Button(win,text='CLEAR',command=clear_all,font=fontsize)
clrbtn.place(x=10,y=250)

frame.pack()
win.mainloop()
