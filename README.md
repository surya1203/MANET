# MANET

11/01/21
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Geodetic Distance file created.
d : Geodetic Distance
r : Radius of Earth
phi : Longitude in radians
lambda : latitude in radians


h = hav(delta phi) + [ cos(phq1) x cos(phi2) x hav(delta lambda)]
since: hav x = sin^2 (x/2)
h = sin^2 (delta phi/2) + [ cos(phq1) x cos(phi2) x sin^2 (delta lambda/2]

d = r x archav (h)
since: archav (h) = 2 arcsin(sqrt(h))
d = r x 2 arcsin(sqrt(h))
