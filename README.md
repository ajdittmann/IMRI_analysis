# IMRI analysis

A collection of scripts for analyzing simulation outputs from the LISA disk-IMRI project.

### Scripts
`timeseries.py` - A script which makes a quick plot of all of the files in the `TimeSeries` directory (for now, in the future I/someone should let the user chose which files to plot).
One can use `-v` or `--vars` to chose which quantities to plot on the y axis.
The `-a` or `--average` option can be set to `1` to average the outputs over a number of orbital periods set by the `-n`/`--navg` option. By setting `-s 1` or `--save 1`, a pdf of the plot will be saved - otherwise an interactive matplotlib window will be opened. Passing values to `--xmin`, `--xmax`, `--ymin`, and `--ymax` can control the plotting limits.
For example 
```
python timeseries.py -v 1 3 --xmin 0 --xmax 1 
```
will bring up plots of the torque on primary and secondary over the first orbit.
