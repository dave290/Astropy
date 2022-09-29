#Name:       plot-gc.py
#Purpose:    Creates scatter plot of glat vs glong over 24 h period for a constant alt-az
#Usage:      python plot_gc.py -az 180 -alt 70 
#Reference:  https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py
#Reference:  https://docs.astropy.org/en/stable/coordinates/index.html
#Notes:      Starting date/time and timezone do not matter

import numpy as np
#import astropy.units as u
from astropy import units as u
from astropy.time import Time
from datetime import datetime
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Galactic
import matplotlib.pyplot as plt

#Read data provided by user
import argparse
parser = argparse.ArgumentParser(description='plot_gc.py')
parser.add_argument("-alt", "--alt", help="Enter altitude in degrees", type=float)
parser.add_argument("-az", "--az", help="Enter azimuth in degrees", type=float)
args = parser.parse_args()
altitude=args.alt
azimuth=args.az

#Program uses information below for calculations
LATITUDE=+41.867; LONGITUDE=-87.630
Chicago = EarthLocation(lat=LATITUDE*u.deg, lon=LONGITUDE*u.deg, height=0*u.m)
print("Latitude",LATITUDE,"Longitude",LONGITUDE)
print("Starting date and time do not matter.")

frame=Galactic

ax=plt.axes()
ax.set_title("Altitude, Azimuth, "+str(altitude)+", "+str(azimuth))
#ax.set_xlim(0,240)
ax.set_xticks([0,40,80,120,160,200,240,280,320,360])
ax.set_yticks([-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])
plt.xlabel('Galactic Longitude (degrees)')
plt.ylabel('Galactic Latitude (degrees)')
for i in range(96):   #15 minute steps
    j=0.25*i
    k=j*u.hour
    time=Time("2022-01-01 12:00:00")+k   
    aa=SkyCoord(obstime=time,location=Chicago,alt=altitude*u.degree,az=azimuth*u.degree,frame='altaz')
    gc=aa.transform_to(frame)
    gallon=gc.l.deg,1
    gallat=gc.b.deg,1
    gallon=float(gallon[0])
    gallat=float(gallat[0])
    ax.scatter(gallon,gallat)

#Generate a line passing through galactic latitude of zero degrees
x=[0];y=[0]
for i in range(360):
    x.append(i)
    y.append(0)
ax.scatter(x,y,marker=".")
plt.grid()
plt.show()
exit()

