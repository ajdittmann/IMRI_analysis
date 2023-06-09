# IMRI analysis

A collection of scripts for analyzing simulation outputs from the LISA disk-IMRI project.

### Scripts
`timeseries.py` - A script which makes a quick plot of all of the files in the `TimeSeries` directory (for now, in the future I/someone should let the user chose which files to plot).
One can use `-v` or `--vars` to chose which quantities to plot on the y axis.
Using the `-a` or `--average` option will average the outputs over a number of orbital periods set by the `-n`/`--navg` option. Using `-s` or `--save`, will save a pdf of the plot - otherwise an interactive matplotlib window will be opened. Passing values to `--xmin`, `--xmax`, `--ymin`, and `--ymax` can control the plotting limits, and using `-l` or `--linear` will plot a [torque prediction](https://ui.adsabs.harvard.edu/abs/2002ApJ...565.1257T/abstract).
For example 
```
python timeseries.py -v 1 3 --xmin 0 --xmax 1 
```
will bring up plots of the torque on primary and secondary over the first orbit.


`triplot2D.py' - A simple script that attempts to plot surface density distributions using Delaunay triangulations. 
