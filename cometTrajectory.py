from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt

cometId = '3I' # Comet 3/I ATLAS
cometObserverLocation = '500@0' # barycenter
cometTimeSpec = {'start':'2025-07-01', 'stop':'2026-02-01', 'step':'1d'} # Starting from comets entry to approximate exit with step of 1 day.

comet = Horizons(id = cometId, location = cometObserverLocation, epochs = cometTimeSpec)

# Print ephemerides
'''
eph = comet.ephemerides()
#print(eph)
'''

# Plot RA, DEC of trajectory
'''
plt.figure(figsize=(10,5))
plt.plot(eph['RA'], eph['DEC'])
plt.xlabel('RA')
plt.ylabel('DEC')
plt.title('3/I ATLAS Path across sky')
plt.show()
'''

vec = comet.vectors()

plt.figure()
plt.plot(vec['x'], vec['y'])
plt.scatter(0, 0)  

plt.xlabel("x")
plt.ylabel("y")
plt.title("3/I ATLAS Orbit around sun")
plt.text(0,0, "   Solar System Barycenter")

plt.xlim(-5, 5)
plt.ylim(-5,5)

plt.show()
