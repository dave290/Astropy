# barycentric.py
# example: python barycentric.py
# notes: user must input UNIVERSAL TIME, LAT, LONG
# notes: user must also choose to enter GALACTIC or CELESTIAL coordinates, using """ to null block
# notes: user may also input observed frequency if they want to calculate corrected velocity
# notes: uses Astropy package
# https://docs.astropy.org/en/stable/coordinates/velocities.html
# https://docs.astropy.org/en/stable/api/astropy.coordinates.SkyCoord.html#astropy.coordinates.SkyCoord.radial_velocity_correction

from astropy.coordinates import SkyCoord, EarthLocation
import astropy.units as u
from datetime import datetime
from astropy.time import Time

observationtime='2020-09-22 00:20:00' #this is UNIVERSAL time, written to .ast files
home=EarthLocation.from_geodetic(lat=41.867, lon=-87.630, height=0)


#######################################################################################################
#OPTION 1: ENTER GALACTIC COORDINATES
#######################################################################################################
GALLON=60.0;GALLAT=+17.0
#North ecliptic (orbital) pole is GALLON=96, GALLAT=+30.  This is where barycentric correction ~0 km/s 
gc=SkyCoord(l=GALLON*u.degree, b=GALLAT*u.degree, frame='galactic')
barycorr=gc.radial_velocity_correction(obstime=Time(observationtime), location=home)
print("barycentric correction: includes orbital correction only")
print(barycorr.to(u.km/u.s))
x=float(barycorr.to(u.km/u.s)*(1.*u.s)/(1.*u.km))

#heliocorr calculates both Earth's orbital and rotational corrections, combined.
heliocorr=gc.radial_velocity_correction('heliocentric',obstime=Time(observationtime), location=home)
#next line converts an astropy quantity with units into a unitless quantity
y=float(heliocorr.to(u.km/u.s)*(1.*u.s)/(1.*u.km))
print("heliocentric correction: rotation only")
print(heliocorr.to(u.km/u.s)-barycorr.to(u.km/u.s))
print("total correction: includes orbital and rotational corrections")
print(heliocorr.to(u.km/u.s))
print(" ")

"""
#######################################################################################################
#OPTION 2: ENTER CELESTIAL COORDINATES
#######################################################################################################
RA="18h00m00s"; DEC="+66d33m00s"
#North ecliptic (orbital) pole is RA 18h00m, DEC +66d33m.  This is where barycentric correction ~0 km/s 
cc=SkyCoord(ra=RA, dec=DEC, frame='icrs', unit=(u.hourangle,u.deg))
gc=cc.galactic    
print("Galactic Longitude")
GALLON=gc.l.deg  
print(GALLON)
print("Galactic Latitude")
GALLAT=gc.b.deg
print(GALLAT)
print(" ")

#barycorr calculates Earth's orbital velocity around the Sun
barycorr=cc.radial_velocity_correction(obstime=Time(observationtime), location=home)
print("barycentric correction: includes orbital correction only")
print(barycorr.to(u.km/u.s))
x=float(barycorr.to(u.km/u.s)*(1.*u.s)/(1.*u.km))

#heliocorr calculates both Earth's orbital and rotational corrections, combined.
heliocorr=cc.radial_velocity_correction('heliocentric',obstime=Time(observationtime), location=home)
#next line converts an astropy quantity with units into a unitless quantity
y=float(heliocorr.to(u.km/u.s)*(1.*u.s)/(1.*u.km))
print("heliocentric correction: rotation only")
print(heliocorr.to(u.km/u.s)-barycorr.to(u.km/u.s))
print("total correction: includes orbital and rotational corrections")
print(heliocorr.to(u.km/u.s))
print(" ")
"""

#######################################################################################################
#CALCULATE DOPPLER SHIFTED VELOCITY USING MEASURED FREQUENCY
#######################################################################################################
freq_measured=1421598828   #grab this from .ast file
freq_ref=     1420405750   #do not change. This is H spin-flip frequency that is used in T.py
c=300000
vshift=c*(freq_ref-freq_measured)/freq_ref
vcorrected=vshift+y
print("measured frequency")
#next line converts a unitless quantity into an astropy quantity with units
print(u.Quantity(freq_measured, u.Hz))
print("net doppler shift")
print(u.Quantity(vshift, u.km/u.s))
print("corrected doppler shift")
print(u.Quantity(vcorrected, u.km/u.s))

exit()
