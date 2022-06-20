#Name        plot_altaz.py
#Purpose:    Creates scatter plot of altitude vs azimuth for specified object, over 24 hours 
#Usage:      python plot_altaz.py -day 2022-06-20 -glat 0 -glong 180
#Notes:      User must enter Latitude, longitude, and time zone in script.  Do not change time from 12:00      
#Reference:  https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py

import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()

import argparse
parser = argparse.ArgumentParser(description='plot_altaz.py')
parser.add_argument("-day", "--day", help="Enter date 2021-09-23", type=str)
parser.add_argument("-glong", "--glong", help="Enter galactic longitude in degrees", type=float)
parser.add_argument("-glat", "--glat", help="Enter galactic latitude in degrees", type=float)
args = parser.parse_args()
GALLON=args.glong
GALLAT=args.glat
day=args.day

#Program uses information below for calculations
LATITUDE=+41.867; LONGITUDE=-87.630; TIMEZONE=-5.0 #-5 summer (DST), -6 winter
print("Latitude",LATITUDE,"Longitude",LONGITUDE,"Timezone",TIMEZONE)
Chicago = EarthLocation(lat=LATITUDE*u.deg, lon=LONGITUDE*u.deg, height=0*u.m)
utcoffset = -TIMEZONE*u.hour
dateandtime=day+" 12:00:00"  #do not change clock time
noon = Time(dateandtime) - utcoffset

delta_noon = np.linspace(-12, 12, 1000)*u.hour
times=noon+delta_noon
frame = AltAz(obstime=noon+delta_noon,location=Chicago)

#Calculate Alt-Az for specified object
gc=SkyCoord(l=GALLON*u.degree, b=GALLAT*u.degree, frame='galactic')
objectaltazs=gc.transform_to(frame)

#Plot the data
plt.plot(objectaltazs.az, objectaltazs.alt, color='b', label="Object")
plt.legend(loc='upper left')
plt.xlabel('Azimuth [deg]')
plt.ylabel('Altitude [deg]')
plt.title("Date,GalLon,GalLat "+dateandtime+"   "+str(GALLON)+"   "+str(GALLAT))
plt.show()

exit()
