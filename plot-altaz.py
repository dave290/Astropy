#Name        plot-altaz.py
#Purpose:    Creates scatter plot of altitude vs azimuth for specified object, over 24 hours 
#Usage:      python plot-altaz.py -glat 0 -glong 180
#Notes:      User must enter Latitude and longitude.  Day and time do not matter.      
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
parser.add_argument("-glong", "--glong", help="Enter galactic longitude in degrees", type=float)
parser.add_argument("-glat", "--glat", help="Enter galactic latitude in degrees", type=float)
args = parser.parse_args()
GALLON=args.glong
GALLAT=args.glat

#Program uses information below for calculations
LATITUDE=+41.867; LONGITUDE=-87.630
print("Latitude",LATITUDE,"Longitude",LONGITUDE)
Chicago = EarthLocation(lat=LATITUDE*u.deg, lon=LONGITUDE*u.deg, height=0*u.m)
time = Time("2022-01-01 12:00:00")
print("Day and time do not matter")

delta = np.linspace(-12, 12, 1000)*u.hour
times=time+delta
frame = AltAz(obstime=times,location=Chicago)

#Calculate Alt-Az for specified object
gc=SkyCoord(l=GALLON*u.degree, b=GALLAT*u.degree, frame='galactic')
objectaltazs=gc.transform_to(frame)

#Plot the data
plt.plot(objectaltazs.az, objectaltazs.alt, color='b')
plt.xlabel('Azimuth [deg]')
plt.ylabel('Altitude [deg]')
plt.title("GalLon,  "+str(GALLON)+"   Gallat,  "+str(GALLAT))
plt.show()

exit()
