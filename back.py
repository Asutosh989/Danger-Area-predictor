from math import radians, cos, sin, asin, sqrt
def haversine(a,b):
    # convert decimal degrees to radians
    km_l = []
    for i in range(len(b)):
        lat1,lon1,lat2,lon2 = a[0],a[1],b[i][0],b[i][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        x = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(x))
        km = 6367 * c
        km_l.append("{0:.2f}".format(km))
    km_l.sort()
    return km_l
