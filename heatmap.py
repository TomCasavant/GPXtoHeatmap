import gpxpy
import googlemaps
import os
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
API_KEY = parser.get('GOOGLE', 'API_KEY')


"""Loads all gpx files into a list of points"""
def load_points(folder):
    coords = []
    for filename in os.listdir(folder):
        print (filename)
        if (filename.endswith(".gpx")):
            gpx_file = open(f'{folder}/' + filename)
            gpx = gpxpy.parse(gpx_file)
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        coords.append([float(point.latitude), float(point.longitude)])
                        print(f'Point at ({point.latitude}, {point.longitude}) -> {point.elevation}')

    return (coords)


def get_outline():
    with open('map-outline.txt', 'r') as file:
        outline = file.read()
    return outline

def generate_html(points, file_out):
    f = open(f"{file_out}.html", "w")
    outline = get_outline()
    google_points = ",\n".join([f"new google.maps.LatLng({point[0]}, {point[1]})" for point in points])
    updated_content = outline.replace("LIST_OF_POINTS", google_points).replace("API_KEY", API_KEY)
    f.write(updated_content)
    f.close()


if __name__ == '__main__':
    points = load_points("gpx")
    generate_html(points, "map")
