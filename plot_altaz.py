#Name        plot_altaz.py
#Purpose:    Creates scatter plot of altitude vs azimuth for specified object, over 24 hours 
#Purpose:    Includes altitudes of the sun and moon
#Usage:      python plot_altaz_sm.py -glong 180 -glat 0
#Reference:  https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py
#Notes:      Be sure to input the latitude, longitude, date and time zone.  Do not change time. from 12:00
#Notes:      Altitudes of sun and moon are always at az=180 degrees. Object azimuth may be different

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
print("Enter date into program, but do not change the time")
Chicago = EarthLocation(lat=41.867*u.deg, lon=-87.630*u.deg, height=0*u.m)
utcoffset = -5*u.hour
dateandtime="2021-09-10 12:00:00"
noon = Time(dateandtime) - utcoffset
time_zone=-5.0  #Adjust to -6.0 from Nov-Mar

delta_noon = np.linspace(-12, 12, 1000)*u.hour
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
plt.plot(objectaltazs.az, objectaltazs.alt, color='b', label="Object")
plt.plot(sunaltazs.az, sunaltazs.alt, color='r', label='Sun')
plt.plot(moonaltazs.az, moonaltazs.alt, color=[0.75]*3, ls='--', label='Moon')
plt.legend(loc='upper left')
plt.xlabel('Azimuth [deg]')
plt.ylabel('Altitude [deg]')
plt.title("Date,GalLon,GalLat "+dateandtime+"   "+str(GALLON)+"   "+str(GALLAT))
plt.show()

exit()
