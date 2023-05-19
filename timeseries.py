import numpy as np
import argparse as ag
import matplotlib
matplotlib.rc('text', usetex=True)
import matplotlib.pyplot as plt
import glob


def plotdata(files, vars=[1], save=False, doOrbitAverage=False, Navg=1, xlim=[None,None], ylim=[None,None]):
  for var in vars:
    for file in files:
      d = np.loadtxt(file)
      t = d[:,0]
      v = d[:,var]

      label = file[file.find('/')+1:file.find('_')]
      if label=="masset-velasco" and var>0: v*=10**-4
      if doOrbitAverage:
        T = np.unique(t.astype('int')).astype('float')[::Navg]
        norb = len(T)
        V = np.empty(norb)
        for i in range(1,norb):
          inds = (t>T[i-1])&(t<T[i])
          V[i]=np.mean(v[inds])
        plt.plot(T, V, label=r'$\rm{'+label+'}$')
      else:
        plt.plot(t, v, label=r'$\rm{'+label+'}$')

    plt.xlabel('time')
    plt.ylabel(labels[var])
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.legend()
    if save:
      plt.savefig(names[var]+'.pdf')
      plt.cla()
    else: plt.show()

if __name__ == "__main__":

    parser = ag.ArgumentParser(description="Create time series plots for IMRI code comparison.")
    parser.add_argument('-v', '--vars', nargs='+', type=int, default=[1],
                            help="Variables to plot.")
    parser.add_argument('-a', '--average', nargs='?', type=int, default=0,
                            help="Average over some number of orbital periods.")

    parser.add_argument('-s', '--save', nargs='?', type=int, default=0,
                            help="Save a PDF of the plot.")

    parser.add_argument('-n', '--navg', nargs='?', type=int, default=1,
                            help="Number of orbits to average over.")

    parser.add_argument('-xmax', '--xmax', type=float,
                            help="Set x maximum.")
    parser.add_argument('-xmin', '--xmin', type=float,
                            help="Set x minimum.")

    parser.add_argument('-ymax', '--ymax', type=float,
                            help="Set y maximum.")
    parser.add_argument('-ymin', '--ymin', type=float,
                            help="Set y minimum.")

    args = parser.parse_args()

    vars = args.vars
    Navg = args.navg
    doOrbitAverage = args.average
    save = args.save

    xlim = [args.xmin, args.xmax]
    ylim = [args.ymin, args.ymax]

    labels = ['time', 'torque on secondary', 'torque on secodnary (excluding smoothing region)', 'torque on primary']
    names = ['time','torqueM2', 'torqueM2_soft', 'torqueM1']

    files = glob.glob('data/*.dat')
    plotdata(files, vars=vars, save=save, doOrbitAverage=doOrbitAverage, Navg=Navg, xlim=xlim, ylim=ylim)
