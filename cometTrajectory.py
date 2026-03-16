from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt

cometId = '3I' 
planets = { 'Mercury': '199', 'Venus': '299', 'Earth': '399', 'Mars': '499', 'Jupiter': '599', 'Saturn': '699', 'Uranus': '799', 'Neptune': '899'}
barycenter = '500@0'
timespec = {'start':'2025-05-01', 'stop':'2026-03-16', 'step':'1d'} # Rough dates of comets travel through solar system

plotSize = 7


# Retrieve comet positions
comet = Horizons(id = cometId, location = barycenter, epochs = timespec)
cometVec = comet.vectors()

# Retrieve planet positions
planetVecs = {}
for name, id in planets.items():
    planet = Horizons(id = id, location = barycenter, epochs = timespec)
    planetVecs[name] = planet.vectors()


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

# PLOTS ORBIT THROUGHOUT SOLAR SYSTEM
plt.figure()

# Comet and Planet trajectory
plt.plot(cometVec['x'], cometVec['y'])
for name, planetVec in planetVecs.items():
    plt.plot(planetVec['x'], planetVec['y'], label = name)
    
plt.scatter(0, 0)  

plt.xlabel("x")
plt.ylabel("y")
plt.title("3/I ATLAS Orbit through Solar System")
plt.text(0,0, "   Solar System Barycenter")

plt.xlim(-plotSize, plotSize)
plt.ylim(-plotSize, plotSize)

plt.legend()

plt.show()
