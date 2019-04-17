import gpxpy
import googlemaps
import os


API_KEY = 'YOUR_API_KEY'



coords = []

for filename in os.listdir('gpx'):
	print (filename)
	gpx_file = open('gpx/' + filename)
	gpx = gpxpy.parse(gpx_file)
	for track in gpx.tracks:
	    for segment in track.segments:
	        for point in segment.points:
	            coords.append([float(point.latitude), float(point.longitude)])
	            print(f'Point at ({point.latitude}, {point.longitude}) -> {point.elevation}')


with open('map-outline.txt', 'r') as file:
	content = file.read()


def generate_html(points):
    f = open("map.html", "w")
    google_points = ",\n".join([f"new google.maps.LatLng({point[0]}, {point[1]})" for point in points])
    newFile = content.replace("LIST_OF_POINTS", google_points).replace("API_KEY", API_KEY)
    f.write(newFile)
    f.close()


generate_html(coords)
