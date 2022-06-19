#Name        plot_alt.py
#Purpose:    Creates scatter plot of altitude vs time for specified object, over 24 hours 
#Purpose:    Includes altitudes of the sun and moon
#Usage:      python plot_alt.py -day 2022-06-20 -timezone -5  -glat 0 -glong 180
#Reference:  https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py

import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()

import argparse
parser = argparse.ArgumentParser(description='plot_altaz.py')
parser.add_argument("-day", "--day", help="Enter date 2021-09-23", type=str)
parser.add_argument("-timezone", "--timezone", help="Enter-5 for summer -6 for winter", type=float)
parser.add_argument("-glong", "--glong", help="Enter galactic longitude in degrees", type=float)
parser.add_argument("-glat", "--glat", help="Enter galactic latitude in degrees", type=float)
args = parser.parse_args()
GALLON=args.glong
GALLAT=args.glat
day=args.day
timezone=args.timezone

#Program uses information below for calculations
print("Make sure latitude and longitude are correct within script")
Chicago = EarthLocation(lat=41.867*u.deg, lon=-87.630*u.deg, height=0*u.m)
utcoffset = -timezone*u.hour #Adjust to -6.0 from Nov-Mar, -5.0 during summer
dateandtime=day+" 12:00:00"  #do not change clock time
noon = Time(dateandtime) - utcoffset

delta_noon = np.linspace(-12, +12, 1000)*u.hour
times=noon+delta_noon
frame = AltAz(obstime=noon+delta_noon,location=Chicago)

#Calculate Alt-Az for specified object
gc=SkyCoord(l=GALLON*u.degree, b=GALLAT*u.degree, frame='galactic')
objectaltazs=gc.transform_to(frame)

#Calculate Alt-Az for Sun
from astropy.coordinates import get_sun
sunaltazs = get_sun(times).transform_to(frame)

#Calculate Alt-Az for Moon
from astropy.coordinates import get_moon
moon = get_moon(times)
moonaltazs = moon.transform_to(frame)

#Plot the data
plt.plot(delta_noon, objectaltazs.alt, color='b', label="Object")
plt.plot(delta_noon, sunaltazs.alt, color='r', label='Sun')
plt.plot(delta_noon, moonaltazs.alt, color=[0.75]*3, ls='--', label='Moon')
plt.fill_between(delta_noon, 0*u.deg, 90*u.deg,sunaltazs.alt < -0*u.deg, color='0.5', zorder=0)
plt.fill_between(delta_noon, 0*u.deg, 90*u.deg,sunaltazs.alt < -18*u.deg, color='k', zorder=0)
plt.legend(loc='upper left')
plt.xlim(-12*u.hour, 12*u.hour)
plt.xticks((np.arange(13)*2-12)*u.hour)
plt.ylim(0*u.deg, 90*u.deg)
plt.xlabel('Hours Relative to Local Noon')
plt.ylabel('Altitude [deg]')
plt.title(dateandtime+" GLONG, GLAT "+str(GALLON)+"   "+str(GALLAT))
plt.show()

exit()
