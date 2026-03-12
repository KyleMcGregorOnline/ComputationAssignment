from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt

cometId = '3I' # Comet 3/I ATLAS
planets = { 'Mercury': '199', 'Venus': '299', 'Earth': '399', 'Mars': '499', 'Jupiter': '599', 'Saturn': '699', 'Uranus': '799', 'Neptune': '899'
} # Planets Mercury to Neptune

barycenter = '500@0'
timespec = {'start':'2025-01-01', 'stop':'2027-01-01', 'step':'1d'} # Rough dates of comets travel through solar system



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

# Plots solar system and comet traj
plt.figure()

# Comet trajectory
plt.plot(cometVec['x'], cometVec['y'])

# Planet orbits
for name, planetVec in planetVecs.items():
    plt.plot(planetVec['x'], planetVec['y'], label = name)
    
plt.scatter(0, 0)  

plt.xlabel("x")
plt.ylabel("y")
plt.title("3/I ATLAS Orbit around sun")
plt.text(0,0, "   Solar System Barycenter")

plt.xlim(-30, 30)
plt.ylim(-30, 30)

plt.legend()

plt.show()
