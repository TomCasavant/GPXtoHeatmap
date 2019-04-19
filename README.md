# GPXtoHeatmap
A complete explanation of this code can be found on [my website](https://tomcasavant.com/python,/gpx,/running,/heatmaps/2019/04/18/generating-heat-maps-from-gpx-files.html).
This program takes a series of gpx files and outputs an html file containing an interactive heatmap from gps data.

![example output](https://media.githubusercontent.com/media/TomCasavant/GPXtoHeatmap/master/heatmap.png "heatmap output example")

## Usage
Fill in the API_KEY in the config-example.ini file, and rename to config.ini

#### Command:

python heatmap.py (optional commands) --output OUTPUTFILE --input INPUTFOLDER --filter [running | walking | cycling]

- ouput defaults to "map"
- input defaults to "gpx"
- filter is by default null


#### Retrieving GPX Files
I use Garmin, and there was a tool to retrieve all gpx files from your account called [garminexport](https://github.com/petergardfjall/garminexport)
