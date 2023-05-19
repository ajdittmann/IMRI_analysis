import numpy as np
import matplotlib
matplotlib.rc('text', usetex=True)
import matplotlib.pyplot as plt
import glob
#f1 = 'derdzinski_disco_r600log_q1e-4_hr10.dat'
#f2 = 'dittmann_athenapp_nx128_1em4_1em1.dat'
#f3 = 'masset-velasco_fargo3d_448x1562_1e-4_0.1_alpha0.1.dat'

#files = [f1,f2,f3]
files = glob.glob('*.dat')
for file in files:
  d = np.loadtxt(file)
  t = d[:,0]
  t2 = d[:,1]
  #if file==f3: t2*=10**-4
  label = file[:file.find('_')]
  plt.plot(t, t2, label=r'$\rm{'+label+'}$')

#plt.xlabel('time (first column)')
#plt.ylabel('torque on secondary (second column)')
plt.xlabel('time')
plt.ylabel('torque on secondary')
plt.legend()
plt.show()
#plt.savefig('imriTorque.pdf')
