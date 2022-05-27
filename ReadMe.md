Welcome.  The Python scripts in this repository allow the user to perform conversions between three astronomical coordinate systems:
-celestial (right ascension & declination)
-telescope (azimuth and altitude)
-galactic (galactic longitude and latitude)

The Astropy module is required.  Install this using:
$ pip install astropy
It is important to make sure that a recent version of numpy is installed.

For background on Astropy, see their website and examples:
https://www.astropy.org/
https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html#sphx-glr-generated-examples-coordinates-plot-obs-planning-py

Specific notes and examples are provided below, and are also included in the headers of the scripts.

converter.py
****************************
#Purpose:    Convert coordinates, using current clock time (options below)    
#Usage:      1-gc:aa, 2-gc:cc, 3-cc:aa, 4-cc:gc, 5-aa:gc, 6-aa:cc    
#Example:    python converter.py -f 1 -glong 180 -glat 5    
#Example:    python converter.py -f 2 -glong 180 -glat 5    
#Example:    python converter.py -f 3 -ra 12:20:00 -dec 40.5    
#Example:    python converter.py -f 4 -ra 12:20:00 -dec 40.5    
#Example:    python converter.py -f 5 -alt 45 -az 60    
#Example:    python converter.py -f 6 -alt 45 -az 60    
#Notes:      Program uses clock time from Pi (but there is option to enter manually)    

plot_gc.py
****************************
#Purpose:    Creates scatter plot of glat vs glong over 24 h period for a constant alt-az    
#Example:    python plot_gc.py -alt 70 -az 180    
#Notes:      Actual start date and time do not matter    

plot_alt.py
****************************
#Purpose:    Creates scatter plot of altitude vs time for specified object, over 24 hours    
#Purpose:    Includes altitudes of the sun and moon    
#Example:    python plot_alt.py -day 2021-09-23 -glong 180 -glat 0    
#Notes:      Altitudes of sun and moon are always at az=180 degrees. Object azimuth may be different    

plot_altaz.py
****************************
#Purpose:    Creates scatter plot of altitude vs azimuth for specified object, over 24 hours    
#Purpose:    Includes altitudes of the sun and moon    
#Example:    python plot_altaz.py -glong 180 -glat 0    
#Notes:      Be sure to input the latitude, longitude, date and time zone.  Do not change time. from 12:00    
#Notes:      Altitudes of sun and moon are always at az=180 degrees. Object azimuth may be different    

plot_sun.py
****************************
#Purpose:   Creates scatter plot of GALLAT vs GALLON for sun over 12-month period.    
#Example:   python plot_sun.py    
#Note:      Be sure to input the latitude, longitude. Date and time do not matter.    

cc-to-aa.py
****************************
#Purpose:   GUI converts celestial coordinates to alt-az coordinates    
#Example:   python cc-to-aa.py    
#Note:      Uses current clock time    

gc-to-aa.py
****************************
#Purpose:   GUI converts galactic coordinates to alt-az coordinates    
#Example:   python gc-to-aa.py    
#Note:      Uses current clock time    