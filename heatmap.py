import gpxpy
import click
import os
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')
API_KEY = parser.get('GOOGLE', 'API_KEY')
INITIAL_LATITUDE = parser.get('MAP', 'LATITUDE')
INITIAL_LONGITUDE = parser.get('MAP', 'LONGITUDE')
INITIAL_ZOOM = parser.get('MAP', 'ZOOM')

@click.command()
@click.option("--output", default="map", help="Specify the name of the output file. Defaults to `map`")
@click.option("--input", default="gpx", help="Specify an input folder. Defaults to `gpx`")
@click.option("--filter", default=None, help="Specify a filter type. Defaults to no filter", type=click.Choice(['running', 'cycling', 'walking']))
def main(output, input, filter):
    points = load_points(input, filter)
    generate_html(points, output)

def load_points(folder, filter):
    """Loads all gpx files into a list of points"""
    coords = []
    print (f"Loading files with type {filter}...") #Loads files with progressbar
    with click.progressbar(os.listdir(folder)) as bar:
        for filename in bar:
            if (filename.lower().endswith(".gpx")):
                #Verify file is a gpx file
                gpx_file = open(f'{folder}/' + filename)
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    if not filter or filter==track.type:
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
    if not os.path.exists('output'):
        os.mkdir('output')
    f = open(f"output/{file_out}.html", "w")
    outline = get_outline()
    google_points = ",\n".join([f"new google.maps.LatLng({point[0]}, {point[1]})" for point in points])
    updated_content = outline.replace("LIST_OF_POINTS", google_points).replace("API_KEY", API_KEY).replace("INIT_LATITUDE", INITIAL_LATITUDE).replace("INIT_LONGITUDE", INITIAL_LONGITUDE).replace("INIT_ZOOM", INITIAL_ZOOM)
    f.write(updated_content)
    f.close()


if __name__ == '__main__':
    main()
