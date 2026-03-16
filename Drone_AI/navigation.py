import math

drone_location = (0,0)

def calculate_distance(lat1,lon1,lat2,lon2):

    R = 6371

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2

    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distance = R*c

    return distance


def estimate_arrival(distance,speed=40):

    time = distance/speed

    return time