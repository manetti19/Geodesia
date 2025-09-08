
import numpy as np

phi_deg = -(8 + 3/60 + 3.4697/3600)
lam_deg = -(34 + 57/60 + 5.4591/3600)
dXYZ = np.array([0.1, 0.3, 0.2], dtype=float)

phi = np.deg2rad(phi_deg)
lam = np.deg2rad(lam_deg)

sphi = np.sin(phi)
cphi = np.cos(phi)
slam = np.sin(lam)
clam = np.cos(lam)

A = np.array([
    [-sphi*clam, -slam,  cphi*clam],
    [-sphi*slam,  clam,  cphi*slam],
    [ cphi,       0.0,   sphi      ]
], dtype=float)

AT = A.T

dNEU = AT @ dXYZ

dN, dE, dU = dNEU[0], dNEU[1], dNEU[2]

print(f"ΔN = {dN:.6f} m")
print(f"ΔE = {dE:.6f} m")
print(f"ΔU = {dU:.6f} m")
