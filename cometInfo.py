from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np

# VARIABLES
cometId = '3I' # Comet 3I/ATLAS
planets = { 'Mercury': '199', 'Venus': '299', 'Earth': '399', 'Mars': '499', 'Jupiter': '599', 'Saturn': '699', 'Uranus': '799', 'Neptune': '899'}
barycenter = '500@0'
timespec = Time('2025-07-01').jd # date of first observation in julian date

# CALCULATIONS
comet = Horizons(id = cometId, location = barycenter, epochs = timespec)
cometInfo = comet.elements()
cometVec = comet.vectors()
cometEph = comet.ephemerides()

# Velocity
cometVx = cometVec['vx'][0]
cometVy = cometVec['vy'][0]
cometVz = cometVec['vz'][0]

cometVAuDay = np.sqrt(cometVx**2 + cometVy**2 + cometVz**2) 
cometV = cometVAuDay * 1731.46


# OUTPUT
print("HOW DID IT PASS INTO THE SOLAR SYSTEM \n")

print(f"Eccentricty = {cometInfo['e'][0]}") # e > 1 means hyperbolic orbit
print(f"Velocity = {cometV} km/s")
print("\n")


print("WHY WAS THIS ONE DETECTED \n")

print(f"Total Apparent Magnitude at first observed date = {cometEph['Tmag'][0]}")
print("\n")


print("FACTORS MODULATING COMET FROM PERFECT KEPLARIAN ORBIT \n")

print("Large planetary bodies such as jupiter exert a large gravitational force")
print("Outgassing - Approaching the sun causes sublimation of ice on the comet, creating gas jets that alter its trajectory")
print("Measurement error and limited observation window")
print("\n")

print("BEST OBSERVATION TIME \n")

print("During approaches closest to earth since magnitude is greater and easier to observe")



# REFERENCES

'https://science.nasa.gov/solar-system/comets/'
'https://science.nasa.gov/solar-system/comets/3i-atlas/'