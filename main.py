from datetime import datetime
from pprint import pprint
import googlemaps
import numpy as np
import requests
import json



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Global Variables
# API key IP Address Restricted - Safe to show
API_key = 'AIzaSyDaTIF0t-wQ_WLUb920Gfq4lAS_8wXt2nw'
gmaps = googlemaps.Client(key=API_key)  # Initialize Google Maps API
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plotMaps(latitude, longitude, tourist_latitude, tourist_longitude, tourist_waypoints, names):
    import gmplot
    
    lat_mean = np.mean(latitude)
    long_mean = np.mean(longitude)
    
    d_lat = abs(max(latitude) - min(latitude))
    d_long = abs(max(longitude) - min(longitude))

    z1 = 2; x1 = 180
    z2 = 20; x2 = 1/(360*60)
    zoom = ((z2 - z1)/(x2 - x1)*(min([d_lat, d_long])-x1)+z1)/2.5

    # Plot the directions on Google Maps
    gmap = gmplot.GoogleMapPlotter(lat_mean, long_mean, zoom=zoom, apikey=API_key)
    #gmap.directions((latitude[0], longitude[0]), (latitude[len(latitude) - 1], longitude[len(latitude) - 1]))
    gmap.directions((tourist_latitude[0], tourist_longitude[0]),  (tourist_latitude[len(tourist_latitude) - 1], tourist_longitude[len(tourist_latitude) - 1]), waypoints=tourist_waypoints)
    gmap.scatter(latitude, longitude, '#ff0000', size=100, marker=False)
    gmap.scatter(tourist_latitude, tourist_longitude, '#00FFFF', size=100, marker=False)
    for i in range(len(names)):
        gmap.text(tourist_waypoints[i][0], tourist_waypoints[i][1], names[i])
    gmap.enable_marker_dropping('orange', draggable=True)
    gmap.draw("map.html")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def parseRoute(route):
    lats = [route[0]['legs'][0]['start_location']['lat']]
    lngs = [route[0]['legs'][0]['start_location']['lng']]
    for leg in route[0]["legs"]:
        
        for i in range(len(leg['steps'])):
            step = leg['steps'][i]
            
            lats.append(step["end_location"]["lat"])
            lngs.append(step["end_location"]["lng"])

    return lats, lngs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bestPlace(places):
    results = dict()

    entry = 0
    for lists in places['results']:
        if 'business_status' in lists.keys():
            if 'rating' in lists.keys():
                if lists['rating'] >= 4.5 and lists['user_ratings_total'] >= 500:
                    results[str(entry)] = lists
                    entry += 1   
    highest_rating = 0
    bestPlace = {}
    for i in range(len(results)):
        if results[str(i)]['rating'] > highest_rating:
            highest_rating = results[str(i)]['rating'] 
            bestPlace = results[str(i)]

    return bestPlace
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """
        Google API approved for Project 
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Directions API
        Distance Matrix API
        Geocoding API
        Maps Static API
        Places API
    """

    # Obtain start and end points
    start_loc = 'Madison, WI'
    end_loc = 'Denver'
    
    # Create a route between the start and end point
    directions = gmaps.directions(start_loc, end_loc,
               mode=None, waypoints=None, alternatives=False, avoid=None,
               language=None, units=None, region=None, departure_time=None,
               arrival_time=None, optimize_waypoints=False, transit_mode=None,
               transit_routing_preference=None, traffic_model=None)
    # Take data from directions and update map
    lats, lngs = parseRoute(directions)

    # Data scrape the route at each waypoint to find locations with > 4-star reviews
    # and with over 500 user reviews with type = tourist, park, or point of interest
    
    tourist_names = []; way_points = []
    for i in np.arange(1, len(lats)-1):
        placed_by = gmaps.places_nearby(location=[lats[i], lngs[i]],
                    radius=1e4, keyword=None, language='english', min_price=None, 
                    max_price=None, name=None, open_now=False, rank_by=None, 
                    type=['tourist_attraction', 'park', 'point_of_interest'],
                    page_token=None,)
        tourist_area = bestPlace(placed_by)
        if tourist_area:
            if tourist_area['name'] not in tourist_names:
                tourist_names.append(tourist_area['name'])
                print(tourist_area['name'])
                way_points.append((tourist_area['geometry']['location']['lat'], tourist_area['geometry']['location']['lng']))
    
    # Create a route between the start and end point
    tourist_route = gmaps.directions(start_loc, end_loc,
               mode=None, waypoints=tourist_names, alternatives=False, avoid=None,
               language=None, units=None, region=None, departure_time=None,
               arrival_time=None, optimize_waypoints=True, transit_mode=None,
               transit_routing_preference=None, traffic_model=None)
    # Take data from directions and update map
    tour_lats, tour_lngs = parseRoute(tourist_route)
    
    plotMaps(lats, lngs, tour_lats, tour_lngs, way_points, tourist_names)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    main()