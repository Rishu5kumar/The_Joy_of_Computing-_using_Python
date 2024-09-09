'''
Global positioning system:- It is something that lets you share your location or track your route using google maps.
It is a network of satellites that help tracking the geographical locations of an individual 
'''

import csv
from gmplot import gmplot

# now place map to a particular coordinate
gmap = gmplot.GoogleMapPlotter(28.689169, 77.324448, 17) # 17 is the zoom resolutio
n
# gmap contains the map location where i want to plot the place

# now second thing is icon which i am going to use to plot my routes
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv','r') as f:
    reader = csv.reader(f)
    # it will create a iterator through this file
    # so that i can iterate over it and read the values one by one as the list
    
    k = 0
    for row in reader:
        # row will contain list so each item of this list will be a value separated by comma in string
        lat = float(row[0])
        long = float(row[1])
        
        # print(lat)
        # print(long)
        # print(lat+long)

        if k==0:
            gmap.marker(lat,long, "yellow")
            k = 1
        else:
            gmap.marker(lat, long, "blue")
          
gmap.marker(lat, long, "red")
gmap.draw("mymap.html")
# now plot this on google map we need a different library named gmplot
