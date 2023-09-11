import numpy as np
import argparse as ag
import matplotlib
matplotlib.rc('text', usetex=True)
import matplotlib.pyplot as plt
import matplotlib.tri as tri


names = ["sigma", "vr", "vp"]

def plotdataTri(file, var=0, rexp=None, cbar=False, cmap='magma', rmin=None, rmax=None, save=False, log=False, outname=None):
  data = np.loadtxt(file)

  x = data[:,0]
  y = data[:,1]
  r = np.sqrt(x**2 + y**2)
  sphi = y/r
  cphi = x/r
  vx = data[:,3]
  vy = data[:,4]

  if "masset-velasco" in file:
    #if velocities were given in the frame of the secondary....
    vx -= y
    vy += x

  if var == 0:
    field = data[:,2]
    cbl = r"$\Sigma$"
  if var == 1:
    #get vr
    field = cphi*vx + sphi*vy
    cbl = r"$v_r$"
  if var == 2:
    #get vphi
    field = cphi*vy - sphi*vx
    cbl = r"$v_\phi$"
  if rmin is None:
    rmin = np.min(r)
  if rmax is None:
    rmax = np.max(r)

  triang = tri.Triangulation(x, y)
  x1 = x[triang.triangles].mean(axis = 1)
  y1 = y[triang.triangles].mean(axis = 1)
  rt = np.sqrt(x1**2 + y1**2)
  mask = np.where( (rt < rmin) | (rt > rmax), 1, 0)
  triang.set_mask(mask)

  if rexp is not None:
    field *= r**rexp
    cbl = cbl+r'$r^{%.1f}$' % (rexp)
  if log:
    field = np.log10(field)
    cbl = r'$\rm{log(}$'+cbl+r'$\rm{)}$'

  plt.tripcolor(triang, field, cmap=cmap)
  if cbar:  plt.colorbar(label=cbl)
  plt.gca().set_aspect('equal')
  plt.xlim([-rmax,rmax])
  plt.ylim([-rmax,rmax])
  plt.tight_layout()
  if save:
    if outname is not None:
      plt.savefig(outname, dpi = 400)
    else:
      plt.savefig(names[var]+'.png', dpi=400)

    plt.cla()
  else: plt.show()

if __name__ == "__main__":

    parser = ag.ArgumentParser(description="Create time series plots for IMRI code comparison.")
    parser.add_argument('snapshot', help="snapshot (.dat) file to plot.")
    parser.add_argument('-v', '--var', type=int, default=0,
                            help="Variable to plot.")
    parser.add_argument('-cb', '--colorbar', action="store_true",
                            help="Add a colorbar to the plot.")
    parser.add_argument('-l', '--log', action="store_true",
                            help="set log scale")
    parser.add_argument('-s', '--save', action="store_true",
                            help="Save a PNG of the plot.")
    parser.add_argument('-rmax', '--rmax', type=float,
                            help="Set r maximum.")
    parser.add_argument('-rmin', '--rmin', type=float,
                            help="Set r minimum.")
    parser.add_argument('-rexp', '--rexp', type=float,
                            help="Scale the plotted value by some exponent of the radius")
    parser.add_argument('-cmap', '--colormap', type=str, default='magma',
                            help="Choose your own colormap")
    parser.add_argument('-out', '--outname', type=str, default=None,
                            help="name to use when saving file")

    args = parser.parse_args()
    file = args.snapshot
    var = args.var
    save = args.save
    log = args.log
    rmax = args.rmax
    rmin = args.rmin
    rexp = args.rexp
    cmap = args.colormap
    outname = args.outname
    cbar = args.colorbar

    plotdataTri(file, var=var, rexp=rexp, cbar=cbar, cmap=cmap, rmin=rmin, rmax=rmax, save=save, log=log, outname = outname)

