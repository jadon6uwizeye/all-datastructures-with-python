from math import radians, sin, cos, sqrt, atan2,asin
#This function calculate Distance between two points on earth 
# based on their longetude and latitude and returns the distance in km.
def get_distance(lat1, lat2, long1, long2):
    
    #Coverts the lat and long from degrees to radians
    lat1=radians(lat1)
    lat2=radians(lat2)
    long1=radians(long1)
    long2=radians(long2)

    #Using Harversine formula
    distance_lat=lat2-lat1
    distance_long=long2-long1
    earth_radius_in_km=6371.0

    distance_in_km =(2*asin(sqrt((sin(distance_lat/2))**2 
    + cos(lat1)*cos(lat2) * (sin(distance_long/2))**2))
    ) * earth_radius_in_km

    return distance_in_km