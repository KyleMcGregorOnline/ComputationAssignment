from astroquery.jplhorizons import Horizons
from astropy.time import Time


cometId = '3I' # Comet 3/I ATLAS
cometObserverLocation = '500' # Geocentric
cometTimeSpec = {'start':'2025-07-01', 'stop':'2026-02-01', 'step':'1d'} # Starting from comets entry to approximate exit with step of 1 day.


comet = Horizons(id = cometId, location = cometObserverLocation, epochs = cometTimeSpec)

# Print ephemerides
eph = comet.ephemerides()
print(eph)

