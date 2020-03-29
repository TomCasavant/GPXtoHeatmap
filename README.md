# GPXtoHeatmap
A complete explanation of this code can be found on [my website](https://tomcasavant.com/python,/gpx,/running,/heatmaps/2019/04/18/generating-heat-maps-from-gpx-files.html).
This program takes a series of gpx files and outputs an html file containing an interactive heatmap from gps data.

![example output](https://media.githubusercontent.com/media/TomCasavant/GPXtoHeatmap/master/heatmap.png "heatmap output example")


## Usage

**Install Dependencies**

```bash
$ python3 -m pip install -r requirements.txt
```

**Configure environment**

```bash
$ MY_GOOGLE_API_KEY="..."
$ cp config-example.ini config.ini
$ sed -i "s/####/$MY_GOOGLE_API_KEY/g" config.ini
$ cat config.ini
[GOOGLE]
API_KEY = <your API key should be here>
```

#### Command:

Show help:
```bash
$ python3 heatmap.py --help
Usage: heatmap.py [OPTIONS]

Options:
  --output TEXT                   Specify the name of the output file.
                                  Defaults to `map`
  --input TEXT                    Specify an input folder. Defaults to `gpx`
  --filter [running|cycling|walking]
                                  Specify a filter type. Defaults to no filter
  --help                          Show this message and exit.
```

Examples:
```bash
$ python3 heatmap.py
$ python3 heatmap.py --input gpx --output map
```

#### Retrieving GPX Files

- Garmin users can use [garminexport](https://github.com/petergardfjall/garminexport) to export GPX data.
- Strava users can follow [Strava's instructions](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export) to export GPX data

**Note:** [GPSBabel](https://www.gpsbabel.org/download.html) tool may help you convert from file formats such as `.tcx` to `.gpx` files
