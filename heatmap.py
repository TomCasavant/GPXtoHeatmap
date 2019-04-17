import gpxpy
import googlemaps
import click
import os
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
API_KEY = parser.get('GOOGLE', 'API_KEY')

@click.command()
@click.option("--output", default="map", help="Specify the name of the output file")
def main(output):
    points = load_points("gpx")
    generate_html(points, output)

def load_points(folder):
    """Loads all gpx files into a list of points"""

    coords = []
    print ("Loading files...") #Loads files with progressbar
    with click.progressbar(os.listdir(folder)) as bar:
        for filename in bar:
            if (filename.endswith(".gpx")):
                #Verify file is a gpx file
                gpx_file = open(f'{folder}/' + filename)
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    for segment in track.segments:
                        for point in segment.points:
                            coords.append([float(point.latitude), float(point.longitude)])

    return (coords)

def get_outline():
    """Reads in the html outline file"""
    with open('map-outline.txt', 'r') as file:
        outline = file.read()
    return outline

def generate_html(points, file_out):
    """Generates a new html file with points"""
    f = open(f"output/{file_out}.html", "w")
    outline = get_outline()
    google_points = ",\n".join([f"new google.maps.LatLng({point[0]}, {point[1]})" for point in points])
    updated_content = outline.replace("LIST_OF_POINTS", google_points).replace("API_KEY", API_KEY)
    f.write(updated_content)
    f.close()


if __name__ == '__main__':
    main()
