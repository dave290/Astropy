#plot_sun.py
#Usage:      python plot_sun.py
#Purpose:    Creates scatter plot of GALLAT vs GALLON for sun over 12 month period.
#Purpose:    Prints GLAT,GLON for Sun's daily position to terminal window.
#Reference:  https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py
#Notes:      Be sure to input the latitude, longitude. Date and time do not matter.

import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()
from astropy.coordinates import get_sun

#SITE AND TIME (program calculates ALT-AZ using this data, then converts to GALLON-GALLAT)
LocalSite = EarthLocation(lat=41.867*u.deg, lon=-87.630*u.deg, height=0*u.m)
utcoffset =-5.0*u.hour                  #Time zone = -6 for NOV-MAR, -5 for MAR-NOV (DST)
start_time="2021-12-18 12:00:00.000000" #Enter local time here
                                        # 12/18 is when SUN is at GLONG=0 (Sun and GC have same Right ascension)
                                        # 3/? is when Sun is at GLONG=90
                                        # 6/?  is when Sun is at GLONG=180
                                        # 9/? is when Sun is at GLONG=270

ax=plt.axes()
ax.set_title("Sun in Galactic Coordinates")
plt.xlabel('Galactic Longitude (degrees)')
plt.ylabel('Galactic Latitude (degrees)')
ax.set_xlim(0.0,360.0)
ax.set_xticks([0,40,80,120,160,200,240,280,320,360])
ax.set_yticks([-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70])

for i in range(366):
    k=i*u.day
    UNIVERSALTIME=Time(start_time)-utcoffset+k
    print("Local Time",UNIVERSALTIME+utcoffset)

    frame = AltAz(obstime=UNIVERSALTIME,location=LocalSite)
    sunaltazs = get_sun(UNIVERSALTIME).transform_to(frame)
    altitude=float(sunaltazs.alt.deg)
    azimuth=float(sunaltazs.az.deg)
    aa=SkyCoord(alt=altitude*u.degree,az=azimuth*u.degree,frame='altaz',obstime=UNIVERSALTIME,location=LocalSite)
    
    gc=aa.galactic
    GALLON=float(gc.l.deg)
    GALLAT=float(gc.b.deg)
    print("GALLON",GALLON)
    print("GALLAT",GALLAT)

    cc=aa.icrs
    RA=cc.ra.hms
    DEC=cc.dec.deg
    print("RA ",RA)
    print("DEC ",DEC)
    print(" ")

    #exit the loop to print GALLON and GALLAT for a desired starting date/time
    #exit()

    ax.scatter(GALLON,GALLAT,label=i)
plt.show()
exit()



