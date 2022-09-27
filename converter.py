#Name:       converter.py
#Purpose:    Performs coordinate conversions between galactic, celestial and telescope
#Usage:      1-gc:aa, 2-gc:cc, 3-cc:aa, 4-cc:gc, 5-aa:gc, 6-aa:cc
#Usage:      python converter.py -f 1 -glong 180 -glat 5
#Usage:      python converter.py -f 2 -glong 180 -glat 5
#Usage:      python converter.py -f 3 -ra 12:20:00 -dec 40.5
#Usage:      python converter.py -f 4 -ra 12:20:00 -dec 40.5
#Usage:      python converter.py -f 5 -alt 45 -az 60
#Usage:      python converter.py -f 6 -alt 45 -az 60

import numpy as np
from datetime import datetime
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

import argparse
parser = argparse.ArgumentParser(description='converter.py')
parser.add_argument("-f", "--flag", help="Enter flag", type=int)
parser.add_argument("-glong", "--glong", help="Enter galactic longitude in degrees", type=float)
parser.add_argument("-glat", "--glat", help="Enter galactic latitude in degrees", type=float)
parser.add_argument("-ra", "--ra", help="Enter RA as 01h22.5m", type=str)
parser.add_argument("-dec", "--dec", help="Enter declination in degree decimal format", type=float)
parser.add_argument("-alt", "--alt", help="Enter altitude in degree decimal format", type=float)
parser.add_argument("-az", "--az", help="Enter azimuth in degree decimal format", type=float)
args = parser.parse_args()
FLAG=args.flag
GALLON=args.glong;GALLAT=args.glat
RA=args.ra;DEC=args.dec
ALT=args.alt;AZ=args.az

print(" ")
print("1-gc:aa, 2-gc:cc, 3-cc:aa, 4-cc:gc, 5-aa:gc, 6-aa:cc")
print("aa use -alt and -az")
print("gc use -glong and -glat")
print("cc use -ra and -dec")
print("for ra only, example=01h22.5m")
print(" ")

#Location Info
LATITUDE=41.867; LONGITUDE=-87.630
Chicago = EarthLocation(lat=LATITUDE*u.deg, lon=LONGITUDE*u.deg, height=0*u.m)
print("Latitude",LATITUDE,"Longitude",LONGITUDE)

#DATETIME OPTION 1: Use Current Clock Time to automatically find universal time
UNIVERSALTIME=Time.now()
print("Using clock time.  To set date and time manually, see directions in script")
'''
#DATETIME OPTION 2: Set Date and Time Manually
LOCALTIME="2022-09-26 20:32:0.0"  #enter local time manually
time_zone=-5.0                    #-6.0 Nov-Mar (CENTRAL STANDARD TIME), -5.0 Mar-Nov (DST)
utcoffset = time_zone*u.hour
UNIVERSALTIME = Time(LOCALTIME) - utcoffset
print("Using local time entered into script by user.")
print(LOCALTIME)
print("Time zone correction=",time_zone)
print("To use clock time, see directions in script.")
'''
print("Universal Time")
print(UNIVERSALTIME)

print(" ")

#F1-Convert galactic to alt-az coordinates
if FLAG==1:
    gc=SkyCoord(l=GALLON*u.degree, b=GALLAT*u.degree, frame='galactic')
    aa = gc.transform_to(AltAz(obstime=UNIVERSALTIME,location=Chicago))
    altitude=float(round(aa.alt.deg,1))
    azimuth=float(round(aa.az.deg,1))
    print("Altitude ",altitude)
    print("Azimuth ",azimuth)

#F2-Convert galactic to celestial coordinates
if FLAG==2:
    gc = SkyCoord(l=GALLON*u.degree, b=GALLAT*u.degree, frame='galactic')
    celestial=gc.icrs
    ra=celestial.ra.hms
    dec=celestial.dec.dms
    print("RA ",ra)
    print("DEC ",dec)

#F3-Convert celestrial to alt-az coordinates
if FLAG==3:
    cc = SkyCoord(ra=RA, dec=DEC, frame='icrs', unit=(u.hourangle,u.deg))
    aa = cc.transform_to(AltAz(obstime=UNIVERSALTIME,location=Chicago))
    altitude=float(round(aa.alt.deg,1))
    azimuth=float(round(aa.az.deg,1))
    print("Altitude ",altitude)
    print("Azimuth ",azimuth)

#F4-Convert celestial to galactic coordinates
if FLAG==4:
    cc = SkyCoord(ra=RA, dec=DEC, frame='icrs', unit=(u.hourangle,u.deg))
    gc=cc.galactic     
    GALLON=gc.l.deg   
    GALLAT=gc.b.deg
    print("Galactic Longitude ",GALLON)
    print("Galactic Latitude ",GALLAT)

#F5-Convert alt-az to galactic coordinates
if FLAG==5:
    aa=SkyCoord(alt=ALT*u.degree, az=AZ*u.degree, frame='altaz',location=Chicago,obstime=UNIVERSALTIME)
    gc=aa.galactic
    GALLON=gc.l.deg
    GALLAT=gc.b.deg
    print("Galactic Longitude ",GALLON)
    print("Galactic Latitude ",GALLAT)

#F6-Convert alt-az to celestial coordinates
if FLAG==6:
    aa=SkyCoord(alt=ALT*u.degree, az=AZ*u.degree, frame='altaz',location=Chicago,obstime=UNIVERSALTIME)
    cc=aa.icrs
    RA=cc.ra.hms
    DEC=cc.dec.deg
    print("RA ",RA)
    print("DEC ",DEC)

print(" ")
exit()
