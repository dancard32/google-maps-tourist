from datetime import datetime
from enum import Flag
from pprint import pprint
import googlemaps
import requests
import json

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Global Variables
# API key IP Address Restricted - Safe to show
API_key = 'AIzaSyDaTIF0t-wQ_WLUb920Gfq4lAS_8wXt2nw'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plotMaps(latitude, longitude):
    import gmplot
    import numpy as np

    lat_mean = np.mean(latitude)
    long_mean = np.mean(longitude)
    
    d_lat = abs(max(latitude) - min(latitude))
    d_long = abs(max(longitude) - min(longitude))

    z1 = 2; x1 = 180
    z2 = 20; x2 = 1/(360*60)
    zoom = 4/5*((z2 - z1)/(x2 - x1)*(max([d_lat, d_long])-x1)+z1)

    gmap = gmplot.GoogleMapPlotter(lat_mean, long_mean, zoom=zoom)
    gmap.scatter(latitude, longitude, '#ff0000', size=50, marker=False)
    gmap.plot(latitude, longitude, 'blue', edge_width=2.5)
    gmap.draw("map.html")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """
        Google API for Project
        #~~~~~~~~~~~~~~~~~~~~~~~~
        Directions API
        Distance Matrix API
        Geocoding API
        Maps Static API
        Places API
    """

    lats = [19.0790, 19.0810, 19.0850]
    longs = [72.890, 72.910, 72.930]
    plotMaps(lats, longs)

    """
        Obtain start and end points
    """

    """
        geocode the starts and ends
    """

    """
        Create a route between the start and end point
    """

    """
        data scrape the route for recommended locations (> 4-star) "en-route" from Google Info
    """

    """
        With a list of potential locations to visit optimize the route
        via traveling sales-man method to reduce time off optimal route
        while increasing the amount of places visited

        - to avoid trivial results group in accordance to North/East/South/West
          else there may be lots of zig-zagging across the optimal route
    """

    """
        With the routes found and the groups split in N/E/S/W take the shorter recommended
        route and return and compare/contrast against the optimal
    """

def junk():

    """
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key="+API_key

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)


    with open('data.json', 'w') as outfile:
        json.dump(response.text, outfile)

    print(response.text, response, type(response))

    gmaps = googlemaps.Client(key=API_key)
    print(dir(gmaps))

    loc = '101 N Main St. Clearfield, UT'
    response = gmaps.geocode(loc)
    pprint(response)

    # Geocoding an address

    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                        "Parramatta, NSW",
                                        mode="transit",
                                        departure_time=now)

    """
if __name__ == "__main__":
    main()