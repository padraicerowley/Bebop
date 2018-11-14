import geocoder

def getLatLon(placeName):
    g = geocoder.google(placeName)
    return g.latlng
