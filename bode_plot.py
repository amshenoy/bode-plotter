import matplotlib.pyplot as plt
import numpy as np

f = np.logspace(-3,4,10000)
w = 2*np.pi*f
s = 1j*w # frequency response

H = ((2*s+3)*(s**2+2*s+3))/((s**2+2*s+1)*(s**2+3*s+2))

db_mag = 20*np.log10(np.abs(H))
phase = np.arctan2(np.imag(H),np.real(H))*180/np.pi

plt.figure()
plt.subplot(211)
plt.semilogx(f,db_mag)
plt.ylabel('dB Mag.')
plt.ylim([-120,50])
plt.subplot(212)
plt.semilogx(f,phase)
plt.xlabel('Freq. (Hz)')
plt.ylabel('Phase (deg.)')
plt.ylim([-185,185])
plt.yticks(np.arange(-180,185,45))

plt.show()

