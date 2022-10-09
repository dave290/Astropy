#plot-sun.py
#Usage:      python plot-sun.py
#Purpose:    Creates scatter plot of GALLAT vs GALLON for sun over 12 month period.
#Purpose:    Prints GLAT,GLON for Sun's daily position to terminal window.
#Reference:  https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py
#Notes:      Be sure to input the latitude, longitude. Date and time do not matter.

import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Galactic
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()
from astropy.coordinates import get_sun

#SITE AND TIME
start_time="2022-12-18 12:00:00.000000" 
#12/18 is when SUN is closest to the galactic center (GALLONG ~4.5 degrees and GALLAT~3 degrees)

day=np.linspace(0, 365, 13)*u.day    #stepsize 13 gives monthly intervals, 366 gives daily
time=Time(start_time)+day
print(time)
print(" ")

#NEXT BLOCK PUTS SUN IN CELESTIAL COORDINATES
sun_cc=get_sun(time)   #in RA/DEC
#print(sun_cc)

#NEXT BLOCK CONVERTS INTO GALACTIC COORDINATES.
sun_cc=SkyCoord(sun_cc.ra,sun_cc.dec, frame='icrs', unit=(u.hourangle,u.deg))
sun_gc=sun_cc.galactic
print(sun_gc)

#Plot the data
ax=plt.axes()
ax.set_title("Sun in Galactic Coordinates")
plt.xlabel('Galactic Longitude (degrees)')
plt.ylabel('Galactic Latitude (degrees)')
ax.set_xlim(0.0,360.0)
ax.set_ylim(-80.0,+80.0)
ax.set_xticks([0,40,80,120,160,200,240,280,320,360])
ax.set_yticks([-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80])
ax.scatter(sun_gc.l,sun_gc.b)
plt.show()
exit()



