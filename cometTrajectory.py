from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np

# CONSTANTS
cometId = '3I' # Comet 3I/ATLAS
planets = { 'Mercury': '199', 'Venus': '299', 'Earth': '399', 'Mars': '499', 'Jupiter': '599', 'Saturn': '699', 'Uranus': '799', 'Neptune': '899'}
barycenter = '500@0'
timespec = {'start':'2025-01-01', 'stop':'2027-01-01', 'step':'1d'}

plotSize = 7


# CALCULATIONS

# Retrieve comet positions and time
comet = Horizons(id = cometId, location = barycenter, epochs = timespec)
cometVec = comet.vectors()
cometEph = comet.ephemerides()

cx =  cometVec['x']
cy = cometVec['y']
cz = cometVec['z']

time = cometVec['datetime_str']

area3sigma = cometEph['Area_3sigma']

# Retrieve planet positions + distance from comet
planetVecs = {}
planetDists = {}

closestApproaches = {}
cometClosestPos = {}

for name, id in planets.items():
    planet = Horizons(id = id, location = barycenter, epochs = timespec)
    planetVec = planet.vectors()
    
    planetVecs[name] = planetVec
    
    px = planetVec['x']
    py = planetVec['y']
    pz = planetVec['z']
    
    # Distance between comet and planet
    dist = np.sqrt((cx-px)**2 + (cy-py)**2 + (cz-pz)**2)
    planetDists[name] = dist
    
    # Closest approach for each planet
    closest = np.argmin(dist)
    closestApproaches[name] = {'time': time[closest], 
                               'distance': dist[closest],
                               'x': px[closest],
                               'y': py[closest]}
    
    # Comet position at each closest approach
    cometClosestPos[name] = {
        'x': cx[closest],
        'y': cy[closest]
    }

# Sorts closest approaches and selects only top 3 to show on figure
top3 = sorted(closestApproaches.items(), key = lambda item: item[1]['distance'])
top3 = top3[:3]


# OUTPUT

# PLOTS ORBIT THROUGHOUT SOLAR SYSTEM
plt.figure()

plt.plot(cx, cy, label = "3I/ATLAS")

for name, planetVec in planetVecs.items():
    plt.plot(planetVec['x'], planetVec['y'], label = name)

for name, data in top3:
    plt.scatter(data['x'], data['y'], label = f"Closest to {name}")
    
    cometPos = cometClosestPos[name]
    plt.scatter(cometPos['x'], cometPos['y'], color = 'blue')
    
    

plt.scatter(0, 0, color = 'yellow')  
plt.text(0, 0, "   Solar System Barycenter")

plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.title("3I/ATLAS Orbit through Solar System")

plt.xlim(-plotSize, plotSize)
plt.ylim(-plotSize, plotSize)

plt.legend()



# CLOSEST PLANET APPROACHES

plt.figure()

for name, planetDist in planetDists.items():
    plt.plot(time, planetDist, label = name)

for name, data in top3:
    plt.axvline(x = data['time'], color = 'red')
    
plt.xlabel("Date")
plt.ylabel("Distance (AU)")
plt.title("Distance between 3I/ATLAS and planets")

plt.legend()


# ERROR ELLPISE AREA VERSUS TIME

plt.figure()

plt.plot(time, area3sigma)

plt.xlabel("Date")
plt.ylabel("3sigma Error Ellipse Area (arcseconds^2)")
plt.title("Change in error ellipse over time for 3I/ATLAS")

plt.show()






















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