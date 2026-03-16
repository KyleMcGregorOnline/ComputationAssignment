from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np

cometId = '3I' # Comet 3/I ATLAS
planets = { 'Mercury': '199', 'Venus': '299', 'Earth': '399', 'Mars': '499', 'Jupiter': '599', 'Saturn': '699', 'Uranus': '799', 'Neptune': '899'}
barycenter = '500@0'
timespec = Time('2025-07-01').jd # date of first observation in julian date

comet = Horizons(id = cometId, location = barycenter, epochs = timespec)
cometInfo = comet.elements()
cometVec = comet.vectors()

cometVx =cometVec['vx'][0]
cometVy =cometVec['vy'][0]
cometVz =cometVec['vz'][0]

cometVAuDay = np.sqrt(cometVx**2 + cometVy**2 + cometVz**2) 
cometV = cometVAuDay * 1731.46


# How did it pass into the Solar System?
print("HOW DID IT PASS INTO THE SOLAR SYSTEM \n")

print(f"Eccentricty = {cometInfo['e'][0]}")
print(f"Velocity = {cometV} km/s")