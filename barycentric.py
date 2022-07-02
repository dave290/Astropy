# https://docs.astropy.org/en/stable/coordinates/velocities.html
# https://docs.astropy.org/en/stable/api/astropy.coordinates.SkyCoord.html#astropy.coordinates.SkyCoord.radial_velocity_correction

from astropy.coordinates import SkyCoord, EarthLocation
import astropy.units as u
from datetime import datetime
from astropy.time import Time

observationtime='2022-03-30'
RA="18h46m"
DEC="-2d36m"
home=EarthLocation.from_geodetic(lat=41.867, lon=-87.630, height=0)
cc=SkyCoord(ra=RA, dec=DEC, frame='icrs', unit=(u.hourangle,u.deg))

gc=cc.galactic    
print("Galactic Longitude")
GALLON=gc.l.deg  
print(GALLON)
print("Galactic Latitude")
GALLAT=gc.b.deg
print(GALLAT)
print(" ")

barycorr=cc.radial_velocity_correction(obstime=Time(observationtime), location=home)
barycorr.to(u.km/u.s)
print("barycentric correction")
print(barycorr)

heliocorr=cc.radial_velocity_correction('heliocentric',obstime=Time(observationtime), location=home)
heliocorr.to(u.km/u.s)
print("heliocentric correction")
print(heliocorr)
print(" ")

exit()
