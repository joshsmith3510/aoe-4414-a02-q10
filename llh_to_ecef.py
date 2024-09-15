# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  Outputs x,y,z coordinates in the ECEF frame
#
# Written by Josh Smith
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
E_E=0.081819221456

# helper functions
## calc_denom
def calc_denom(ecc, lat_rad):
   return math.sqrt(1.0-ecc*ecc * math.pow(math.sin(lat_rad),2.0))

#   pass

# initialize script arguments
lat_deg = float('nan') # Latitude in Degrees
lon_deg = float('nan') # Longitude in Degrees
hae_km = float('nan') # Height above Ellipsoid in KM
# parse script arguments
if len(sys.argv)==4:
   lat_deg = float(sys.argv[1])
   lon_deg = float(sys.argv[2])
   hae_km= float(sys.argv[3])
   ...
else:
   print(\
      'Usage: '\
        'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
    )
   exit()

# write script below this line
lat_rad=lat_deg*(math.pi/180)
lon_rad=lon_deg*(math.pi/180)
denom=calc_denom(E_E,lat_rad)
C_E=R_E_KM/denom
S_E=R_E_KM*(1-E_E*E_E)/denom

r_x_km=(C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km=(C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km=(S_E+hae_km)*math.sin(lat_rad)

print('r_x_km= '+str(r_x_km))
print('r_y_km= '+str(r_y_km))
print('r_z_km= '+str(r_z_km))